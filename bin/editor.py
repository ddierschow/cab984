#!/usr/local/bin/python

import copy, os, urllib2
import basics
import mbdata
import useful


# ------- editor ---------------------------------------------------

#- presentation

def Start(pif):
    if pif.FormBool('clear'):
        pif.dbh.ClearHealth()

    errs = pif.dbh.FetchPages("health!=0")
    if errs:
        print '<hr>'
        print "<b>Errors found:<br><ul>"
        for err in errs:
            print "<li>", err['page_info.id']
        print "</ul>"
        print pif.render.FormatButton('clear', '?clear=1')

    table_list = []
    for table in pif.dbh.table_info:
        if 'ask' in pif.dbh.table_info[table]:
            table_list.append(table)
    table_list.sort()
    for table in table_list:
        print '<hr>'
        print '<b>' + table + '</b>'
        Ask(pif, pif.dbh.GetTableInfo(table))


def Ask(pif, table_info):
    print "<form>"
    print '<input type="hidden" name="table" value="%s">' % table_info['name']
    print pif.render.FormatTableStart()
    for ent in table_info['ask']:
        print pif.render.FormatRowStart()
        print pif.render.FormatCell(0, ent)
        print pif.render.FormatCell(1, '<input type="text" name="%s">' % ent)
        print pif.render.FormatRowEnd()
    print pif.render.FormatTableEnd()
    print pif.render.FormatButtonInput("submit")
    print pif.render.FormatButtonInput('add')
    print "</form>"


# primary entry

@basics.WebPage
def EditorMain(pif):
    pif.render.PrintHtml()
    print pif.form, '<br>'
    pif.Restrict('a')
    print pif.render.FormatHead(extra=pif.render.reset_button_js)
    ShowTable(pif)
    print pif.render.FormatTail()


def ShowTable(pif):
    if not pif.FormStr('table'):
        Start(pif)
        return
    table_info = pif.dbh.GetTableInfo(pif.FormStr('table'))
    print '<b>', table_info['name'], '</b>'
    print pif.render.FormatButton('show all', "?table=" + table_info['name'])
    print pif.form, '<br>'
    # DOES ANYBODY KNOW WHAT THE HELL I WAS THINKING HERE?
#    if len(pif.form) == 1 and table_info.get('ask'):
#       Ask(pif, table_info)
#       return

    if pif.FormHas('save'):
        pif.dbh.Write(table_info['name'], {x: pif.FormStr(x) for x in table_info['columns']}, pif.FormWhere(table_info['id'], 'o_'), modonly=True, tag='ShowTableSave')
        #del pif.FormDel('id')
        print '<br>record saved<br>'
    elif pif.FormHas('delete'):
        pif.dbh.Delete(table_info['name'], pif.FormWhere(table_info['id'], 'o_'))
        pif.FormDel('id')
        print '<br>record deleted<br>'
    elif pif.FormHas('add'):
        print '<br>add', table_info.get('name', 'unset'), '<br>'
        print table_info, '<br>'
        adds = table_info.get('add', {})
        creat = table_info.get('create', {})
        cond = {}
        for id in creat:
            pif.FormDef(id, creat[id])
            cond[id] = pif.FormStr(id)
        print 'cond', cond, '<br>'
        print 'Write', table_info['name'], cond
        lid = pif.dbh.Write(table_info['name'], cond, newonly=True, tag='ShowTableAdd', verbose=1)
        if lid > 0:
            pif.FormSet('id', lid)
        print 'lid', lid, '<br>'
        print '<br>record added<br>'
    elif pif.FormHas('clone'):
        pif.dbh.Write(table_info['name'], {x: pif.FormStr(x) for x in table_info['columns']}, pif.FormWhere(table_info['id'], 'o_'), newonly=True, tag='ShowTableClone')
        #del pif.FormDel('id')
        print '<br>record cloned<br>'
    where = pif.FormWhere(table_info['columns'])
    dats = pif.dbh.Fetch(table_info['name'], where=where, tag='ShowTable')
    if pif.FormHas('order'):
        dats.sort(key=lambda x: x[pif.FormStr('order')])
    if len(dats) > 1:
        print len(dats), 'records'
        ShowMulti(pif, table_info, dats, showsubs=True)
        if table_info['name'] in table_info.get('add', {}):
            cond = {'add': '1'}
            print pif.render.FormatButton('add', "?table=" + table_info['name'] + "&" + "&".join([x + '=' + cond[x] for x in cond]))
    elif len(dats) == 1:
        ShowSingle(pif, table_info, dats[0])
    else:
        ShowNone(pif, table_info, {x: pif.FormStr(x) for x in table_info['columns']})
    return
    args = ''
    for col in table_info['columns']:
        if pif.FormHas(col):
            args += '&' + pif.FormReformat([col])
    print '<a href="?table=' + table_info['name'] + '&add=1' + args + '">' + pif.render.FormatButton('add') + '</a>'


