#!/usr/local/bin/python

import itertools, os, urllib
import basics
import config
import mbdata
import models
import useful


def create_section(pif, attribute_type):
    def prep_mod(mod):
	mod = pif.dbh.modify_man_item(mod)
	mod['img'] = '/'.join(pif.render.find_image_file(mod['attribute_picture.mod_id'] + '-' + mod['attribute_picture.picture_id'], prefix=attribute_type, pdir=config.IMG_DIR_ADD))
	mod['img'] = pif.render.format_link('/' + mod['img'], txt=mod['attribute_picture.description'])
	return mod
    mods = pif.dbh.fetch_attribute_pictures_by_type(attribute_type, 'attribute_picture.mod_id')
    lsec = pif.dbh.fetch_sections({'page_id': pif.page_id})[0]
    lsec['range'] = [{'entry':
	[{'text': models.add_model_thumb_pic_link(pif, prep_mod(mod))} for mod in mods]}]
    return lsec


def errors(pif):
    pif.render.print_html()
    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('/cgi-bin/errors.cgi', 'Error Models')
    pif.render.set_button_comment(pif)

    lsec = create_section(pif, 'e')

    llineup = {'section': [lsec], 'columns': lsec['columns']}
    pif.render.format_matrix_for_template(llineup)
    return pif.render.format_template('simplematrix.html', llineup=llineup)


def prepro(pif):
    pif.render.print_html()
    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('/cgi-bin/prepro.cgi', 'Prototype and Preproduction Models')
    pif.render.set_button_comment(pif)

    lsec = create_section(pif, 'p')

    llineup = {'section': [lsec]}
    pif.render.format_matrix_for_template(llineup)
    return pif.render.format_template('simplematrix.html', llineup=llineup)


def code2(pif):
    if pif.form.get_str('mod_id'):
	return code2_model(pif)

    def prep_mod(pif, mod, cat):
	mod = pif.dbh.modify_man_item(mod)
	mod['img'] = pif.render.format_link('?mod_id=%s&cat=%s' % (mod['id'], cat), txt='%d Variation%s' % (mod['count(*)'], 's' if mod['count(*)'] != 1 else ''))
	return models.add_model_thumb_pic_link(pif, mod)

    section_id = pif.form.get_str('section')
    pif.render.print_html()
    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('/cgi-bin/code2.cgi', 'Code 2 Models')
    pif.render.set_button_comment(pif)

    llineup = {'section': []}
    for lsec in pif.dbh.fetch_sections({'page_id': pif.page_id}):
	if not section_id or section_id == lsec['id']:
	    if section_id:
		pif.render.hierarchy_append('/cgi-bin/code2.cgi?section=%s' % section_id, lsec['name'])
	    mods = pif.dbh.fetch_castings_by_category(lsec['page_id'], lsec['category'])
	    lsec['range'] = [{'entry': [{'text': prep_mod(pif, mod, lsec['category'])} for mod in mods]}]
	    llineup['section'].append(lsec)

    pif.render.format_matrix_for_template(llineup)
    return pif.render.format_template('simplematrix.html', llineup=llineup)


def code2_model(pif):
    mod_id = pif.form.get_str('mod_id')
    cat_id = pif.form.get_str('cat')
    pif.render.print_html()
    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('/cgi-bin/code2.cgi', 'Code 2 Models')
    pif.render.set_button_comment(pif)

    mod = pif.dbh.modify_man_item(pif.dbh.fetch_casting(mod_id))
    img = pif.render.format_image_required(mod_id, largest=mbdata.IMG_SIZ_MEDIUM, pdir=config.IMG_DIR_MAN)
    header = '<center>%s<br><b>%s: %s</b></center><p>' % (img, mod['id'], mod['name'])
    lsec = pif.dbh.fetch_section(page_id=pif.page_id, category=cat_id)
    if not lsec:
	raise useful.SimpleError('No models found.')
    lsec = lsec.todict()
    pif.render.hierarchy_append('/cgi-bin/code2.cgi?section=%s' % lsec['id'], lsec['name'])
    pif.render.hierarchy_append('/cgi-bin/code2.cgi?mod_id=%s&cat=%s' % (mod['id'], cat_id), mod['id'])
    lsec['range'] = [{'entry': []}]
    mvars = pif.dbh.fetch_variation_by_select(mod_id, pif.page_id, '', category=cat_id)
    for var in mvars:
	useful.write_comment(var)
	entry = {'text': models.add_model_var_pic_link(pif, pif.dbh.depref('v', var))}
	lsec['range'][0]['entry'].append(entry)

    llineup = {
	'section': [lsec],
	'header': header,
    }
    pif.render.format_matrix_for_template(llineup)
    return pif.render.format_template('simplematrix.html', llineup=llineup)


