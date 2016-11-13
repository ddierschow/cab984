#!/usr/local/bin/python

import glob, os, re, sys
import basics
import config
import imglib
import mbdata
import models
import useful

# ---------------------------------------------------------------------

# columns, colspan, rowspan, picsize
# columns and picsize MUST NOT exceed 4!
pack_layouts = {
    '1s': [1, 1, 1, 4],
    '2h': [2, 2, 1, 4],
    '2v': [2, 1, 2, 2],
    '3h': [3, 3, 1, 4],
    '3v': [2, 1, 3, 2],
    '4h': [4, 4, 1, 4],
    '4v': [2, 1, 4, 2],
    '5h': [4, 3, 1, 3],
    '5l': [2, 1, 3, 3],
    '5s': [3, 2, 2, 3],
    '5v': [2, 1, 5, 2],
    '6h': [3, 3, 1, 4],
    '6s': [3, 2, 3, 3],
    '6v': [2, 1, 4, 2],
    '7s': [4, 3, 3, 3],
    '8h': [4, 4, 1, 4],
    '8s': [3, 2, 2, 3],
    '8v': [4, 3, 4, 2],
    '9h': [3, 3, 1, 4],
    'th': [4, 3, 2, 3],
    'tv': [3, 2, 4, 2],
    'wh': [4, 4, 1, 4],
}
pack_pic_size = 'tcmlh'

# ---- page list ------------------------------------------------------

def make_page_list(pif):
    pif.render.set_button_comment(pif)
    pages = pif.dbh.fetch_pages("format_type='packs'")
    pages.sort(key=lambda x: x['page_info.title'])
    lsec = pif.dbh.depref('section', pif.dbh.fetch_sections({'page_id': 'packs'}))
    entries = list()
    lsec[0]['range'] = [{'entry': entries}]
    llineup = {'id': 'main', 'name': '', 'section': lsec}
    for page in pages:
        page = pif.dbh.depref('page_info', page)
        if not (page['flags'] & pif.dbh.FLAG_PAGE_INFO_NOT_RELEASED):
            txt = models.add_icons(pif, page['id'][6:], '', '') + '<center>' + page['title'] + '</center>'
            entries.append({'text': pif.render.format_link('?page=' + page['id'][page['id'].find('.') + 1:], txt)})
    pif.render.format_matrix_for_template(llineup)
    return pif.render.format_template('packpages.html', llineup=llineup)

# ---- pack list ------------------------------------------------------

def make_pack_list(pif, sec='', year='', region='', lid='', verbose=False):
    pif.render.set_button_comment(pif)
    years = set()
    regions = set()
    has_note = False
    title = pif.form.search('title')

    sections = pif.dbh.depref('section', pif.dbh.fetch_sections({'page_id': pif.page_id}))
    packs = pif.dbh.depref(['base_id', 'pack'], pif.dbh.fetch_packs(page_id=pif.page_id))
    cols = ['name', 'year', 'product_code']
    heads = ['Name', 'Year', 'Product Code']
    if verbose:
	cols = ['edlink'] + cols + ['region', 'country', 'layout', 'thumb', 'pic', 'material', 'stars', 'rel']
	heads = ['Pack ID'] + heads + ['Rg', 'Cy', 'Ly', 'Th', 'Pic', 'Mat', 'Models', 'Related']
    else:
	cols += ['regionname']
	heads += ['Region']
    cols += ['note']
    heads += ['Note']
    heads = dict(zip(cols, heads))

    llineup = dict(section=[])
    for lsection in sections:
	entries = list()
	for pack in packs:
	    if pack['section_id'] == lsection['id']:
		years.add(pack['first_year'])
		regions.add(pack['region'])
		pack['name'] = pack['rawname'].replace(';', ' ')
		if (year and (year < pack['first_year'] or year > pack['end_year'])) or \
			 (region and region != pack['region']) or (lid and not pack['id'].startswith(lid)) or \
			 not useful.search_match(title, pack['name']):
		    continue
		relateds = []  #pif.dbh.fetch_packs_related(pack['id'])
		pack['rel'] = ' '.join(sorted([x['pack.id'] for x in relateds]))
		pack['year'] = (pack['first_year'] + '-' + pack['end_year']) if (pack['end_year'] and pack['end_year'] != pack['first_year']) else pack['first_year']

		pack['layout'] = pack['layout'] if pack['layout'] in pack_layouts else '<font color="red">%s</font>' % pack['layout']
		pack['page'] = pif.form.get_str('page')
		pack['regionname'] = mbdata.regions[pack['region']]
		pack['name'] = '<a href="?page=%(page)s&id=%(id)s">%(name)s</a>' % pack
		has_note = has_note or bool(pack['note'])
		if verbose:
		    modify_pack_admin(pif, pack)
		entries.append(pack)
	if not entries:
	    continue
	entries.sort(key=lambda x: (x[pif.form.get_str('order', 'name')], x['name'], x['first_year']))