def ShowMulti(pif, table_info, dats, cols=None, showsubs=False):
    print '%s entries' % len(dats)
    if not cols:
        cols = table_info['columns']
    if pif.FormHas('order'):
        sort_ord = pif.FormStr('order')
        dats.sort(key=lambda x: x[sort_ord])
    print pif.render.FormatTableStart()
    print pif.render.FormatRowStart()
    for col in cols:
        if col not in table_info.get('hidden', []):
            print pif.render.FormatCell(0, col)
    print pif.render.FormatRowEnd()
    for dat in dats:
        dat = pif.dbh.DePref(table_info['name'], dat)
        print pif.render.FormatRowStart()
        for col in cols:
            if col in table_info.get('hidden', []):
                pass
            if col in table_info.get('clinks', {}):
                cond = []
                for id in table_info['clinks'][col]['id']:
                    fr, to = id.split('/')
                    cond.append(fr + "=" + str(dat[to]))
                print pif.render.FormatCell(1, '<a href="?table=%s&%s">%s</a><br>' % (table_info['clinks'][col]['tab'], '&'.join(cond), str(dat[col])))
            else:
                print pif.render.FormatCell(1, str(dat.get(col, '')))
        print pif.render.FormatRowEnd()
    print pif.render.FormatTableEnd()

    if showsubs:
        for subtab in table_info.get('tlinks', []):
            if not eval(subtab.get('if', '1')):
                continue
            print "<hr>", subtab['tab']
            print pif.render.FormatButton('show', "?table=" + subtab['tab'])

    print '<hr>'