# Brazil, Bulgaria, China, England, Hong Kong, Hungary, Japan, Macau, Thailand, no origin, [blank]
def plants(pif):
    if pif.form.get_str('id'):
	return plant_models(pif)

    def prep_entry(pif, name, code):
	img = pif.render.format_image_art('flag_' + code) if code else pif.render.fmt_no_pic()
	return {'text': pif.render.format_link('?id=%s' % (code if code else 'unset'), img + '<br>' + name)}

    pif.render.print_html()
    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('/cgi-bin/plants.cgi', 'By Manufacturing Plant')
    pif.render.set_button_comment(pif)

    llineup = {'section': [{'columns': 3, 'range': [
	{'id': 'ix', 'entry': [prep_entry(pif, *x) for x in mbdata.plants]}
    ]}]}

    pif.render.format_matrix_for_template(llineup)
    return pif.render.format_template('simplematrix.html', llineup=llineup)


def plant_models(pif):
    plant_id = pif.form.get_str('id')
    if plant_id == 'unset':
	plant_id = ''
    plant_d = dict([(y, x) for x, y in mbdata.plants])
    pif.render.title = plant_name = plant_d.get(plant_id, 'origin not set')
    pif.render.print_html()
    pif.render.set_button_comment(pif)
    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('/cgi-bin/plants.cgi', 'By Manufacturing Plant')
    pif.render.hierarchy_append('/cgi-bin/plants.cgi?id=%s' % plant_id, plant_name)

    entries = []
    mmods = pif.dbh.fetch_castings_by_plant(plant_name if plant_id else '')
    for mmod in mmods:
	mod = pif.dbh.make_man_item(mmod)
	mod['count'] = mmod['count']
	mod['img'] = pif.render.format_link('/cgi-bin/vars.cgi?manufacture=%s&mod=%s' % (plant_d.get(plant_id, 'unset'), mod['id']), txt='%d Variation%s' % (mod.get('count', -1), 's' if mod.get('count', -1) != 1 else ''))
	entries.append({'text': models.add_model_thumb_pic_link(pif, mod)})

    llineup = {
	'section': [{'range': [{'entry': entries}]}],
	'columns': 3,
    }
    pif.render.format_matrix_for_template(llineup)
    return pif.render.format_template('simplematrix.html', llineup=llineup)