#	if not has_note:
#	    cols.remove('note')

	lrange = dict(entry=entries, note='')
	lsection['columns'] = cols
	lsection['headers'] = heads
	lsection['range'] = [lrange]
	lsection['note'] = ''
	llineup['section'].append(lsection)
    useful.write_comment(llineup)
    context = {
	'page_id': pif.form.get_str('page'),
	'years': sorted(years),
	'regions': [(x, mbdata.regions[x]) for x in sorted(regions)],
	'llineup': llineup,
	#'lid': calc_pack_select(pif, packs),
    }
    return pif.render.format_template('packlist.html', **context)

def modify_pack_admin(pif, pack):
    pmodels = distill_models(pif, pack, pif.page_id)
    stars = ''
    for mod in sorted(pmodels.keys()):
	if not pmodels[mod].get('id'):
	    stars += pif.render.format_image_art('stargreen.gif') + ' '
	elif not pmodels[mod].get('vs.var_id'):
	    stars += pif.render.format_image_art('starred.gif') + ' '
	elif pmodels[mod]['imgstr'].find('-') < 0:
	    stars += pif.render.format_image_art('stargray.gif') + ' '
	else:
	    stars += pif.render.format_image_art('star.gif') + ' '
    pack['stars'] = stars
    pack['edlink'] = '<a href="mass.cgi?verbose=1&type=pack&section_id=%(section_id)s&pack=%(id)s&num=">%(id)s</a>' % pack
    relateds = []  #pif.dbh.fetch_packs_related(pack['id'])
    pack['rel'] = ' '.join(sorted([x['pack.id'] for x in relateds]))

# ---- single pack ----------------------------------------------------

def do_single_pack(pif, pid):
    pack = dict()
    packs = pif.dbh.fetch_pack(pid)
    if not packs:
	raise useful.SimpleError("That pack doesn't seem to exist.")
    pack = packs[0]
    pif.render.hierarchy_append('', pack['base_id.rawname'])

    pack_id = pack['pack.id']
    relateds = [
	{
	    'link': pif.render.format_link("?page=" + pif.form.get_str('page') + "&id=" + r['pack.id'], r['base_id.rawname']),
	    'product_code': r['pack.product_code'],
	    'region': mbdata.regions.get(r['pack.region'], ''),
	    'country': mbdata.get_country(r['pack.country']),
	    'material': mbdata.materials.get(r['pack.material'], ''),
	    'description': r['base_id.description'],
	}
	for r in pif.dbh.fetch_packs_related(pack_id)
    ]

    tcomments = set()
    pack.update({key[key.find('.') + 1:]: pack[key] for key in pack})
    pack['name'] = pack['rawname'].replace(';', ' ')

    pmodels = distill_models(pif, pack, pif.page_id)
    if pack['layout'].isdigit():
	layout = [int(x) for x in pack['layout']]
    elif not pmodels:
	layout = pack_layouts['1s']
    else:
	layout = pack_layouts.get(pack['layout'], [4, 4, 1, 4])
    if len(layout) == 2:
	layout[3] = 1
    if len(layout) == 3:
	layout[4] = 4 - (layout[0] - layout[1])

    pif.render.comment('pack:', pack)
    entries = [{'text': show_pack(pif, pack, pack_pic_size[layout[3]]), 'display_id': '0', 'colspan': layout[1], 'rowspan': layout[2]}]
    for mod in sorted(pmodels.keys()):
        pif.render.comment("do_single_pack mod", pmodels[mod])

        if not pmodels[mod].get('id'):
            pmodels[mod]['no_casting'] = 1
            tcomments.add('m')
        else:
            if pmodels[mod]['imgstr'].find('-') < 0:
                tcomments.add('i')
            if not pmodels[mod].get('vs.var_id'):
                pmodels[mod]['no_variation'] = 1
                tcomments.add('v')

        entries.append({'text': show_pack_model(pif, pmodels[mod]), 'display_id': 1})

    lsec = dict(id='', columns=layout[0], anchor=pack['id'], range=[{'entry': entries}])
    llineup = dict(section=[lsec], tail=[''], id='')

    # left bar
    left_bar_content = ''
    if pif.is_allowed('a'):  # pragma: no cover
        #left_bar_content += str(pack['page_id']) + '/' + str(pack['id'])
	left_bar_content += '<br><center>'
        left_bar_content += '<p><b><a href="%s">Base ID</a></b><br>\n' % pif.dbh.get_editor_link('base_id', {'id': pack_id})
        left_bar_content += '<b><a href="%s">Pack</a></b><br>\n' % pif.dbh.get_editor_link('pack', {'id': pack_id})
        left_bar_content += '<b><a href="traverse.cgi?d=%s">Library</a></b><br>\n' % config.IMG_DIR_PACK
        left_bar_content += '<b><a href="mass.cgi?verbose=1&type=pack&section_id=%s&pack=%s&num=">Edit</a></b><br>\n' % (pack['section_id'], pack['id'])
        left_bar_content += '<b><a href="imawidget.cgi?d=./%s&f=%s.jpg">Edit Pic</a></b>\n' % (pif.render.pic_dir, pack['id'])
        left_bar_content += '</center>\n'

    pif.render.set_button_comment(pif, 'd=%s' % pif.form.get_str('id'))
    pif.render.format_matrix_for_template(llineup)
    context = {
	'title': pack['name'],
	'note': pack['note'],
	'type_id': pif.page_name,
	'icon_id': '',#pack_id,
	'vehicle_type': '',
	'rowspan': 4,
	'left_bar_content': left_bar_content,
	'llineup': llineup,
	'relateds': relateds,
    }
    return pif.render.format_template('pack.html', **context)