def ShowSingle(pif, table_info, dat):
    dat = pif.dbh.DePref(table_info['name'], dat)
    dats = [dat]
    adds = table_info.get('add', {})
    print '<form>'
    print '<input type="hidden" name="verbose" value="1">'
    print '<input type="hidden" name="table" value="%s">' % table_info['name']
    for f in table_info['id']:
        print '<input type="hidden" name="o_%s" value="%s">' % (f, dat[f])
    descs = pif.dbh.DescribeDict(table_info['name'])
    print pif.render.FormatTableStart()
    for col in table_info['columns']:
        print pif.render.FormatRowStart()
        also = {}
        if col in table_info['id']:
            also = {'class': 'id'}
        print pif.render.FormatCell(0, col, also=also)
        coltype = descs.get(col).get('type')
        print pif.render.FormatCell(0, coltype, also=also)
        if col in table_info.get('clinks', {}):
            cond = {'table': table_info['clinks'][col]['tab']}
            for id in table_info['clinks'][col]['id']:
                fr, to = id.split('/')
                cond[fr] = str(dat[to])
            #print pif.render.FormatCell(1, '<a href="?table=%s&%s">%s</a><br>' % (table_info['clinks'][col]['tab'], '&'.join(cond), dat[col]), also=also)
            print pif.render.FormatCell(1, pif.render.FormatLink('', str(dat[col]), cond, also=also))
        else:
            print pif.render.FormatCell(1, str(dat[col]), also=also)
        if col in table_info.get('readonly', []):
            print pif.render.FormatCell(1, '&nbsp;<input type=hidden name="%s" value="%s">' % (col, dat[col]), also=also)
        elif coltype.startswith('varchar('):
            colwidth = int(coltype[8:-1])
            print pif.render.FormatCell(1, pif.render.FormatTextInput(col, colwidth, colwidth, value=dat[col]), also=also)
        elif coltype.startswith('char('):
            colwidth = 1
            print pif.render.FormatCell(1, pif.render.FormatTextInput(col, colwidth, colwidth, value=dat[col]), also=also)
        elif coltype.startswith('tinyint('):
            if dat[col] is None:
                dat[col] = 0
            colwidth = int(coltype[8:-1])
            val = dat[col]
            if isinstance(val, str) and val.isdigit():
                val = str(int(val))
            elif not val:
                val = '0'
            print pif.render.FormatCell(1, pif.render.FormatTextInput(col, colwidth, colwidth, value=val), also=also)
        elif coltype.startswith('int('):
            if dat[col] is None:
                dat[col] = 0
            colwidth = int(coltype[4:-1])
            val = dat[col]
            if isinstance(val, str) and val.isdigit():
                val = int(val)
            elif not val:
                val = 0
            print pif.render.FormatCell(1, pif.render.FormatTextInput(col, colwidth, colwidth, value=str(val)), also=also)
        else:
            print pif.render.FormatCell(1, coltype, also=also)
        print pif.render.FormatRowEnd()
    print pif.render.FormatTableEnd()
    print pif.render.FormatButtonInput("save")
    print pif.render.FormatButtonInput("delete")
    if table_info['name'] in adds:
        cond = dict()
        cond['add'] = '1'
        for id in adds[table_info['name']]:
            fr, to = id.split('/')
            cond[fr] = dat[to]
        print pif.render.FormatButton('add', "?table=" + table_info['name'] + "&" + "&".join([x + '=' + cond[x] for x in cond]))
        del adds[table_info['name']]
        print pif.render.FormatButtonInput('clone')
    print '</form>'
    for elink in table_info.get('elinks', []):
        print pif.render.FormatLink((elink['url'] % dat).lower(), elink['name']) + '<br>'

    print '<h3>Subtables</h3>'
    for subtab in table_info.get('tlinks', []):
        if not eval(subtab.get('if', '1')):
            continue
        #print "<hr>"
        print subtab['tab']

        if subtab['tab'] in adds:
            cond = dict()
            cond['add'] = '1'
            for id in adds[subtab['tab']]:
                fr, to = id.split('/')
                cond[fr] = dat[to]
            print pif.render.FormatButton('add', "?table=" + subtab['tab'] + "&" + "&".join([x + '=' + str(cond[x]) for x in cond]))
            del adds[subtab['tab']]

        cond = dict()
        if 'id' in subtab:
            for id in subtab['id']:
                fr, to = id.split('/')
                if to[0] == '*':
                    cond[fr] = eval(to[1:])
                else:
                    cond[fr] = dat[to]
            print pif.render.FormatButton('show', "?table=" + subtab['tab'] + "&" + "&".join([x + '=' + str(cond[x]) for x in cond]))
            ShowSubTable(pif, pif.dbh.GetTableInfo(subtab['tab']), cond, ref=subtab.get('ref', {}))
        else:
            print pif.render.FormatButton('show', "?table=" + subtab['tab'])
#       if subtab['tab'] in adds:
#           print pif.render.FormatButton('add', "?table=" + subtab['tab'] + "&" + "&".join([x + '=' + str(cond[x]) forx in cond]))

    print '<hr>'