def ads(pif):
    pif.render.print_html()
    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('/cgi-bin/ads.cgi', 'Advertisements')
    pif.render.set_button_comment(pif)

    pic_dir = config.IMG_DIR_ADS
    lib_dir = config.LIB_DIR + '/pub/ads'
    ranges = []

    def fmt_cy(ent):
	cy = ent.get('country', '')
	cyflag = pif.render.show_flag(cy) if (cy and cy != 'US') else ''
	cyflag = (' <img src="' + cyflag[1] + '">') if cyflag else ''
	return cy, cyflag

    def fmt_vid(ent):
	#sep = pif.render.format_image_art('wheel.gif', also={'class': 'dlm'})
	# add country
	cy, cyflag = fmt_cy(ent)
	cmt = ent['description']
	ostr = pif.render.format_link(ent['url'], ent['name'])
	if cmt:
	    ostr += ' ' + cmt
	ostr += cyflag
	ostr += (' ' + pif.render.format_link('edlinks.cgi?id=%s' % ent['id'], '<i class="fa fa-edit"></i>')) if pif.is_allowed('ma') else ''
	return ostr

    #id, page_id, section_id, display_order, flags, associated_link, last_status, link_type, country, url, name, description, note
    vlinks = [fmt_vid(x) for x in
	pif.dbh.depref('link_line', pif.dbh.fetch_link_lines(page_id='links.others', section='Lvideoads', order='name'))]

    files = list()

    def fmt_pub(ent, pdir=None):
	pdir = pdir if pdir else pic_dir
	# ent: id, description, country, first_year, model_type
	cy, post = fmt_cy(ent)
	floc = '.' + pdir + '/' + ent['id'] + '.jpg'
	lloc = floc.replace('/pic/', '/lib/')
	url = pdir + '/' + ent['id'] + '.jpg'
	name = useful.printablize(ent['description'])
	if ent.get('first_year'):
	    name += ' (' + ent['first_year'] + ')'
	if pif.is_allowed('ma'):
	    if ent.get('model_type'):
		post += ' ' + pif.render.format_link(pif.dbh.get_editor_link('publication', {'id': ent['id']}), '<i class="fa fa-edit"></i>')
	    else:
		post += ' ' + pif.render.format_link(
'/cgi-bin/mass.cgi?type=ads&id=%s&description=%s&year=%s&country=%s' % (ent['id'], urllib.quote_plus(ent['description']), ent.get('first_year', ''), cy)
, '<i class="fa fa-plus-square-o"></i>'
)
	    if os.path.exists(floc):
		post += ' ' + pif.render.format_link('/cgi-bin/imawidget.cgi?d=.%s&f=%s' % (pdir, ent['id'] + '.jpg'), '<i class="fa fa-paint-brush"></i>')
	    elif os.path.exists(lloc):
		post += ' ' + pif.render.format_link('/cgi-bin/imawidget.cgi?d=.%s&f=%s' % (pdir.replace('pic', 'lib'), ent['id'] + '.jpg'), '<i class="fa fa-paint-brush"></i>')
	    post += ' ' + pif.render.format_link('/cgi-bin/upload.cgi?d=.%s&n=%s' % (lib_dir, ent['id'] + '.jpg'), '<i class="fa fa-upload"></i>')
	    name = ent['id'] + ' - ' + name
	files.append(ent['id'] + '.jpg')
	if os.path.exists(floc):
	    return pif.render.format_link(url, name) + post
	return name + post

    #id, first_year, model_type, rawname, description, flags
    plinks = list()
    missing = []
    links = pif.dbh.fetch_publications(model_type='AD', order='base_id.first_year,base_id.id')
    for ent in pif.dbh.modify_man_items(links):
	if os.path.exists('.' + pic_dir + '/' + ent['id'] + '.jpg'):
	    plinks.append(fmt_pub(ent))
	else:
	    missing.append(fmt_pub(ent))
    ranges.append({'entry': plinks})

    plinks = [fmt_pub(dict(itertools.izip_longest(['id', 'description', 'first_year', 'country', 'model_type'], ent)))
	for ent in [x.strip().split('|') for x in open('.' + pic_dir + '/list.dat').readlines()] if ent[0] + '.jpg' not in files]
    plinks += [fmt_pub({'id': ent[:-4], 'description': ent[:-4]})
	for ent in sorted(set(os.listdir('.' + pic_dir)) - set(files)) if ent.endswith('.jpg')]
    if plinks:
	ranges.append({'name': 'More information is needed on these (year, location).', 'entry': plinks})

    if pif.is_allowed('ma'):
	plinks = [fmt_pub({'id': ent[:-4], 'description': ent[:-4]}, lib_dir)
	    for ent in sorted(os.listdir('.' + lib_dir)) if ent.endswith('.jpg')]
	if plinks:
	    ranges.append({'name': '<i>Nonpublished ads</i>', 'entry': plinks})
	if missing:
	    ranges.append({'name': '<i>Database entries missing pictures</i>', 'entry': missing})

    lsecs = [
	{'id': 'print', 'name': 'Print Advertising', 'range': ranges},
	{'id': 'video', 'name': 'Video Advertising', 'range': [{'entry': vlinks}]},
    ]

    pif.render.set_footer(pif.render.format_button('back', '/') + ' to the index.')
    if pif.is_allowed('ma'):
	pif.render.set_footer(
	    pif.render.format_link('/cgi-bin/upload.cgi?d=.%s' % config.LIB_DIR + '/ads', 'Upload new ad') + ' - ' +
	    pif.render.format_link('/cgi-bin/edlinks.cgi?page_id=links.others&sec=Lvideoads&add=1', 'Add new video')
    )
    llineup = {'section': lsecs}
    return pif.render.format_template('simpleulist.html', llineup=llineup)