def distill_models(pif, pack, page_id):
    model_list = pif.dbh.fetch_pack_models(pack_id=pack['id'], page_id=page_id)
    pack['pic'] = ''
    #for pic in glob.glob(os.path.join(config.IMG_DIR_PACK, '?_' + pack['id'] + '.jpg')):
    pic = pif.render.find_image_path(pack['id'], pdir=config.IMG_DIR_PACK, largest=mbdata.IMG_SIZ_HUGE)
    pack['pic'] += pif.render.format_image_art(imglib.image_star(pic))
    linmod = pif.dbh.fetch_lineup_model(where="mod_id='%s'" % pack['id'])
    pack['thumb'] = pif.render.format_image_art('box-sm-x.gif' if linmod else 'box-sm.gif')
    if pif.render.find_image_file(pack['id'], pdir=config.IMG_DIR_MAN, prefix=mbdata.IMG_SIZ_SMALL):
        pack['thumb'] += pif.render.format_image_art('starblack.gif')
    pmodels = {}

    for mod in [x for x in model_list if x['pack.id'] == pack['id']]:
        mod = pif.dbh.modify_man_item(mod)
        sub_ids = [None, '', pack['id'], pack['id'] + '.' + str(mod['pack_model.display_order'])]
        if mod['vs.sub_id'] in sub_ids:
            mod['imgl'] = [mbdata.IMG_SIZ_SMALL + '_' + mod['id'], mod['id'], mod['pack_model.mod_id']]
            for s in mod['descs']:
                if s.startswith('same as '):
                    mod['imgl'].extend([mbdata.IMG_SIZ_SMALL + '_' + s[8:], s[8:]])
            if not mod.get('vs.ref_id'):
                mod['vs.ref_id'] = ''
            if not mod.get('vs.sub_id'):
                mod['vs.sub_id'] = ''
            mod['pdir'] = pif.render.pic_dir
	    if mod['pack_model.mod_id'] != 'unknown':
		mod['href'] = "single.cgi?id=%(pack_model.mod_id)s&dir=%(pdir)s&pic=%(pack_model.pack_id)s&ref=%(vs.ref_id)s&sub=%(vs.sub_id)s" % mod
            #'<a href="single.cgi?dir=%(dir)s&pic=%(link)s&ref=%(vs.ref_id)s&id=%(mod_id)s">' % ent
            #'pack_model.pack_id': 'car02',
        #    if mod['pack_model.var'] and mod['imgl']:  # still not perfect
        #       mod['href'] = mod['href'] + '&pic=' + mod['imgl'][mod['imgl'].rfind('/') + 1:-2]
            mod['vars'] = []
            mod['pics'] = []
            if not mod['pack_model.display_order'] in pmodels:
                pmodels[mod['pack_model.display_order']] = mod
            if mod['v.picture_id']:
                pmodels[mod['pack_model.display_order']]['pics'].append(mod['v.picture_id'])
            else:
                pmodels[mod['pack_model.display_order']]['pics'].append(mod['vs.var_id'])
            if mod.get('vs.var_id'):
                pmodels[mod['pack_model.display_order']]['vars'].append(mod['vs.var_id'])
    for dispo in pmodels:
        pmodels[dispo]['imgstr'] = pif.render.format_image_required(pmodels[dispo]['imgl'], pdir=config.IMG_DIR_MAN, prefix=mbdata.IMG_SIZ_SMALL, vars=pmodels[dispo].get('pics'))
    return pmodels