def ShowNone(pif, table_info, dat):
    dats = []
    print "No records found.<br>"
    adds = table_info.get('add', {})
    if table_info['name'] in adds:
        cond = {'add': '1'}
        for id in adds[table_info['name']]:
            fr, to = id.split('/')
            cond[fr] = dat.get(to, '')
        print pif.render.FormatButton('add', "?table=" + table_info['name'] + "&" + "&".join([x + '=' + cond[x] for x in cond]))
        del adds[table_info['name']]
    for subtab in table_info.get('tlinks', []):
        if not eval(subtab.get('if', '1')):
            continue
        print "<hr>", subtab['tab']
        if subtab['tab'] in adds:
            print pif.render.FormatButton('add', "?table=" + subtab['tab'] + "&" + "&".join([x + '=' + str(cond[x]) for x in cond]))
        cond = {}
        if 'id' in subtab:
            for id in subtab['id']:
                fr, to = id.split('/')
                if to[0] == '*':
                    cond[fr] = eval(to[1:])
                else:
                    cond[fr] = dat.get(to, '')
            print pif.render.FormatButton('show', "?table=" + subtab['tab'] + "&" + "&".join([x + '=' + str(cond[x]) for x in cond]))
            ShowSubTable(pif, pif.dbh.GetTableInfo(subtab['tab']), cond, ref=subtab.get('ref', {}))
        else:
            print pif.render.FormatButton('show', "?table=" + subtab['tab'])
        if subtab['tab'] in adds:
            cond = {'add': '1'}
            for id in adds[subtab['tab']]:
                fr, to = id.split('/')
                cond[fr] = dat.get(to, '')
            del adds[subtab['tab']]



def ShowSubTable(pif, table_info, cond, ref={}):
    # need to make this handle subtab['ref']
    #{'tab': 'detail', 'id': ['mod_id/mod_id', 'var_id/var'], 'ref': {'attr_id': ['attribute', 'id', 'attribute_name']}},
    # so in this case: ref = {'attr_id': ['attribute', 'id', 'attribute_name']}
    tname = table_info['name']
    if ref:
        cols = [table_info['name'] + '.' + x for x in table_info['columns']]
        lcond = {}
        for key in ref:
            lcond[key] = ref[key][0] + '.' + ref[key][1]
            cols.append(ref[key][0] + '.' + ref[key][2])
            tname += ',' + ref[key][0]  # this will break if we do two columns
        where = " and ".join([table_info['name'] + '.' + x + "='" + cond[x] + "'" for x in cond])
        if lcond:
            where += " and " + " and ".join([table_info['name'] + '.' + x + "=" + lcond[x] for x in lcond])
    else:
        cols = table_info['columns']
        where = " and ".join([table_info['name'] + '.' + x + "='" + str(cond[x]) + "'" for x in cond])
    dats = pif.dbh.Fetch(tname, columns=cols, where=where, tag='ShowSubTable')
    ShowMulti(pif, table_info, dats, cols)

# ------- mass -----------------------------------------------------

@basics.WebPage
def MassMain(pif):
    if pif.FormStr('type') == 'lineup':
        AddLineupMain(pif)
    else:
        pif.render.PrintHtml()
        pif.Restrict('a')
        print pif.render.FormatHead(extra=pif.render.reset_button_js)
        if pif.FormHas('save'):
            MassSave(pif)
        elif pif.FormHas('select'):
            MassSelect(pif)
        else:
            MassAsk(pif)
        print pif.render.FormatTail()

def MassAsk(pif):
    print '<form method="post">'
    print pif.render.FormatTableStart()

    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, "select")
    print pif.render.FormatCell(1, pif.render.FormatTextInput("select", 256, 80))
    print pif.render.FormatRowEnd()

    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, "from")
    print pif.render.FormatCell(1, pif.render.FormatTextInput("from", 256, 80))
    print pif.render.FormatRowEnd()

    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, "where")
    print pif.render.FormatCell(1, pif.render.FormatTextInput("where", 256, 80))
    print pif.render.FormatRowEnd()

    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, "order")
    print pif.render.FormatCell(1, pif.render.FormatTextInput("order", 256, 80))
    print pif.render.FormatRowEnd()

    print pif.render.FormatTableEnd()
    print '<input type="hidden" name="verbose" value="1">'
    print pif.render.FormatButtonInput()
    print "</form>"