def custom_create_section(pif, attribute_type):
    adds = {x[0][0]: x[1] for x in mbdata.model_adds}
    credits = {x['photo_credit.name'][2:]: x['photographer.name'] for x in pif.dbh.fetch_photo_credits(path=config.IMG_DIR_ADD[1:])
		    if x['photo_credit.name'].startswith(attribute_type)}

    def prep_mod(attr_pic):
	mod_id = attr_pic['attribute_picture.mod_id']
	img_id = mod_id.lower() + ('-' + attr_pic['attribute_picture.picture_id'] if attr_pic['attribute_picture.picture_id'] else '')
	add = adds.get(attr_pic['attribute_picture.attr_type'], 'Picture%s')
	img = pif.render.find_image_path(img_id, prefix=attr_pic['attribute_picture.attr_type'], pdir=config.IMG_DIR_ADD)
	caption = attr_pic['attribute_picture.description']
	img_credit = credits.get(img_id, '')
	ostr = ''
	if img:
	    ostr += '<center><h3>%s</h3>\n' % add % {'s': ''}
	    ostr += '<table><tr><td>' + pif.render.fmt_img_src(img) + '<br>'
	    if img_credit:
		ostr += '<div class="credit">Photo credit: %s</div>' % img_credit
	    ostr += '</td></tr></table>'
	    if attr_pic['attribute_picture.description']:
		ostr += attr_pic['attribute_picture.description']
	    ostr += '<p></center>\n'
	return (''' <a onclick="init_modal('m.%s');" class="modalbutton">%s</a>\n''' % (img_id, attr_pic['attribute_picture.description']),
		pif.render.format_modal('m.' + img_id, ostr))

    mods = pif.dbh.fetch_attribute_pictures_by_type(attribute_type, 'attribute_picture.mod_id')
    modd = {}
    modals = []
    for mod in mods:
	mod_id = mod['attribute_picture.mod_id']
	if mod_id not in modd:
	    modd[mod_id] = pif.dbh.modify_man_item(mod)
	    modd[mod_id]['img'] = []
	img, modal = prep_mod(mod)
	modd[mod_id]['img'].append(img)
	modals.append(modal)
    lsec = pif.dbh.fetch_sections({'page_id': pif.page_id})[0]
    lsec['range'] = [{'entry':
	[{'text': models.add_model_thumb_pic_link(pif, mod[1])} for mod in sorted(modd.items())]}]
    lsec['footer'] = '\n'.join(modals)
    return lsec


def custom(pif):
    pif.render.set_page_extra(pif.render.modal_js)
    pif.render.print_html()
    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('/cgi-bin/custom.cgi', 'Customizations')
    pif.render.set_button_comment(pif)

    lsec = custom_create_section(pif, 'a')

    llineup = {'section': [lsec], 'columns': lsec['columns']}
    pif.render.format_matrix_for_template(llineup)
    return pif.render.format_template('simplematrix.html', llineup=llineup)


@basics.web_page
def main(pif):
    if pif.page_id == 'errors':
	return errors(pif)
    if pif.page_id == 'prepro':
	return prepro(pif)
    if pif.page_id == 'code2':
	return code2(pif)
    if pif.page_id == 'plant':
	return plants(pif)
    if pif.page_id == 'ads':
	return ads(pif)
    if pif.page_id == 'custom':
	return custom(pif)

#---- compare -------------------------------

@basics.web_page
def compare_main(pif):
    pif.render.print_html()
    csecs = pif.dbh.fetch_sections({'page_id': pif.page_id})
    llineup = {'section': []}
    for sec in csecs:

	cmods = pif.dbh.fetch_casting_related_compares(section_id=sec['section.id'])
	cmods.sort(key=lambda x: x['c2.first_year'])
	lsec = {'name': sec['section.name'], 'note': sec['section.note'], 'range': []}
	llineup['section'].append(lsec)
        modsets = {}
        for mod in [m for m in cmods if m['cr.section_id'] == sec['section.id']]:
	    mod['name'] = mod['c2.rawname'].replace(';', ' ')
	    mod['model_id'] = mod['cr.related_id']
            modsets.setdefault(mod['cr.model_id'], [])
	    img = pif.render.format_image_optional(mod['cr.model_id'] + ('-%s' % mod['cr.picture_id'] if mod['cr.picture_id'] else ''),
			prefix='z_', nopad=True)
            modsets[mod['cr.model_id']].append((mod['model_id'], mod['name'], mod['cr.description'].split(';'), img))

        for main_id in sorted(modsets.keys()):
            modset = modsets[main_id]
            names = list()
            for id, name, descs, img in modset:
                if name not in names:
                    names.append(name)
	    lran = {'name': ', '.join(names), 'entry': []}
	    lsec['range'].append(lran)
            for id, name, descs, img in modset:
		lent = [models.add_model_pic_link_short(pif, id),
			filter(None, descs), img]
		lran['entry'].append(lent)

    return pif.render.format_template('compare.html', lcompare=llineup)
