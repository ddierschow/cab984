#!/usr/local/bin/python
# -*- coding: utf8 -*-

import os, re, sys
import basics
import config
import useful

'''
VariationImportData
get_file_list
get_model_ids
get_html_tables
show_file_settings

transform_header
header_column_change
transform_row
row_column_change
'''


# ------ initialize data -------------------------------------


# Decorator for reading data files
def read_data_file(main_fn):
    def read_dat(fn):
        dat = open(os.path.join(config.SRC_DIR, fn + '.dat')).readlines()
        dat = filter(lambda x: x and not x.startswith('#'), [ln.strip() for ln in dat])
        return main_fn(dat)
    return read_dat


@read_data_file
def read_column_change(fil):
    changes = dict()
    for ln in fil:
        mnl, col, colto = ln.split('|')
        for mn in mnl.split(';'):
            changes.setdefault(mn, list())
            changes[mn].append([col.split(';'), colto.split(';')])
    return changes


@read_data_file
def read_cell_change(fil):
    changes = dict()
    for ln in fil:
        mnl, col, replfrom, replto = ln.split('|')[0:4]
        for mn in mnl.split(';'):
            changes.setdefault(mn, list())
            if replfrom.startswith('r/'):
                changes[mn].append([col, re.compile(replfrom[2:]), replto])
            else:
                changes[mn].append([col, replfrom, replto])
    return changes


@read_data_file
def read_plants(fil):
    return [re.compile(ln) for ln in fil]


@read_data_file
def read_trans(fil):
    changes = list()
    for ln in fil:
        transfrom, transto = ln.split('|')[:2]
        transfrom = transfrom.replace('.', r'\.').replace(' ', r'\s').replace('>', r'\b')
        changes.append([re.compile(transfrom), transto])
    return changes


@read_data_file
def read_filenames(fil):
    changes = list()
    for ln in fil:
        transfrom, transto = ln.split('|')[:2]
        changes.append([re.compile('^%s$' % transfrom) if '?' in transfrom else transfrom, transto.split(';') if transto else []])
    return changes