def MassSelect(pif):
    columns = pif.FormStr('select').split(',')
    table_info = pif.dbh.table_info[pif.FormStr('from')]
    rows = pif.dbh.Fetch(pif.FormStr('from'), columns=columns + table_info['id'], where=pif.FormStr('where'), order=pif.FormStr('order'), tag='MassSelect')
    print '<form method="post">'
    print '<input type="hidden" name="from" value="%s">' % pif.FormStr('from')
    print '<input type="hidden" name="select" value="%s">' % pif.FormStr('select')
    print '<input type="hidden" name="verbose" value="1">'
    print pif.render.FormatTableStart()

    print pif.render.FormatRowStart()
    for col in columns:
        print pif.render.FormatCell(0, col)
    print pif.render.FormatRowEnd()

    for row in rows:
        print pif.render.FormatRowStart()
        for col in columns:
            if col in table_info['id']:
                print pif.render.FormatCell(1, row[col])
            else:
                print pif.render.FormatCell(1,
                    pif.render.FormatTextInput(col + "." + '.'.join([str(row[x]) for x in table_info['id']]),
                    256, 80, row[col]))
        print pif.render.FormatRowEnd()

    print pif.render.FormatTableEnd()
    print pif.render.FormatButtonInput("save")
    print "</form>"

def MassSave(pif):
    columns = pif.FormStr('select').split(',')
    table_info = pif.dbh.table_info[pif.FormStr('from')]

    for key in pif.FormKeys(has='.'):
        col, ids = key.split('.', 1)
        if col in columns:
            wheres = pif.dbh.MakeWhere(dict(zip(table_info['id'], ids.split('.'))))
            #where = " and ".join(["%s='%s'" % x for x in wheres])
            # update table set col=value where condition;
            #query = "update %s set %s='%s' where %s" % (pif.FormStr('from'), col, pif.dbh.escape_string(pif.FormStr(key)), where)
            #print query, '<br>'
            #pif.dbh.RawExecute(query, tag='MassSave')
            # note: untested
            # note: Write might already escape values
            pif.dbh.Write(pif.FormStr('from'), values={col: pif.dbh.escape_string(pif.FormStr(key))}, where=wheres, modonly=True, tag='MassSave')

# ------- add lineup -----------------------------------------------

# TODO add base_id/casting_id for new castings
def AddLineupMain(pif):
    pif.render.PrintHtml()
    pif.Restrict('a')
    print pif.render.FormatHead(extra=pif.render.reset_button_js)
    if pif.FormHas('save'):
        AddLineupFinal(pif)
    elif pif.FormHas('num'):
        AddLineupList(pif)
    else:
        print "<form>"
        print "Number of models:"
        print pif.render.FormatTextInput("num", 8, 8, value='')
        print '<br>Year:'
        print pif.render.FormatTextInput("year", 4, 4, value='')
        print '<br>Region:'
        print pif.render.FormatTextInput("region", 4, 4, value='')
        print '<br>Model List:'
        print pif.render.FormatTextInput("models", 80, 80, value='')
        print pif.render.FormatButtonInput()
        print pif.render.FormatHiddenInput({'type': 'lineup'})
        print "</form>"
    print pif.render.FormatTail()

def AddLineupFinal(pif):
    pif.dbh.dbi.insert_or_update('page_info',
    {
        'id'          : pif.FormStr('page_id'),
        'flags'       : 0,
        'health'      : '',
        'format_type' : '',
        'title'       : '',
        'pic_dir'     : pif.FormStr('picdir'),
        'tail'        : '',
        'description' : '',
        'note'        : '',
    })
    pif.dbh.dbi.insert_or_update('section',
    {
        'id'            : pif.FormStr('region'),
        'page_id'       : pif.FormStr('page_id'),
        'display_order' : 0,
        'category'      : 'man',
        'flags'         : 0,
        'name'          : pif.FormStr('sec_title'),
        'columns'       : pif.FormInt('cols', 4),
        'start'         : 0,
        'pic_dir'       : '',
        'disp_format'   : '%d.',
        'link_format'   : pif.FormStr('link_fmt'),
        'img_format'    : '',
        'note'          : '',
    })

    for key in pif.FormKeys(start='mod_id.'):
        num = key[7:]
        pif.dbh.dbi.insert_or_update('lineup_model',
        {
            'mod_id'     : pif.FormStr(key),
            'number'     : num,
            'style_id'   : pif.FormStr('style_id.' + num),
            'picture_id' : '',
            'region'     : pif.FormStr('region'),
            'year'       : pif.FormStr('year'),
            'page_id'    : pif.FormStr('page_id'),
            'name'       : pif.FormStr('name.' + num),
        })