#'columns': ['id', 'page_id', 'section_id', 'name', 'first_year', 'end_year', 'region', 'layout', 'product_code', 'material', 'country'],
def show_pack(pif, pack, picsize):
    ostr = pif.render.format_image_required(pack['id'], largest=picsize)
    if pif.is_allowed('a'):  # pragma: no cover
        ostr = '<a href="upload.cgi?d=./%s&n=%s">%s</a>' % ('lib/prod/packs', pack['id'], ostr)
    else:
        ostr = '<a href="upload.cgi">%s</a>' % (ostr)
    pack['country'] = mbdata.get_country(pack['country'])
    pack['material'] = mbdata.materials.get(pack['material'], '')
    if pack['product_code']:
        ostr += '<br>' + pack['product_code']
    if pack['region']:
        ostr += '<br>' + mbdata.regions[pack['region']]
    ostr += '<p>'
    if pack['first_year']:
	if pack['end_year'] and pack['end_year'] != pack['first_year']:
	    ostr += '<b>%(first_year)s-%(end_year)s</b><br>' % pack
	else:
	    ostr += '<b>%(first_year)s</b><br>' % pack
    dets = filter(None, [pack['country'], pack['material']])
    ostr += ' - '.join(dets)
    return ostr


#mdict: descriptions href imgstr name no_casting not_made number pdir picture_only product subname
#def add_model_table_product_link(pif, mdict):

def show_pack_model(pif, mdict):
    pif.render.comment("show_pack_model", mdict)

    mdict['number'] = ''
    mdict['descriptions'] = []
    if mdict['v.text_description']:
        mdict['descriptions'] = [mdict['v.text_description']]  # fix this
    mdict['product'] = ''
    if mdict['imgstr'].find('-') < 0:
        mdict['no_specific_image'] = 1

    desclist = list()
    for var in mdict.get('descriptions', []):
	if var and var not in desclist:
	    desclist.append(var)
    mdict['descriptions'] = desclist

    if not mdict.get('disp_format') or not mdict.get('shown_id'):
        mdict['displayed_id'] = '&nbsp;'
    else:
        mdict['displayed_id'] = mdict['disp_format'] % (mdict['shown_id'])

    return models.add_model_table_product_link(pif, mdict)


def edit_model(pif, mdict):
    ostr = pif.render.format_row_start()
    ostr += '<input type="hidden" name="pm.id.%s" value="%s">\n' % (mdict['pack_model.id'], mdict['pack_model.id'])
    ostr += '<input type="hidden" name="pm.pack_id.%s" value="%s">\n' % (mdict['pack_model.id'], mdict['pack_model.pack_id'])
    ostr += pif.render.format_cell(0, 'mod ' + pif.render.format_text_input("pm.mod_id.%s" % mdict['pack_model.id'], 8, 8, value=mdict['pack_model.mod_id']))
    ostr += pif.render.format_cell(0, 'var ' + pif.render.format_text_input("pm.var_id.%s" % mdict['pack_model.id'], 20, 20, value='/'.join(mdict['vars'])) + ' (' + str(mdict['pack_model.var_id']) + ')')
    ostr += pif.render.format_cell(0, 'disp ' + pif.render.format_text_input("pm.display_order.%s" % mdict['pack_model.id'], 2, 2, value=mdict['pack_model.display_order']))
    ostr += pif.render.format_row_end()
    return ostr

# ---- main -----------------------------------------------------------

@basics.web_page
def do_page(pif):
    pif.render.print_html()
    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('packs.cgi', 'Multi-Model Packs')
    #pif.form.set_val('id', pif.form.get_list('id')[0])  # with no id this blows
#    if isinstance(pif.form.get('id'), list):
#       pif.form['id'] = pif.form.get_str('id')[0]
    if pif.form.has('id'):
        pif.form.set_val('id', pif.form.get_list('id')[0])  # with no id this blows
	pid = pif.form.get_str('id')
        return do_single_pack(pif, pid)
    elif pif.form.has('page'):
	return make_pack_list(pif,
		    verbose=pif.is_allowed('m') and pif.form.get_int('verbose'),
		    **pif.form.get_dict(['sec', 'year', 'region', 'lid']))
    else:
        return make_page_list(pif)

# ---------------------------------------------------------------------

if __name__ == '__main__':  # pragma: no cover
    basics.goaway()