class VariationImportData:

    # ------ html ------------------------------------------------

    cmt_re = re.compile(r'<!--.*?-->', re.S)
    hln_re = re.compile(r'\\hline')
    mup_re = re.compile(r'<[^>]*>', re.S)
    tab_re = re.compile(r'<table[^>]*>(?P<c>.*?)</table>', re.S)
    row_re = re.compile(r'<tr[^>]*>(?P<c>.*?)</tr>', re.S)
    cel_re = re.compile(r'<t(?P<t>[hd])[^>]*>(?P<c>.*?)</t[hd]>', re.S)
    div_re = re.compile('</?div.*?>', re.S | re.M)

    column_split_delim = {
        'body_license_plate': ' ',
        'windows_rear_side_window_corners': ',',
    }

    last_change = [
        [re.compile("\(\s+"), " ("],
        [re.compile("\s+\)"), ") "],
        [re.compile("\s+,"), ","],
        [re.compile("^\s+"), ""],  # do these three last
        [re.compile("\s+$"), ""],
        [re.compile("\s+"), " "],
    ]

    def __init__(self, verbose=False):
        self.verbose = verbose

        self.fnam_change = read_filenames('vfilename')
        self.manu_change = read_plants('vplants')
        self.cell_change = read_trans('vtrans')
        self.head_change = read_trans('vheads')
        self.base_change = read_column_change('vbases')
        self.clmn_change = read_column_change('vcolumns')
        self.prep_change = read_cell_change('vpre')
        self.post_change = read_cell_change('vpost')

    # ------ data ------------------------------------------------

    def get_html_tables(self, fn):
        f = open(fn).read()
        f = self.cmt_re.sub('', f)
        f = self.hln_re.sub('', f)
        f = self.div_re.sub('', f)

        tables = list()
        while 1:
            fitab = self.tab_re.search(f)
            if not fitab:
                rest = f
                break

            pred = f[:fitab.start()]
            tab_con = fitab.group('c')
            rows = list()
            while 1:
                row = self.row_re.search(tab_con)
                if not row:
                    break

                row_con = row.group('c')
                cels = list()
                while 1:
                    cel = self.cel_re.search(row_con)
                    if not cel:
                        break

                    cel_con = self.mup_re.sub('', cel.group('c'))
                    cels.append(cel_con)

                    row_con = row_con[cel.end():]
                tab_con = tab_con[row.end():]
                rows.append(cels)
            f = f[fitab.end():]
            tables.append([pred, rows, ''])
        if tables:
            tables[-1][-1] = rest
        else:
            tables.append(['', list(), rest])
        return tables

    # ------ support ---------------------------------------------

    def interpret_base(self, obase, omanuf):
        plant = other = ''
        if '/' in obase:
            obase, other = obase.split('/', 1)
            other = ' / ' + other
        nbase = obase
        for plant_re in self.manu_change:
            m = plant_re.search(obase)
            if m:
                plant = obase[m.start():m.end()].strip()
                nbase = self.transform_cell(plant_re.sub(' ', obase, 1).strip())
                #self.debug('IB', plant_re.pattern, obase[m.start():m.end()])
                break
        if omanuf:
            plant = ', '.join([omanuf, plant]) if plant else omanuf
        return nbase + other, plant

    def debug(self, *arg, **kwargs):
        if self.verbose:
            useful.write_comment(*arg, **kwargs)

    # ------ api -------------------------------------------------

    # 1. prep_change
    # 2. base_change
    # 3. interpret_base
    # 4. clmn_change
    # 5. strip column name from value
    # 6. post_change
    # 7. last_change
    def row_column_change(self, file_id, row):
        #self.debug('RCC 1', row['var'], row)
        self.row_change(row, self.prep_change.get(file_id, []) + self.prep_change.get('', []))

        #self.debug('RCC 2', row)
        row['imported_from'] = file_id
        for hdr, nhdr in self.base_change.get(file_id, []):
            row[nhdr[0]] = row[hdr[0]]
            del row[hdr[0]]

        #self.debug('RCC 3', row)
        row['base'], row['manufacture'] = self.interpret_base(row.get('base', ''), row.get('manufacture'))
        if 'base_insert' in row and not row['manufacture']:
            row['base_insert'], row['manufacture'] = self.interpret_base(row.get('base_insert', ''), row.get('manufacture'))

        #self.debug('RCC 4', row)
        for hdrs, nhdrs in self.clmn_change.get('', []) + self.clmn_change.get(file_id, []):
            #self.debug('RCC 4a', hdrs, nhdrs)
            if len(hdrs) > 1:  # N to 1 join
                #self.debug('RCC 4b')
                nvals = list()
                for hdr in hdrs:
                    #self.debug('RCC 4c', hdr, row.get(hdr))
                    if hdr in row and row[hdr] != 'no' and row[hdr] not in nvals:
                        nvals.append(row[hdr])
                row[nhdrs[0]] = ', '.join(nvals) if nvals else 'no'
            elif len(nhdrs) > 1:  # 1 to N split
                hdr = hdrs[0]
                if hdr not in row:
                    #self.debug('RCC 4d')
                    continue
                if hdr in self.column_split_delim:
                    #self.debug('RCC 4e', nonl=True)
                    flds = row[hdr].rsplit(self.column_split_delim[hdr], len(nhdrs) - 1)
                    if len(flds) < len(nhdrs):
                        flds.append('')
                else:
                    #self.debug('RCC 4f', nonl=True)
                    flds = row[hdr].split('/', len(nhdrs) - 1)
                #self.debug(flds)
                if len(flds) == len(nhdrs):
                    row[hdr] = ''
                    for nhdr in nhdrs:
                        #self.debug('RCC 4g', nhdr, ':', row.get(nhdr), nonl=True)
                        row[nhdr] = (row.get(nhdr, '') + ' ' + flds.pop(0).strip()).strip()
                        #self.debug('to', row[nhdr], 'nhdr', nhdr)
                else:
                    #self.debug('RCC 4h')
                    for nhdr in nhdrs:
                        row[nhdr] = row[hdr]
            else:  # 1 to 1 with +
                if hdrs[0] not in row:
                    #self.debug('RCC 4i')
                    continue
                nhdr = nhdrs[0]
                #self.debug('RCC 4j', nhdr, nonl=True)
                fldadd = ''
                if '+' in nhdr:
                    nhdr, fldadd = nhdr.split('+', 1)
                #self.debug(':', row.get(nhdr), nonl=True)
                row[nhdr] = row[hdrs[0]].strip() + fldadd
                row[hdrs[0]] = ''
                #self.debug('to', row[nhdr], 'nhdr', nhdr)

        #self.debug('RCC 5', row)
        for key in row:
            if row[key].endswith(' ' + key.replace('_', ' ')):
                row[key] = row[key][:-len(key)].strip()

        #self.debug('RCC 6', row)
        self.row_change(row, self.post_change.get(file_id, []) + self.post_change.get('', []))

        #self.debug('RCC 7', row)
        for hdr in row:
            for pp in self.last_change:
                row[hdr] = pp[0].sub(pp[1], row[hdr])

        #self.debug('RCC X', row)
        row['is_valid'] = True
        return row

    def row_change(self, row, changes):
        for hdr, pat, repl in changes:
            if hdr in row:
                row[hdr] = (row[hdr].replace(pat, repl) if isinstance(pat, str) else pat.sub(repl, row[hdr])).strip()

    def header_column_change(self, file_id, hdrs):
        #self.debug('HCC0', self.clmn_change.get(file_id, []))
        #self.debug('HCC1', hdrs)
        nhdrs = list()
        for hdr in hdrs:
            #self.debug('HCC3', hdr)
            for ocolname, ncolname in self.base_change.get(file_id, []):
                if hdr == ocolname[0]:
                    hdr = ncolname[0]
                    break
            #self.debug('HCC4', hdr)
            found = False
            for ent in self.clmn_change.get('', []) + self.clmn_change.get(file_id, []):
                #self.debug('HCC5', hdr, ent)
                if len(ent[0]) == 1:  # 1 to 1 or 1 to N split
                    #self.debug('HCC6')
                    if not hdr == ent[0][0]:
                        continue
                    found = True
                    hdr = ent[0][0]
                    newhdrs = ent[1]
                    for nhdr in newhdrs:
                        if nhdr.find('+') >= 0:
                            nhdr = nhdr[:nhdr.find('+')]
                        if nhdr not in nhdrs:
                            nhdrs.append(nhdr)
                else:
                    #self.debug('HCC7')
                    if hdr == ent[0][0]:
                        nhdrs.append(ent[1][0])
                        found = True
                    elif hdr in ent[0][1:]:
                        found = True
            if not found and hdr not in nhdrs:
                #self.debug('HCC8', hdr)
                nhdrs.append(hdr)
        if 'manufacture' not in nhdrs:
            nhdrs.append('manufacture')
        #self.debug('HCC9', nhdrs)
        return nhdrs

    def transform_row(self, row):
        row = [self.transform_cell(x) for x in row]
        return row

    def transform_cell(self, txt):
        txt = reduce(lambda y, x: x[0].sub(x[1], y), self.cell_change, txt)
        return txt.strip()

    def transform_header(self, txt):
        txt = txt.replace('\xa0', ' ').strip()
        txt = reduce(lambda y, x: x[0].sub(x[1], y), self.head_change, txt)
        return txt

    def get_model_ids(self, omn):
        mn = omn
        for transfrom, transto in self.fnam_change:
            if transfrom == omn:
                return transto
            elif not isinstance(transfrom, str):  # re
                fnl_m = transfrom.match(omn)
                if fnl_m:
                    if transto:
                        transto = [transto[0] % fnl_m.group('n')]
                    return transto
        return [mn]

    def show_settings(self, sets, cols):
        if sets:
            print '<table border=1 width=100%>'
            for row in sets:
                print '<tr>'
                for col in row:
                    if isinstance(col, list):
                        print '<td>%s</td>' % '; '.join(col)
                    elif isinstance(col, str):
                        print '<td>%s</td>' % col
                    else:
                        print '<td>%s</td>' % col.pattern
                print '</tr>'
            print '</table>'

    def show_file_settings(self, fn):
        print '<table border=1 width=100%><tr><th width=33%>Bases</th><th width=33%>Columns</th><th width=33%>Cells</th></tr>'
        print '<tr><td valign=top>'
        self.show_settings(self.base_change.get(fn), 2)
        print '</td><td valign=top>'
        self.show_settings(self.clmn_change.get(fn), 2)
        print '</td><td valign=top>'
        self.show_settings(self.prep_change.get(fn), 3)
        print '</td><td valign=top>'
        self.show_settings(self.post_change.get(fn), 3)
        print '</td></tr>'
        print '</table>'


# ------ whew ------------------------------------------------


@basics.command_line
def commands(pif):
    vid = VariationImportData()
    print vid.transform_header("base no.")


if __name__ == '__main__':  # pragma: no cover
    commands('vars')