def AddLineupList(pif):
    modlist = urllib2.urlopen(pif.FormStr('models')).read().split('\n')
    castings = {x['base_id.rawname'].replace(';', ' '): x['base_id.id'] for x in pif.dbh.FetchCastingList()}
    num_models = pif.FormInt('num')
    year = pif.FormStr('year')
    region = pif.FormStr('region')
    print '<form method="post" action="mass.cgi">'

    print pif.render.FormatTableStart()
    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, 'Page and Section', hdr=True, also={'colspan': 2})
    print pif.render.FormatRowEnd()
    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, 'Page ID')
    print pif.render.FormatCell(0, pif.render.FormatTextInput("page_id", 20, 20, value='year.%s' % year))
    print pif.render.FormatRowEnd()
    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, 'Picture Directory')
    print pif.render.FormatCell(0, pif.render.FormatTextInput("picdir", 80, 80, value=''))
    print pif.render.FormatRowEnd()
    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, 'Section Title')
    print pif.render.FormatCell(0, pif.render.FormatTextInput("sec_title", 80, 80, value='Matchbox %s %s Lineup' % (year, mbdata.regions[region])))
    print pif.render.FormatRowEnd()
    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, 'Link Format')
    print pif.render.FormatCell(0, pif.render.FormatTextInput("link_fmt", 20, 20, value='%s%s%%03d' % (year[2:], region.lower())))
    print pif.render.FormatRowEnd()
    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, 'Columns')
    print pif.render.FormatCell(0, pif.render.FormatTextInput("cols", 1, 1, value=''))
    print pif.render.FormatRowEnd()
    print pif.render.FormatTableEnd()

    print pif.render.FormatTableStart()
    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, 'Models', hdr=True, also={'colspan': 4})
    print pif.render.FormatRowEnd()
    print pif.render.FormatRowStart()
    print pif.render.FormatCell(0, 'Number')
    print pif.render.FormatCell(0, 'Model ID')
    print pif.render.FormatCell(0, 'Style ID')
    print pif.render.FormatCell(0, 'Name')
    print pif.render.FormatRowEnd()
    for cnt in range(0, num_models):
        print pif.render.FormatRowStart()
        print pif.render.FormatCell(0, "%s" % (cnt + 1))
        name = modlist.pop(0)
        print pif.render.FormatCell(0, pif.render.FormatTextInput("mod_id.%d" % (cnt + 1), 12, 12, value=castings.get(name, '')))
        print pif.render.FormatCell(0, pif.render.FormatTextInput("style_id.%d" % (cnt + 1), 3, 3, value='0'))
        print pif.render.FormatCell(0, pif.render.FormatTextInput("name.%d" % (cnt + 1), 64, 64, value=name))
        print pif.render.FormatRowEnd()
    print pif.render.FormatTableEnd()

    print pif.render.FormatButtonInput('save')
    print pif.render.FormatHiddenInput({'type': 'lineup', 'num': num_models})
    print pif.render.FormatHiddenInput({"year": year})
    print pif.render.FormatHiddenInput({"region": region})
    print "</form>"

# ------- roam -----------------------------------------------------

def RoamSelectTable(pif):
    tnames = [''] + pif.dbh.table_info.keys()
    tnames.sort()
    print "<form>"
    print "Table:"
    print pif.render.FormatSelect("table", zip(tnames, tnames))
    print pif.render.FormatButtonInput()
    print "</form>"


def RoamShowTable(pif, table):
    clinks = pif.dbh.table_info[table].get('clinks', {})
    tlinks = pif.dbh.table_info[table].get('tlinks', [])
    where = ''
    cols = pif.dbh.table_info[table]['columns']
    wheres = []
    for col in cols:
        if pif.FormHas(col):
            wheres.append(pif.FormReformat(col))
    dats = pif.dbh.Fetch(table, where=" and ".join(wheres), tag='Roam')

    if len(dats) > 1:
        RoamShowMulti(pif, cols, dats, clinks, tlinks)
    elif len(dats) == 1:
        RoamShowSingle(pif, cols, dats[0], clinks, tlinks)
    else:
        print "No records found."


def RoamShowMulti(pif, cols, dats, clinks, tlinks):
    print pif.render.FormatTableStart()
    print pif.render.FormatRowStart()
    for col in cols:
        print pif.render.FormatCell(0, col)
    for tlink in tlinks:
        print pif.render.FormatCell(0, tlink['tab'])
    print pif.render.FormatRowEnd()
    for dat in dats:
        print pif.render.FormatRowStart()
        for col in cols:
            if col in clinks:
                cond = []
                for id in clinks[col]['id']:
                    fr, to = id.split('/')
                    cond.append(fr + "=" + str(dat[to]))
                print pif.render.FormatCell(1, '<a href="roam.cgi?table=%s&%s">%s</a><br>' % (clinks[col]['tab'], '&'.join(cond), dat[col]))
            else:
                print pif.render.FormatCell(1, dat[col])
        for tlink in tlinks:
            cond = []
            for id in tlink['id']:
                fr, to = id.split('/')
                cond.append(fr + "=" + dat[to])
            print pif.render.FormatCell(1, '<a href="roam.cgi?table=%s&%s">%s</a><br>' % (tlink['tab'], '&'.join(cond), tlink['tab']))
        print pif.render.FormatRowEnd()
    print pif.render.FormatTableEnd()


def RoamShowSingle(pif, cols, dat, clinks, tlinks):
    print pif.render.FormatTableStart()
    for col in cols:
        print pif.render.FormatRowStart()
        print pif.render.FormatCell(0, col)
        if col in clinks:
            cond = []
            for id in clinks[col]['id']:
                fr, to = id.split('/')
                cond.append(fr + "=" + dat[to])
            print pif.render.FormatCell(1, '<a href="roam.cgi?table=%s&%s">%s</a><br>' % (clinks[col]['tab'], '&'.join(cond), dat[col]))
        else:
            print pif.render.FormatCell(1, dat[col])
        print pif.render.FormatRowEnd()
    print pif.render.FormatTableEnd()

    print '<p>'
    for tlink in tlinks:
        cond = []
        for id in tlink['id']:
            fr, to = id.split('/')
            cond.append(fr + "=" + dat[to])
        print '<a href="roam.cgi?table=%s&%s">%s</a><br>' % (tlink['tab'], '&'.join(cond), tlink['tab'])


@basics.WebPage
def RoamMain(pif):
    os.environ['PATH'] += ':/usr/local/bin'
    pif.render.PrintHtml()
    pif.Restrict('a')
    table = pif.FormStr('table', 'tables')
    pif.render.title = table

    print pif.render.FormatHead()
    if pif.FormHas('table'):
        editor.RoamShowTable(pif, table)
    else:
        editor.RoamSelectTable(pif)
    print pif.render.FormatTail()

# ------- counters -------------------------------------------------

@basics.WebPage
def ShowCounters(pif):
    pif.render.PrintHtml()
    pif.Restrict('a')
    print pif.render.FormatHead(extra=pif.render.reset_button_js)
    columns = ['ID', 'Value', 'Timestamp']
    res = pif.dbh.FetchCounters()
    sortorder = pif.FormStr('s', 'id')
    revorder = pif.FormInt('r')
    res.sort(key=lambda x: x['counter.' + sortorder.lower()])
    if revorder:
        res.reverse()
    print pif.render.FormatTableStart()
    print pif.render.FormatRowStart()
    for col in columns:
        if col == sortorder and not revorder:
            print pif.render.FormatCell(0, pif.render.FormatLink('?s=' + col + '&r=1', col), hdr=True)
        else:
            print pif.render.FormatCell(0, pif.render.FormatLink('?s=' + col, col), hdr=True)
    print pif.render.FormatRowEnd()
    for row in res:
        print pif.render.FormatRowStart()
        for col in columns:
            print pif.render.FormatCell(0, row['counter.' + col.lower()])
        print pif.render.FormatRowEnd()
    print pif.render.FormatTableEnd()
    print pif.render.FormatTail()

# ------- ----------------------------------------------------------

if __name__ == '__main__':  # pragma: no cover
    print '''Content-Type: text/html\n\n<html><body bgcolor="#FFFFFF"><img src="../pics/tested.gif"></body></html>'''
