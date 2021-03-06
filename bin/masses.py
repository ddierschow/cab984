#!/usr/local/bin/python

import os, re, urllib2, urlparse
import basics
import config
import images
import mbdata
import useful



# ------- mass -----------------------------------------------------


@basics.web_page
def mass(pif):
    pif.render.print_html()
    pif.restrict('am')
    pif.render.set_page_extra(pif.render.reset_button_js + pif.render.toggle_display_js)

#    if not pif.dbh.insert_token(pif.form.get_str('token')):
#	print 'duplicate form submission detected'
#	return

#    print pif.form, '<hr>'
    mass_type = pif.form.get_str('type')
    return dict(mass_mains_list).get(mass_type, mass_mains_hidden.get(mass_type, mass_main))(pif)


def mass_main(pif):
    if pif.duplicate_form: #not pif.dbh.insert_token(pif.form.get_str('token')):
	print 'duplicate form submission detected'
    elif pif.form.has('save'):
	return mass_save(pif)
    elif pif.form.has('select'):
	return mass_select(pif)
    return mass_ask(pif)


def mass_ask(pif):
    header = '<form method="post">' + pif.create_token()

    rows = ['select', 'from', 'where', 'order']
    entries = [{'title': row, 'value': pif.render.format_text_input(row, 256, 80)} for row in rows]

    footer = '<input type="hidden" name="verbose" value="1">'
    footer += pif.render.format_button_input()
    footer += "</form>"
    footer += mass_sections(pif)

    lsection = dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)
    return pif.render.format_template('simplelistix.html', llineup=dict(section=[lsection]), nofooter=True)


def mass_select(pif):
    # Get table descriptions and use widths.  Allow "*".
    columns = pif.form.get_str('select').split(',')
    table_info = pif.dbh.table_info[pif.form.get_str('from')]
    rows = pif.dbh.fetch(pif.form.get_str('from'), columns=columns + table_info['id'], where=pif.form.get_str('where'), order=pif.form.get_str('order'), tag='mass_select')
    header = '<form method="post">' + pif.create_token()
    header += '<input type="hidden" name="from" value="%s">' % pif.form.get_str('from')
    header += '<input type="hidden" name="select" value="%s">' % pif.form.get_str('select')
    header += '<input type="hidden" name="verbose" value="1">'
    footer = pif.render.format_button_input("save")
    footer += "</form>"
    entries = []

    for row in rows:
	entries.append({col:
	    row[col] if col in table_info['id'] else
		    pif.render.format_text_input(col + "." + '.'.join([str(row[x]) for x in table_info['id']]),
		    256, 40, row[col])
	for col in columns})

    lsection = dict(columns=columns, range=[{'entry': entries}], note='', headers=dict(zip(columns, columns)), header=header, footer=footer)
    return pif.render.format_template('simplelistix.html', llineup=dict(section=[lsection]), nofooter=True)


def mass_save(pif):
    columns = pif.form.get_str('select').split(',')
    table_info = pif.dbh.table_info[pif.form.get_str('from')]

    for key in pif.form.keys(has='.'):
        col, ids = key.split('.', 1)
        if col in columns:
            wheres = pif.dbh.make_where(dict(zip(table_info['id'], ids.split('.'))))
            # where = " and ".join(["%s='%s'" % x for x in wheres])
            # update table set col=value where condition;
            # query = "update %s set %s='%s' where %s" % (pif.form.get_str('from'), col, pif.dbh.escape_string(pif.form.get_str(key)), where)
            # print query, '<br>'
            # pif.dbh.raw_execute(query, tag='mass_save')
            # note: untested
            # note: write might already escape values
            pif.dbh.write(pif.form.get_str('from'), values={col: pif.dbh.escape_string(pif.form.get_str(key))}, where=wheres, modonly=True, tag='mass_save')
    return pif.render.format_template('blank.html', content='')

# ------- varaition dates ------------------------------------------

def dates_main(pif):
    for mvid in pif.form.roots(start='v.'):
	val = pif.form.get_bool('c.' + mvid)
	useful.write_message(mvid, val)
	var = pif.dbh.fetch_variation_bare(*mvid.split('-'))[0]
	var['variation.flags'] = (var['variation.flags'] | pif.dbh.FLAG_MODEL_VARIATION_VERIFIED) if val else (
	    var['variation.flags'] & ~pif.dbh.FLAG_MODEL_VARIATION_VERIFIED)
	pif.dbh.update_variation_bare(var)
    return pif.render.format_template('blank.html', content='')

# ------- add lineup -----------------------------------------------

def lineup_desc_main(pif):
    print pif.render.format_head()
    useful.header_done()
    #for key in pif.form.keys(start='description.'):
    for root in pif.form.roots(start='description.'):
	#root = key[key.find('.') + 1:]
	lm = pif.dbh.depref('lineup_model', pif.dbh.fetch_lineup_model({'id': root})[0])
	if lm['name'] != pif.form.get_str('description.' + root) or lm['style_id'] != pif.form.get_str('style_id.' + root):
	    print root, pif.form.get_str('description.' + root), lm['name']
	    print pif.form.get_str('style_id.' + root), lm['style_id']
	    lm['name'] = pif.form.get_str('description.' + root)
	    lm['style_id'] = pif.form.get_str('style_id.' + root)
	    print pif.dbh.update_lineup_model({'id': root}, lm)
	    print '<br>'
    print pif.render.format_tail()

# TODO add base_id/casting_id for new castings
def add_lineup_main(pif):
    if pif.duplicate_form: #not pif.dbh.insert_token(pif.form.get_str('token')):
	print 'duplicate form submission detected'
    elif pif.form.has('save'):
	print pif.render.format_head()
	useful.header_done()
        add_lineup_final(pif)
	print pif.render.format_tail()
	return
    elif pif.form.has('num'):
        return add_lineup_list(pif)
    return add_lineup_ask(pif)


def add_lineup_ask(pif):
    header = '<form action="mass.cgi">' + pif.create_token()
    entries = [
	{'title': 'Number of models:', 'value': pif.render.format_text_input("num", 8, 8)},
	{'title': 'Year:', 'value': pif.render.format_text_input("year", 4, 4)},
	{'title': 'Region:', 'value': pif.render.format_text_input("region", 4, 4)},
	{'title': 'Model List:', 'value': pif.render.format_text_input("models", 80, 80)},
	{'title': '', 'value': pif.render.format_button_input()},
    ]
    footer = pif.render.format_hidden_input({'type': 'lineup'})
    footer += "</form>"
    lsection = dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)
    return pif.render.format_template('simplelistix.html', llineup=dict(section=[lsection]), nofooter=True)


def add_lineup_final(pif):
    # "I think we could all do better." -- Jim Jeffries
    pif.dbh.dbi.insert_or_update('page_info',
    {
        'id': pif.form.get_str('page_id'),
        'flags': 0,
        'format_type': '',
        'title': '',
        'pic_dir': pif.form.get_str('picdir'),
        'tail': '',
        'description': '',
        'note': '',
    })
    pif.dbh.dbi.insert_or_update('section',
    {
        'id': pif.form.get_str('region'),
        'page_id': pif.form.get_str('page_id'),
        'display_order': 0,
        'category': 'man',
        'flags': 0,
        'name': pif.form.get_str('sec_title'),
        'columns': pif.form.get_int('cols', 4),
        'start': 0,
        'pic_dir': '',
        'disp_format': '%d.',
        'link_format': pif.form.get_str('link_fmt'),
        'img_format': '',
        'note': '',
    })

    for key in pif.form.keys(start='mod_id.'):
        num = key[7:]
        pif.dbh.dbi.insert_or_update('lineup_model',
        {
            'mod_id': pif.form.get_str(key),
            'number': num,
            'style_id': pif.form.get_str('style_id.' + num),
            'picture_id': '',
            'region': pif.form.get_str('region'),
            'year': pif.form.get_str('year'),
            'page_id': pif.form.get_str('page_id'),
            'name': pif.form.get_str('name.' + num),
        })


def add_lineup_list(pif):
    # Currently untested.  Used too rarely to worry about right now.
    modlist = urllib2.urlopen(pif.form.get_str('models')).read().split('\n')
    castings = {x['base_id.rawname'].replace(';', ' '): x['base_id.id'] for x in pif.dbh.fetch_casting_list()}
    num_models = pif.form.get_int('num')
    year = pif.form.get_str('year')
    region = pif.form.get_str('region')

    entries = [
	{'title': 'Page ID:', 'value': pif.render.format_text_input("page_id", 20, 20, value='year.%s' % year)},
	{'title': 'Picture Directory:', 'value': pif.render.format_text_input("picdir", 80, 80)},
	{'title': 'Section Title:', 'value': pif.render.format_text_input("sec_title", 80, 80, value='Matchbox %s %s Lineup' % (year, mbdata.regions[region]))},
	{'title': 'Link Format:', 'value': pif.render.format_text_input("link_fmt", 20, 20, value='%s%s%%03d' % (year[2:], region.lower()))},
	{'title': 'Columns:', 'value': pif.render.format_text_input("cols", 1, 1)},
	{'title': '', 'value': pif.render.format_button_input()},
    ]
    lsection = dict(columns=['title', 'value'], range=[{'entry': entries}], note='Page and Section', noheaders=True,
	header='<form method="post" action="mass.cgi">' + pif.create_token())
    entries = []
    for cnt in range(0, num_models):
	name = modlist.pop(0)
	entries.append({
	    'number': "%s" % (cnt + 1),
	    'mod_id': pif.render.format_text_input("mod_id.%d" % (cnt + 1), 12, 12, value=castings.get(name, '')),
	    'style_id': pif.render.format_text_input("style_id.%d" % (cnt + 1), 3, 3, value='0'),
	    'name': pif.render.format_text_input("name.%d" % (cnt + 1), 64, 64, value=name),
	})
    columns = ['number', 'mod_id', 'style_id', 'name']
    headers = ['Number', 'Model ID', 'Style ID', 'Name']
    footer = pif.render.format_hidden_input({'type': 'lineup'})
    footer += "</form>"
    lsection = dict(columns=['number', 'mod_id', 'style_id', 'name'], range=[{'entry': entries}],
	note='Models', headers=dict(zip(columns, headers)), footer=footer)
    lsection = dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)
    return pif.render.format_template('simplelistix.html', llineup=dict(section=[lsection]), nofooter=True)


# ------- add casting ---------------------------------------------


def add_casting_main(pif):
    if pif.form.has('save'):
        return add_casting_final(pif)

    entries = [
	{'title': "ID:", 'value': pif.render.format_text_input("id", 8, 8, value='')},
	{'title': 'Year:', 'value': pif.render.format_text_input("year", 4, 4, value=pif.form.get_str('year'))},
	{'title': 'Model Type:', 'value': pif.render.format_select('model_type', [x.model_type for x in pif.dbh.fetch_base_id_model_types()], selected='SF')},
	{'title': 'Name:', 'value': pif.render.format_text_input("rawname", 80, 80, value='')},
	{'title': 'Description:', 'value': pif.render.format_text_input("description", 80, 80, value='')},
	{'title': 'Made:', 'value': pif.render.format_checkbox('notmade', [('not', 'not')])},
	{'title': 'Country:', 'value': pif.render.format_select_country('country')},
	{'title': 'Make:', 'value': pif.render.format_select('make', [('unl', 'MBX')] + [(x['vehicle_make.id'], x['vehicle_make.name']) for x in pif.dbh.fetch_vehicle_makes()], blank='')},
	{'title': 'Section:', 'value': pif.render.format_select('section_id', [(x['section.id'], x['section.name']) for x in pif.dbh.fetch_sections(where="page_id like 'man%'")], selected=pif.form.get_str('section_id'))},
	{'title': '', 'value': pif.render.format_button_input('save')},
    ]

    header = '<form name="mass" action="mass.cgi">' + pif.create_token()
    footer = pif.render.format_hidden_input({'type': 'casting'}) + "</form><p>"

    lsections = [dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)]
    return pif.render.format_template('simplelistix.html', llineup=dict(section=lsections), nofooter=True)



def add_casting_final(pif):
    ostr = str(pif.form.get_form()) + '<br>\n'
    if pif.duplicate_form: #not pif.dbh.insert_token(pif.form.get_str('token')):
	print 'duplicate form submission detected'
    else:
	if pif.dbh.fetch_base_id(pif.form.get_str('id')):
	    raise useful.SimpleError("That ID is already in use.")
	# base_id: id, first_year, model_type, rawname, description, flags
	# casting: id, country, make, section_id
	ostr += str(pif.dbh.add_new_base_id({
	    'id': pif.form.get_str('id'),
	    'first_year': pif.form.get_str('year'),
	    'model_type': pif.form.get_str('model_type'),
	    'rawname': pif.form.get_str('rawname'),
	    'description': pif.form.get_str('description'),
	    'flags': pif.dbh.FLAG_MODEL_NOT_MADE if pif.form.get_str('notmade') == 'not' else 0,
	})) + '<br>\n'
	ostr += str(pif.dbh.add_new_casting({
	    'id': pif.form.get_str('id'),
	    'country': pif.form.get_str('country'),
	    'make': pif.form.get_str('make'),
	    'section_id': pif.form.get_str('section_id'),
	    'notes': '',
	})) + '<br>\n'
    return pif.render.format_template('blank.html', content=ostr)


# ------- add pub -------------------------------------------------


def add_pub_main(pif):
    if pif.form.has('save'):
        return add_pub_final(pif)
    entries = [
	{'title': "ID:", 'value': pif.render.format_text_input("id", 8, 8, value='')},
	{'title': 'Year:', 'value': pif.render.format_text_input("year", 4, 4, value=pif.form.get_str('year'))},
	{'title': 'Model Type:', 'value': pif.render.format_select('model_type', sorted(mbdata.model_type_names.items()), selected='BK')},
	{'title': 'Name:', 'value': pif.render.format_text_input("rawname", 80, 80, value='')},
	{'title': 'Description:', 'value': pif.render.format_text_input("description", 80, 80, value='')},
	{'title': 'Made:', 'value': pif.render.format_checkbox('notmade', [('not', 'not')])},
	{'title': 'Country:', 'value': pif.render.format_select_country('country')},
	#{'title': 'Section:', 'value': pif.render.format_select('section_id', [(x['section.id'], x['section.name']) for x in pif.dbh.fetch_sections(where="page_id like 'man%'")], selected=pif.form.get_str('section_id'))},
	{'title': '', 'value': pif.render.format_button_input('save')},
    ]

    header = '<form name="mass" action="mass.cgi">' + pif.create_token()
    footer = pif.render.format_hidden_input({'type': 'pub'}) + "</form><p>"

    lsections = [dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)]
    return pif.render.format_template('simplelistix.html', llineup=dict(section=lsections), nofooter=True)



def add_pub_final(pif):
    if pif.dbh.fetch_base_id(pif.form.get_str('id')):
	raise useful.SimpleError("That ID is already in use.")
    # base_id: id, first_year, model_type, rawname, description, flags
    # publication: id, country, section_id
    ostr = str(pif.form.get_form()) + '<br>\n'
    if pif.duplicate_form: #not pif.dbh.insert_token(pif.form.get_str('token')):
	print 'duplicate form submission detected'
    else:
	ostr += pif.dbh.add_new_base_id({
	    'id': pif.form.get_str('id'),
	    'first_year': pif.form.get_str('year'),
	    'model_type': pif.form.get_str('model_type'),
	    'rawname': pif.form.get_str('rawname'),
	    'description': pif.form.get_str('description'),
	    'flags': pif.dbh.FLAG_MODEL_NOT_MADE if pif.form.get_str('notmade') == 'not' else 0,
	}) + '<br>\n'
	ostr += pif.dbh.add_new_publication({
	    'id': pif.form.get_str('id'),
	    'country': pif.form.get_str('country'),
	    'section_id': pif.form.get_str('model_type').lower(),
	}) + '<br>\n'
    return pif.render.format_template('blank.html', content=ostr)


# ------- add var -------------------------------------------------


def add_var_main(pif):

    if pif.form.get_bool('save'):
	print pif.render.format_head()
	useful.header_done()
	add_var_final(pif)
	print pif.render.format_tail()
	return
    elif pif.form.get_str('mod_id'):
	return add_var_info(pif)
    print pif.render.format_head()
    useful.header_done()
    add_var_ask(pif)
    print pif.render.format_tail()


def add_var_ask(pif):
    print "<form>" + pif.create_token()
    print "Man ID:", pif.render.format_text_input("mod_id", 8, 8, value=pif.form.get_str('mod_id')), '<br>'
    print 'Var ID:', pif.render.format_text_input("var", 8, 8, value=''), '<br>'
    print 'Date:', pif.render.format_text_input("date", 8, 8, value=''), '<br>'
    print 'Imported From:', pif.render.format_text_input("imported_from", 8, 8, value=''), '<br>'
    print pif.render.format_button_input('submit')
    print pif.render.format_hidden_input({'type': 'var'})
    print "</form>"
    print pif.render.format_button('catalog', '/lib/mbusa/', lalso={'target': '_blank'})


var_id_columns = ['mod_id', 'var']
var_attr_columns = ['body', 'base', 'windows', 'interior']
var_data_columns = ['category', 'area', 'date', 'note', 'manufacture', 'imported_from', 'imported_var']
var_record_columns = var_id_columns + var_attr_columns + var_data_columns
def add_var_info(pif):
    mod_id = pif.form.get_str('mod_id')
    mod = pif.dbh.fetch_casting_by_id_or_alias(mod_id)
    if not mod:
	raise useful.SimpleError("Model not found.")
    elif len(mod) > 1:
	raise useful.SimpleError("Multiple models found.")
    mod = pif.dbh.modify_man_item(mod[0])
    mod_id = mod['id']
    var_id = mbdata.normalize_var_id(mod, pif.form.get_str('var'))
    attrs = pif.dbh.fetch_attributes(mod_id)
    attr_names = [x['attribute.attribute_name'] for x in attrs]
    var = pif.dbh.fetch_variation(mod_id, var_id)
    useful.write_message(mod)

    print pif.render.format_head()
    useful.header_done()
    print '<h3>%s</h3>' % mod['name']
    print '<form onsubmit="save.disabled=true; return true;">' + pif.create_token()
    if var:
	print pif.render.format_hidden_input({'store': 'update'})
	var = pif.dbh.depref('variation', var[0])
    else:
	print pif.render.format_hidden_input({'store': 'insert'})
	var = {}
    print '<table class="tb">'
    defs = {'mod_id': mod_id,
	    'var': var_id,
	    'flags': 0,
	    'manufacture': 'Thailand',
	    'imported_from': pif.form.get_str('imported_from'),
	    'imported_var': var_id,
	    'date': pif.form.get_str('date')
    }
    cats = [(x['category.id'], x['category.name'],) for x in pif.dbh.fetch_categories()]
    for col in var_id_columns + [None] + var_attr_columns + attr_names + [None] + var_data_columns:
	if col:
	    val = var.get(col) if var.get(col) else defs.get(col, '')
	    print '<tr><td class="eb">%s</td>' % col
	    if var:
		print '<td class="eb">%s</td>' % val
	    print '<td class="eb">%s</td></tr>' % (
		pif.render.format_select(col, sorted(cats), val, blank='') if col == 'category' else
		pif.render.format_text_input(col, 64, 32, value=val))
	else:
	    print '<tr><td class="eb" colspan="%s"></td></tr>' % (3 if var else 2)
    print "</table>"
    print pif.render.format_button_input('save')
    print pif.render.format_hidden_input({'type': 'var'})
    print pif.render.format_link('/cgi-bin/single.cgi?id=' + mod_id, mod_id)
    print "</form>"

    for var in pif.dbh.fetch_variations(mod_id):
	lnk = '/cgi-bin/vars.cgi?edit=1&mod=%(variation.mod_id)s&var=%(variation.var)s' % var
	print var['variation.var'], ':', pif.render.format_link(lnk, var['variation.text_description']), '<br>'
    print pif.render.format_tail()


def add_var_final(pif):
    mod_id = pif.form.get_str('mod_id')
    var_id = pif.form.get_str('var')
    attrs = pif.dbh.fetch_attributes(mod_id)
    attr_names = [x['attribute.attribute_name'] for x in attrs]
    upd = False
    if pif.form.get_str('store') == 'update':
	var = pif.dbh.depref('variation', pif.dbh.fetch_variation(mod_id, var_id))
	if var:
	    var = var[0]
	    upd = True
	else:
	    var = {}
    else:
	var = {}
    for col in var_record_columns + attr_names:
	var[col] = pif.form.get_str(col)
    print var, '<br>'
    if pif.duplicate_form: #not pif.dbh.insert_token(pif.form.get_str('token')):
	print 'duplicate form submission detected'
    elif upd:
	pif.dbh.update_variation(var, {'mod_id': mod_id, 'var': var_id}, verbose=True)
    else:
	pif.dbh.insert_variation(mod_id, var_id, var, verbose=True)
    pif.dbh.recalc_description(mod_id, showtexts=False, verbose=False)
    raise useful.Redirect('/cgi-bin/vars.cgi?edit=1&mod=%s&var=%s' % (mod_id, var_id))


# ------- casting_related ------------------------------------------


def show_all_casting_related(pif):
    useful.write_message('show_all_casting_related')
    print pif.render.format_head()
    # 'columns': ['id', 'model_id', 'related_id', 'section_id', 'picture_id', 'description'],
    print 'show_all_casting_related', pif.form, '<br>'

    mod_id = ''
    section_id = pif.form.get_str('section_id', 'single')
    crl = pif.dbh.fetch_casting_related_models()
    crd_m = {}
    crd_r = {}
    for cr in crl:
	if mod_id in (None, cr['casting_related.model_id'], cr['casting_related.related_id']):
	    if mod_id or cr['m.model_type'] in ('SF', 'RW') or cr['r.model_type'] in ('SF', 'RW'):
		m_id = cr['casting_related.model_id']
		r_id = cr['casting_related.related_id']
		if m_id < r_id:
		    crd_m[(m_id, r_id)] = cr
		    crd_r.setdefault((m_id, r_id), {})
		else:
		    crd_m.setdefault((r_id, m_id), {})
		    crd_r[(r_id, m_id)] = cr

    print '<form action="mass.cgi" onsubmit="save.disabled=true; return true;">' + pif.create_token()
    print '<table border=1>'
    print pif.render.format_hidden_input({'section_id': section_id, 'type': 'related'})
    cnt = 0
    for cr in crd_m:
	cnt += 1
	print '<tr>'
	print '<td><a href="%s">%s</a></td>' % (pif.dbh.get_editor_link('casting_related', {'id': crd_m[cr].get('casting_related.id', '')}), crd_m[cr].get('casting_related.id', ''))
	print '<td><a href="single.cgi?id=%s">%s</a><input type="hidden" name="m.%s" value="%s"></td>' % (cr[0], cr[0], cnt, cr[0])
	print '<td>', crd_m[cr].get('m.rawname', ''), '</td>'
	print '<input type="hidden" name="im.%s" value="%s">' % (cnt, crd_m[cr].get('casting_related.id', ''))
	#print '<td>', crd_r[cr].get('casting_related.id', '') if cr in crd_r else '', '</td>'
	if cr in crd_r:
	    print '<td><a href="%s">%s</a></td>' % (pif.dbh.get_editor_link('casting_related', {'id': crd_r[cr].get('casting_related.id', '')}), crd_r[cr].get('casting_related.id', ''))
	else:
	    print '<td></td>'
	print '<td><a href="single.cgi?id=%s">%s</a><input type="hidden" name="r.%s" value="%s"></td>' % (cr[1], cr[1], cnt, cr[1])
	print '<td>', crd_m[cr].get('r.rawname', ''), '' if cr in crd_r else '(missing)', '</td>'
	if cr in crd_r:
	    print '<input type="hidden" name="ir.%s" value="%s">' % (cnt, crd_r[cr].get('casting_related.id', ''))
	print '</tr><tr>'
	print '<td colspan=3>%s</td>' % crd_m[cr].get('m.description', '')
	print '<td colspan=3>%s</td>' % crd_m[cr].get('r.description', '')
	print '</tr><tr>'
	rd = crd_r[cr].get('casting_related.description', '') if cr in crd_r else ''
	print '<td colspan=3><input type="text" name="dr.%s" value="%s"></td>' % (cnt, rd)
	print '<td colspan=3><input type="text" name="dm.%s" value="%s"></td>' % (cnt, crd_m[cr].get('casting_related.description', ''))
	print '</tr><tr>'
	rd = crd_r[cr].get('casting_related.section_id', '') if cr in crd_r else ''
	print '<td colspan=3><input type="text" name="sr.%s" value="%s"></td>' % (cnt, rd)
	print '<td colspan=3><input type="text" name="sm.%s" value="%s"></td>' % (cnt, crd_m[cr].get('casting_related.section_id', ''))
	print '</tr>'
    print '</table>'
    print pif.render.format_button_input('save')
    print '</form><hr>'
    print pif.render.format_tail()


def edit_casting_related_ask(pif):
    useful.write_message('edit_casting_related_ask')
    header = '<form action="mass.cgi">' + pif.create_token()
    entries = [
	{'title': 'Model:', 'value': pif.render.format_text_input("mod_id", 16, 16)},
	{'title': '', 'value': pif.render.format_button_input()},
	{'title': '', 'value': pif.render.format_button("show all", "mass.cgi?type=related&show_all=1")},
    ]
    footer = pif.render.format_hidden_input({'type': 'related'})
    footer += "</form>"
    lsection = dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)
    return pif.render.format_template('simplelistix.html', llineup=dict(section=[lsection]), nofooter=True)


def edit_casting_related(pif):
    useful.write_message('edit_casting_related')
    if pif.form.has('show_all'):
	return show_all_casting_related(pif)
    if not pif.form.has('mod_id'):
	return edit_casting_related_ask(pif)

    print pif.render.format_head()
    mod_id = pif.form.get_str('mod_id')
    section_id = pif.form.get_str('section_id', 'single')
    # 'columns': ['id', 'model_id', 'related_id', 'section_id', 'picture_id', 'description'],
    print 'edit_casting_related', pif.form, '<br>'
    print 'This currently only handles single.<br>'

    revlist = pif.form.get_list('rev')
    revdict = {}
    if pif.form.has('save'):
	for root in pif.form.roots(start='i'):
	    rec = {'id': pif.form.get_str('i' + root),
		   'model_id': pif.form.get_str('m' + root),
		   'related_id': pif.form.get_str('r' + root),
		   'description': pif.form.get_str('d' + root),
		   'flags': pif.form.get_str('f' + root, '0'),
		   'section_id': section_id,
		   'picture_id': '',
	    }
	    revdict[pif.form.get_str('m' + root)] = root[1:] in revlist
	    pif.dbh.update_casting_related(rec)
	print revdict
	for upd_id in revdict:
	    if revdict[upd_id]:
		pif.dbh.update_flags('base_id', pif.dbh.FLAG_MODEL_CASTING_REVISED, 0, where="id='%s'" % upd_id)
		print upd_id, 'on<br>'
	    else:
		pif.dbh.update_flags('base_id', 0, pif.dbh.FLAG_MODEL_CASTING_REVISED, where="id='%s'" % upd_id)
		print upd_id, 'off<br>'

    # id          | int(11)
    # model_id    | varchar(12)
    # related_id  | varchar(12)
    # section_id  | varchar(16)
    # picture_id  | varchar(12) - always blank for single
    # description | varchar(256)

    crl_m = pif.dbh.fetch_casting_relateds(mod_id=mod_id, section_id=section_id)
    crl_r = pif.dbh.fetch_casting_relateds(rel_id=mod_id, section_id=section_id)

    crd_m = {x['casting_related.related_id']: x for x in crl_m}
    crd_r = {x['casting_related.model_id']: x for x in crl_r}
    keys = set(crd_m.keys() + crd_r.keys())
    if pif.form.has('r'):
	keys.add(pif.form.get_str('r'))
    print '<hr>'

    def show_rel(num, cr):
	print '<td>', cr.get('casting_related.id', '')
	print pif.render.format_hidden_input({'i.%s' % num: cr.get('casting_related.id', 0)}), '</td>'
	for tag, key, wid in [
		('m', 'casting_related.model_id', 12),
		('r', 'casting_related.related_id', 12),
		('d', 'casting_related.description', 256),
		('f', 'casting_related.flags', 4),
	    ]:
	    print '<td>', pif.render.format_text_input('%s.%s' % (tag, num), wid, min(wid, 64), value=str(cr.get(key, '0' if tag == 'f' else ''))), '</td>'

    print '<form name="edit" method="post" action="mass.cgi">' + pif.create_token()
    print '<table border=1>'

    print '<table border=1>'
    num = 1
    revised = []
    for rel_id in keys:
	print '<tr>'
	print '<td>%s %s</td>' % (num, section_id)
	if rel_id in crd_r:
	    print '<td colspan=4>%s</td>' % pif.render.format_link('/cgi-bin/single.cgi?id=' + crd_r[rel_id]['base_id.id'], crd_r[rel_id]['base_id.rawname'])
	    if crd_r[rel_id]['base_id.flags'] & pif.dbh.FLAG_MODEL_CASTING_REVISED:
		revised.append(str(num))
	else:
	    print '<td colspan=4></td>'
	print '<td>%s</td>' % (num + 1)
	if rel_id in crd_m:
	    print '<td colspan=4>%s</td>' % pif.render.format_link('/cgi-bin/single.cgi?id=' + crd_m[rel_id]['base_id.id'], crd_m[rel_id]['base_id.rawname'])
	    if crd_m[rel_id]['base_id.flags'] & pif.dbh.FLAG_MODEL_CASTING_REVISED:
		revised.append(str(num + 1))
	else:
	    print '<td colspan=4></td>'
	print '</tr>'
	print '<tr>'
	print '<td>%s</td>' % pif.render.format_checkbox('rev', [(str(num), 'R')], checked=revised)
	if rel_id in crd_r:
	    print '<td colspan=4>%s</td>' % pif.render.format_image_required(mod_id, pdir=config.IMG_DIR_MAN, largest=mbdata.IMG_SIZ_SMALL)
	else:
	    print '<td colspan=4></td>'
	print '<td>%s</td>' % pif.render.format_checkbox('rev', [(str(num + 1), 'R')], checked=revised)
	if rel_id in crd_m:
	    print '<td colspan=4>%s</td>' % pif.render.format_image_required(rel_id, pdir=config.IMG_DIR_MAN, largest=mbdata.IMG_SIZ_SMALL)
	else:
	    print '<td colspan=4></td>'
	print '</tr>'
	print '<tr>'
	if rel_id in crd_m:
	    show_rel(num, crd_m[rel_id])
	else:
	    show_rel(num, {'casting_related.model_id': mod_id, 'casting_related.related_id': rel_id})
	num += 1
	if rel_id in crd_r:
	    show_rel(num, crd_r[rel_id])
	else:
	    show_rel(num, {'casting_related.model_id': rel_id, 'casting_related.related_id': mod_id})
	print '</tr>'
	num += 1
    print '</table>'

    print pif.render.format_button_input('save')
    print pif.render.format_hidden_input({'mod_id': pif.form.get_str('mod_id'), 'type': 'related'})
    print pif.render.format_hidden_input({'section_id': section_id})
    print '</form><hr>'
    if pif.form.has('mod_id'):
	print '<form name="add" action="mass.cgi" onsubmit="add.disabled=true; return true;">' + pif.create_token()
	print pif.render.format_hidden_input({'mod_id': pif.form.get_str('mod_id'), 'type': 'related'})
	print pif.render.format_text_input('r', 12)
	print pif.render.format_button_input('add')
	print pif.render.format_hidden_input({'section_id': section_id})
	print '</form>'
    print pif.render.format_tail()

# ------- packs ----------------------------------------------------

# should be able to either edit an existing or create a new pack here
def add_pack(pif):
    if pif.form.has('save'):
	add_pack_save(pif)
    elif pif.form.has('delete'):
	add_pack_delete(pif)
    elif pif.form.get_str('pack'):
	return add_pack_form(pif)
    return add_pack_ask(pif)


def add_pack_ask(pif):
    pid = pif.form.get_str('id')
    if not pid:
	pid = pif.form.get_str('section_id')
    if '.' in pid:
	pid = pid[pid.find('.') + 1:]
    header = '<form action="mass.cgi">' + pif.create_token()
    entries = [
	{'title': 'Section ID:', 'value': pif.render.format_text_input("section_id", 12, 12, value=pid)},
	{'title': 'Pack ID:', 'value': pif.render.format_text_input("pack", 12, 12)},
	{'title': 'Var ID:', 'value': pif.render.format_text_input("var", 12, 12)},
	{'title': 'Number of Models:', 'value': pif.render.format_text_input("num", 4, 4, value=pif.form.get_str('num'))},
	{'title': '', 'value': pif.render.format_button_input()},
    ]
    footer = pif.render.format_hidden_input({'type': 'pack'})
    footer += pif.render.format_hidden_input({'verbose': '1'})
    footer += "</form>"
    lsection = dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)
    return pif.render.format_template('simplelistix.html', llineup=dict(section=[lsection]), nofooter=True)


pack_sec = {
    '5packs' : 'X.63',
    'lic5packs' : 'X.64',
    'launcher' : 'X.66',
    '10packs' : 'X.65',
    '2packs' : 'X.66',
    'rwgs' : 'X.62',
    'sfgs' : 'X.62',
    'rwps' : 'X.61',
}
def add_pack_form(pif):
    pack_id = pif.form.get_str('pack')
    long_pack_id = pif.form.get_str('pack') + ('-' + pif.form.get_str('var') if pif.form.get_str('var') else '')

    section_id = pif.form.get_str('section_id')
    if section_id not in pack_sec:
	raise useful.SimpleError('Unrecognized section id.')
    year = pack_id[:4]
    if not year.isdigit():
	year = '0000'
    base_id = pif.dbh.fetch_base_id(id=pack_id)
    pack = pif.dbh.fetch_pack(id=pack_id, var=pif.form.get_str('var'))
    pack_img = pif.render.find_image_file(long_pack_id, pdir=config.IMG_DIR_PROD_PACK, largest='g')

    header = '<hr>\n'
    header += str(pif.form) + '<hr>\n'
    header += '<form action="mass.cgi">\n' + pif.create_token()
    header += '<input type="hidden" name="verbose" value="1">\n'
    header += '<input type="hidden" name="type" value="pack">\n'

    if base_id:
	header += id_attributes(pif, 'base_id', base_id)
    if pack:
	pack = pack[0]
	header += id_attributes(pif, 'pack', pack)
    else:
	pack = {
	    'base_id.id': base_id['base_id.id'] if base_id else pack_id,
	    'base_id.first_year': base_id['base_id.first_year'] if base_id else year,
	    'base_id.model_type': base_id['base_id.model_type'] if base_id else 'MP',
	    'base_id.rawname': base_id['base_id.rawname'] if base_id else '',
	    'base_id.description': base_id['base_id.description'] if base_id else '',
	    'base_id.flags': base_id['base_id.flags'] if base_id else 0,
	    'pack.id': pack_id,
	    'pack.var': pif.form.get_str('var'),
	    'pack.page_id': 'packs.' + section_id,
	    'pack.section_id': section_id,
	    'pack.end_year': year,
	    'pack.region': 'W',
	    'pack.layout': '5v',
	    'pack.product_code': '',
	    'pack.material': 'C',
	    'pack.country': 'TH',
	    'pack.note': '',
	}

    header += pif.render.format_button("edit", "imawidget.cgi?d=.%s&f=%s.jpg" % (config.IMG_DIR_PROD_PACK, pack_id))
    header += pif.render.format_button("upload", "upload.cgi?d=.%s&n=%s" % (config.IMG_DIR_PROD_PACK, pack_id))
    header += '%(pack.page_id)s/%(pack.id)s<br>' % pack
    header += '/'.join(pack_img) + '<br>'
    header += '<a href="imawidget.cgi?d=./%s&f=%s">%s</a>' % (pack_img + (pif.render.format_image_required(long_pack_id, pdir=config.IMG_DIR_PROD_PACK, largest='g'),))
    header += '<a href="imawidget.cgi?d=.%s&f=%s.jpg">%s</a><br>' % (config.IMG_DIR_MAN, 's_' + pack_id, pif.render.format_image_required('s_' + pack_id, pdir=config.IMG_DIR_MAN))
    header += pif.render.format_image_required(long_pack_id, pdir=config.IMG_DIR_PROD_PACK) + '<br>'

    pack_num = int(pack['pack.note'][2:-1]) if pack['pack.note'].startswith('(#') else 0
    linmod = pif.dbh.fetch_lineup_model(where="mod_id='%s'" % pack_id)
    linmod = linmod[0] if linmod else {
	'lineup_model.id': 0, # delete later
	'lineup_model.base_id': '%s%s%02d' % (year, pack_sec[section_id].replace('.', ''), pack_num),
	'lineup_model.mod_id': pack_id,
	'lineup_model.number': pack_num,
	'lineup_model.flags': 0,
	'lineup_model.style_id': '',
	'lineup_model.picture_id': '',
	'lineup_model.region': pack_sec[section_id],
	'lineup_model.year': year,
	'lineup_model.name': pack['base_id.rawname'],
	'lineup_model.page_id': 'year.' + year,
    }
    x_linmods = [x['lineup_model.base_id'][7:] for x in pif.dbh.fetch_lineup_models(year, pack_sec[section_id])
		    if x.get('lineup_model.region') == pack_sec[section_id]]
    x_linmods.sort()
    llistix = {'section': [], 'note': header}
    llistix['section'].append(entry_form(pif, 'base_id', pack))
    llistix['section'].append(entry_form(pif, 'pack', pack))
    llistix['section'].append(entry_form(pif, 'lineup_model', linmod,
	note=pif.render.format_checkbox('nope', [('1', 'nope')], ['1'] if not linmod['lineup_model.id'] else [])))
    llistix['section'][-1]['header'] = 'in use: %s<br>\n' % ', '.join(x_linmods) + llistix['section'][-1]['header']

    # editor
    #useful.write_message('add_pack_model', pack, long_pack_id)
    llistix['section'].append(add_pack_model(pif, pack, long_pack_id))

    # related
    relateds = pif.dbh.fetch_packs_related(pack_id)
    footer = 'related '
    footer += pif.render.format_button('edit', link='?type=related&section_id=packs&mod_id=%s' % pack_id)
    footer += '<br>\n'
    for rel in relateds:
	footer += rel['pack.id'] + '<br>\n'

    footer += pif.render.format_button_input("save")
    footer += pif.render.format_button_input("delete")
    footer += '</form>'
    llistix['section'][-1]['footer'] = footer

    return pif.render.format_template('simplelistix.html', llineup=llistix)


def add_pack_model(pif, pack, long_pack_id):
    # there may be a better way to do this.
    cols = ['mod', 'var', 'disp', 'edit']
    pmodels = {x + 1: {'pack_model.display_order': x + 1} for x in range(pif.form.get_int('num'))}
    if pack.get('base_id.id'):
	model_list = pif.dbh.fetch_pack_models(pack_id=pack['pack.id'], pack_var=pack['pack.var'], page_id=pack.get('pack.page_id'))

	#for mod in pif.dbh.modify_man_items([x for x in model_list if x['pack_model.pack_id'] == long_pack_id]):
	for mod in pif.dbh.modify_man_items(model_list):
	    sub_ids = [None, '', long_pack_id, long_pack_id + '.' + str(mod['pack_model.display_order'])]
	    if mod['vs.sub_id'] in sub_ids:
		mod['vars'] = []
		if not pmodels.get(mod['pack_model.display_order'], {}).get('pack_model.mod_id'):
		    pmodels[mod['pack_model.display_order']] = mod
		if mod.get('vs.var_id'):
		    pmodels[mod['pack_model.display_order']]['vars'].append(mod['vs.var_id'])

    entries = [
	{
	    'mod': pif.render.format_hidden_input({'pm.id.%s' % key: mod.get('pack_model.id', '0'),
			'pm.pack_id.%s' % key: long_pack_id}) +
		   pif.render.format_link("single.cgi?id=%s" % mod.get('pack_model.mod_id', ''), mod.get('pack_model.mod_id', '')) + ' ' +
	           pif.render.format_text_input("pm.mod_id.%s" % key, 8, 8, value=mod.get('pack_model.mod_id', '')),
	    'var': 'var ' + pif.render.format_text_input("pm.var_id.%s" % key, 80, 20, value='/'.join(list(set(mod.get('vars', ''))))) +
		    ' (' + str(mod.get('pack_model.var_id', '')) + ')',
	    'disp': 'disp ' + pif.render.format_text_input("pm.display_order.%s" % key, 2, 2, value=mod.get('pack_model.display_order', '')),
	    'edit': pif.render.format_button('edit', link=pif.dbh.get_editor_link('pack_model',
			pif.dbh.make_id('pack_model', mod, 'pack_model' + '.'))),
	}
    for key, mod in sorted(pmodels.items())]
    return dict(columns=cols, range=[{'entry': entries}], noheaders=True, header='pack_model<br>')

def add_pack_delete(pif):
    if not pif.duplicate_form:
	#print 'delete base_id', pif.form.get_str('base_id.id'), '<br>'
	pif.dbh.delete_base_id({'id': pif.form.get_str('base_id.id')})
	#print 'delete pack', pif.form.get_str('pack.id'), '<br>'
	pif.dbh.delete_pack(pif.form.get_str('pack.id'))
	pif.dbh.delete_pack_models(pif.form.get_str('pack.page_id'), pif.form.get_str('pack.id'))
	#print 'delete lineup_model', pif.form.get_str('lineup_model.id'), '<br>'
	pif.dbh.delete_lineup_model({'id': pif.form.get_int('lineup_model.id')})


def get_correct_model_id(pif, mod_id):
    alias = pif.dbh.fetch_alias(mod_id)
    return alias.get('base_id.id', mod_id)


def add_pack_save(pif):
    pack_id = pif.form.get_str('pack.id') + ('-' + pif.form.get_str('pack.var') if pif.form.get_str('pack.var') else '')
    useful.write_message(pack_id)

    mods = [x[6:] for x in pif.form.keys(start='pm.id.')]
    pms = [
	{
	    'id': pif.form.get_int('pm.id.' + mod),
	    'pack_id': pack_id,
	    'mod_id': get_correct_model_id(pif, pif.form.get_str('pm.mod_id.' + mod)),
	    'var_id': pif.form.get_str('pm.var_id.' + mod),
	    'display_order': pif.form.get_int('pm.display_order.' + mod),
	}
	for mod in mods]
    useful.write_message('pms', pms)
    useful.write_message('pack', pif.dbh.make_values('pack', pif.form, 'pack.'))
    useful.write_message('base_id', pif.dbh.make_values('base_id', pif.form, 'base_id.'))
    useful.write_message('o_pack_id', pif.form.has('o_pack_id'), pif.form.get_str('o_pack_id'))
    useful.write_message('o_base_id_id', pif.form.has('o_base_id_id'), pif.form.get_str('o_base_id_id'))

    if pif.duplicate_form:
	return

    if pif.form.has('o_base_id_id'):  # update existing records
	pif.dbh.update_base_id(pif.form.get_str('o_base_id_id'), {x: pif.form.get_str('base_id.' + x) for x in pif.dbh.table_info['base_id']['columns']})
    else:
	pif.dbh.add_new_base_id(pif.dbh.make_values('base_id', pif.form, 'base_id.'))

    if pif.form.has('o_pack_id'):  # update existing records
	pif.dbh.update_pack_models(pms)
	pif.dbh.update_variation_select_pack(pms, pif.form.get_str('pack.page_id'), pif.form.get_str('o_pack_id'))

	p_table_info = pif.dbh.table_info['pack']
	if pif.form.get_str('o_pack_id') != pif.form.get_str('pack.id'):  # change id of pack
	    pif.dbh.update_variation_select_subid(pif.form.get_str('pack.id'), pif.form.get_str('pack.page_id'), pif.form.get_str('o_pack_id'))
	    if os.path.exists(pif.render.pic_dir + '/' + pif.form.get_str('o_pack_id') + '.jpg'):
		os.rename(pif.render.pic_dir + '/' + pif.form.get_str('o_pack_id') + '.jpg', pif.render.pic_dir + '/' + pif.form.get_str('pack.id') + '.jpg')
	pif.dbh.update_pack(pif.form.get_str('o_pack_id'), {x: pif.form.get_str('pack.' + x) for x in p_table_info['columns']})

	p_table_info = pif.dbh.table_info['base_id']

    else:  # add new records
	pif.dbh.add_new_pack_models(pms)
	pif.dbh.update_variation_select_pack(pms, pif.form.get_str('pack.page_id'), pif.form.get_str('o_pack_id'))
	pif.dbh.add_new_pack(pif.dbh.make_values('pack', pif.form, 'pack.'))

    # now do lineup_model separately
    if not pif.form.get_int('nope'):
	values = pif.dbh.make_values('lineup_model', pif.form, 'lineup_model.')
	if pif.form.get_int('lineup_model.id'):
	    #print 'update line_model', values, '<br>'
	    pif.dbh.update_lineup_model({'id': pif.form.get_int('lineup_model.id')}, values)
	else:
	    #print 'new line_model', values, '<br>'
	    linmod = pif.dbh.fetch_lineup_model(where="mod_id='%s'" % values['mod_id'])
	    if not linmod:  # goddamn bounciness
		#print 'already<br>'
		del values['id']
		pif.dbh.insert_lineup_model(values)

    #print pif.render.format_link("packs.cgi?page=%s&id=%s" % (pif.form.get_str('pack.section_id'), pif.form.get_str('pack.id')), "pack")


def id_attributes(pif, tab, dat):
    return '\n'.join(['<input type="hidden" name="o_%s_%s" value="%s">\n' % (tab, f, dat.get(tab + '.' + f, ''))
	for f in pif.dbh.table_info[tab]['id']]) + '\n'


paren_re = re.compile('''\((?P<n>\d*)\)''')
def entry_form(pif, tab, dat, div_id=None, note=''):
    if not div_id:
	div_id = tab
    header = tab + ' ' + pif.render.format_button('edit', link=pif.dbh.get_editor_link(tab,
	pif.dbh.make_id(tab, dat, tab + '.')))
    header +=  pif.render.format_button_input_visibility(div_id) + ' ' + note + '<br>'
    descs = pif.dbh.describe_dict(tab)
    entries = []
    for col in pif.dbh.table_info[tab]['columns']:
        coltype = descs.get(col).get('type')
        colwidth = int(paren_re.search(coltype).group('n'))
	entries.append({'title': col, 'type': coltype, 'value': str(dat.get(tab + '.' + col, '')),
			'new_value': pif.render.format_text_input(tab + '.' + col, colwidth, min(colwidth, 80), value=dat.get(tab + '.' + col, ''))})
    return dict(columns=['title', 'type', 'value', 'new_value'], range=[{'entry': entries}], noheaders=True, header=header)


# ------- links ----------------------------------------------------

COBRA	= 1 # offline
MBXFDOC	= 2
COMPARE	= 3 # no scraper
WIKIA	= 4
TOYVAN	= 5
PSDC	= 6
AREH	= 7
DAN	= 8
MBXF	= 9
CF	= 10
KULIT	= 11
DCPLUS	= 12
MCCH	= 13 # offline
MBDB	= 14
MBXU	= 15
LW	= 16
YT	= 17

ml_re = re.compile('''<.*?>''', re.M|re.S)
def_re_str = '''<a\s+href=['"](?P<u>[^'"]*)['"].*?>(?P<t>.*?)</a>'''

class LinkScraper(object):
    def_re = re.compile(def_re_str, re.I | re.M | re.S)

    def __init__(self, pif):
	self.pif = pif

    def url_fetch(self, url):
	return useful.url_fetch(url, None)

    def links_parse(self, url):
	data = self.url_fetch(url)
	return [(x, useful.printablize(y)) for x,y in self.def_re.findall(data)]

    def is_valid_link(self, url, lnk):
	return not lnk.startswith('mailto:') and not lnk.startswith('javascript:')

    def clean_link(self, lnk):
	return lnk

    def clean_name(self, lnk, txt):
	return txt.replace('<', '[').replace('>', ']')

    def calc_page_id(self, lnk, txt):
	return ''

    def clean_page_id(self, page_id):
	if not page_id.startswith('single'):
	    return ''
	page_id = page_id[7:]
	mod = self.pif.dbh.fetch_casting(page_id)
	if mod:
	    return 'single.' + mod['id']
	mod = self.pif.dbh.fetch_casting_by_alias(page_id)
	if mod:
	    return 'single.' + mod['id']
	return ''

    def scrape_link(self, url, lnk, txt):
	return {
	    'page_id': self.calc_page_id(lnk, txt),
	    'url': urlparse.urljoin(url, self.clean_link(lnk)),
	    'name': self.clean_name(lnk, txt),
	}

class LinkScraperMBXFDOC(LinkScraper):
    lid = MBXFDOC

class LinkScraperWIKIA(LinkScraper):
    lid = WIKIA

class LinkScraperTOYVAN(LinkScraper):
    lid = TOYVAN

class LinkScraperPSDC(LinkScraper):
    lid = PSDC

    def is_valid_link(self, url, lnk):
	return super(LinkScraperPSDC, self).is_valid_link(url, lnk) and (not 'index.htm' in lnk)

    def links_parse(self, url):
	lnks = []
	for lnk in super(LinkScraperPSDC, self).links_parse(url):
	    for olnk in lnks:
		if olnk[0] == lnk[0]:
		    olnk[1] = olnk[1].strip() + ' ' + lnk[1].strip()
		    break
	    else:
		lnks.append([lnk[0], lnk[1].strip()])
	return lnks

    def calc_page_id(self, lnk, txt):
	return 'single.' + txt[:txt.find(' ')]

    def clean_name(self, lnk, txt):
	return ml_re.sub('', txt).strip()

class LinkScraperAREH(LinkScraper):
    lid = AREH

    site_re_str = '''<option value="(?P<u>[^'"]*)">(?P<t>.*?)</option>'''
    def links_parse(self, url):
	data = self.url_fetch(url)
	return re.compile(self.site_re_str, re.I | re.M | re.S).findall(data)

    def clean_link(self, lnk):
	return lnk[5:] if lnk.startswith('Data_') else lnk

class LinkScraperDAN(LinkScraper):
    lid = DAN

    def is_valid_link(self, url, lnk):
	return lnk.startswith('../mb') or (super(LinkScraperDAN, self).is_valid_link(url, lnk) and
					   not lnk.startswith('man') and not lnk.startswith('../') and
					   not lnk.startswith('http://'))

    def calc_page_id(self, lnk, txt):
	txt = self.clean_name(lnk, txt)
	return self.clean_page_id('single.' + txt[:txt.find(' ')]) if txt else ''

    def clean_name(self, lnk, txt):
	return ml_re.sub('', txt).strip()

class LinkScraperMBXF(LinkScraper):
    lid = MBXF

class LinkScraperCF(LinkScraper):
    lid = CF

    def clean_name(self, lnk, txt):
	return ml_re.sub('', txt)

class LinkScraperKULIT(LinkScraper):
    lid = KULIT

class LinkScraperDCPLUS(LinkScraper):
    lid = DCPLUS

class LinkScraperMBDB(LinkScraper):
    lid = MBDB

    def links_parse(self, url):
	if 'list.php' in url:
	    return super(LinkScraperMBDB, self).links_parse(url)
	topdata = self.url_fetch(url)
	top_re_str = '''<a\s+href=['"](?P<u>list.php?[^'"]*)['"].*?>(?P<t>.*?)</a>'''
	toplinks = re.compile(top_re_str, re.I | re.M | re.S).findall(topdata)
	links = []
	for lnk in toplinks:
	    links.extend(super(LinkScraperMBDB, self).links_parse(urlparse.urljoin(url, lnk[0])))
	return links

    def is_valid_link(self, url, lnk):
	return super(LinkScraperMBDB, self).is_valid_link(url, lnk) and not ('list.php' in lnk or 'index.php' in lnk)

    def calc_page_id(self, lnk, txt):
	return 'single.MB' + self.clean_name(lnk, txt) if 'showcar.php' in lnk else ''

    def clean_name(self, lnk, txt):
	return lnk[lnk.rfind('=') + 1:]

class LinkScraperMBXU(LinkScraper):
    lid = MBXU

    def url_fetch(self, url):
	urlp = urlparse.urlparse(url)
	url = urlparse.urlunparse(urlp[:3] + ('', '', ''))
	data = urlparse.parse_qs(urlp.query)
	return useful.url_fetch(url, data)

class LinkScraperLW(LinkScraper):
    lid = LW

class LinkScraperYT(LinkScraper):
    lid = YT

    def_re = re.compile('''<a href="(?P<url>/watch\?[^"]*)"\s.*?\stitle="(?P<name>[^"]*)"''')
    def links_parse(self, url):
	links = super(LinkScraperYT, self).links_parse(url)
	return [x for x in links if '/watch?' in x[0]]

    def calc_page_id(self, lnk, txt):
	return 'links.others'


link_scraper = {
    MBXFDOC: LinkScraperMBXFDOC,
    WIKIA: LinkScraperWIKIA,
    TOYVAN: LinkScraperTOYVAN,
    PSDC: LinkScraperPSDC,
    AREH: LinkScraperAREH,
    DAN: LinkScraperDAN,
    MBXF: LinkScraperMBXF,
    CF: LinkScraperCF,
    KULIT: LinkScraperKULIT,
    DCPLUS: LinkScraperDCPLUS,
    MBDB: LinkScraperMBDB,
    MBXU: LinkScraperMBXU,
    LW: LinkScraperLW,
    YT: LinkScraperYT,
}


def add_links(pif):
    if pif.form.has('save'):
        return add_links_final(pif)
    elif pif.form.has('url'):
        return add_links_scrape(pif)
    return add_links_ask(pif)


def add_links_ask(pif):
    '''Top level of phase 1.'''
    asslinks = pif.dbh.fetch_link_lines(flags=pif.dbh.FLAG_LINK_LINE_ASSOCIABLE)

    entries = [
	{'title': "URL to scrape:", 'value': pif.render.format_text_input("url", 256, 80, value='')},
	{'title': "Section ID:", 'value': pif.render.format_text_input("section_id", 256, 80, value='single')},
	{'title': "Associated Link:", 'value': pif.render.format_select('associated_link', [(0, '')] + [(x['link_line.id'], x['link_line.name']) for x in asslinks])},
	{'title': '', 'value': pif.render.format_button_input()},
    ]

    header = '<form name="mass" action="mass.cgi">' + pif.create_token()
    footer = pif.render.format_hidden_input({'type': 'links'}) + "</form><p>"

    for lnk in asslinks:
	if lnk['link_line.id'] in link_scraper:
	    footer += '%s %s<br>\n' % (lnk['link_line.id'], pif.render.format_link(lnk['link_line.url'], lnk['link_line.name']))
    lsections = [dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)]
    return pif.render.format_template('simplelistix.html', llineup=dict(section=lsections), nofooter=True)



#-----------------+--------------+------+-----+---------+----------------+
# Field           | Type         | Null | Key | Default | Extra          |
#-----------------+--------------+------+-----+---------+----------------+
# id              | int(11)      | NO   | PRI | NULL    | auto_increment |
# page_id         | varchar(20)  | NO   |     |         |                |
# section_id      | varchar(20)  | YES  |     |         |                |
# display_order   | int(3)       | YES  |     | 0       |                |
# flags           | int(11)      | YES  |     | 0       |                |
# associated_link | int(11)      | YES  |     | 0       |                |
# last_status     | varchar(5)   | YES  |     | NULL    |                |
# link_type       | varchar(1)   | YES  |     |         |                |
# country         | varchar(2)   | YES  |     |         |                |
# url             | varchar(256) | YES  |     |         |                |
# name            | varchar(128) | YES  |     |         |                |
# description     | varchar(512) | YES  |     |         |                |
# note            | varchar(256) | YES  |     |         |                |
#-----------------+--------------+------+-----+---------+----------------+
# 8412 | single.MB897  | single     |             7 |     0 |               7 | 200         | l         |         | http://www.areh.de/HTML/Bas1142.html | Blaze Blaster(2013)                               |             |      |
# 8413 | single.MB899  | single     |             7 |     0 |               7 | 200         | l         |         | http://www.areh.de/HTML/Bas1144.html | Questor(2013)                                     |             |      |

def add_links_scrape(pif):
    '''Top level of phase 2.'''
    url = pif.form.get_str('url')
    site = pif.form.get_int('associated_link')
    scraper = link_scraper.get(site)
    if not scraper:
	raise useful.SimpleError("no scraper for", site)
    scraper = scraper(pif)

    header = '<form method="post" action="mass.cgi">' + pif.create_token()

    columns = ['ch', 'url', 'page_id', 'name', 'description', 'country']
    found = 0
    cnt = 1
    entries = []

    for lnk, txt in scraper.links_parse(url):
	if not scraper.is_valid_link(url, lnk):
	    continue
	dat = scraper.scrape_link(url, lnk, txt.strip())
	if pif.dbh.fetch_link_line_url(dat['url']):
	    found += 1
	    continue
	entries.append({
	    'ch': pif.render.format_checkbox('ch.' + str(cnt), [('1', '')], checked=['1']),
	    'url': pif.render.format_link(dat['url']) +
		   pif.render.format_hidden_input({'url.' + str(cnt): dat['url']}),
	    'page_id': pif.render.format_text_input('page_id.' + str(cnt), 256, 20, dat['page_id']),
	    'name': pif.render.format_text_input('name.' + str(cnt), 256, 40, dat['name']),
	    'description': pif.render.format_text_input('description.' + str(cnt), 256, 20, ''),
	    'country': pif.render.format_text_input('country.' + str(cnt), 2, 2, ''),
	})
	cnt += 1
    footer = pif.render.format_button_input('save')
    footer += pif.render.format_hidden_input({'type': 'links'})
    footer += "%d found and dropped" % found
    footer += "</form>"

    lsections = [dict(columns=columns, range=[{'entry': entries}], note='', headers=dict(zip(columns, columns)), header=header, footer=footer)]
    return pif.render.format_template('simplelistix.html', llineup=dict(section=lsections), nofooter=True)



def add_links_final(pif):
    '''Top level of phase 3.'''
    #print pif.form, '<hr>'
    site = pif.form.get_int('associated_link')
    # cheating: leaving the dot off here removes it from the get_dict call.
    ostr = ''
    for key in pif.form.roots(start='page_id'):
	link_vals = pif.form.get_dict(end=key)
	if link_vals.get('ch'):
	    del link_vals['ch']
	    link_vals.update({'display_order': site,
		'flags': 0, 'country': link_vals.get('country', ''),
		'description': link_vals.get('description', ''),
		'associated_link': site, 'page_id': link_vals.get('page_id', ''),
		'note': '', 'last_status': None, 'link_type': 'l'})
	    ostr += str(link_vals)
	    ostr += ' ' + str(pif.dbh.insert_link_line(link_vals, verbose=True))
	    ostr += '<br>\n'
    return pif.render.format_template('blank.html', content=ostr)

# ------- book -----------------------------------------------------

def add_book(pif):
#-----------+-------------+------+-----+---------+----------------+
# Field     | Type        | Null | Key | Default | Extra          |
#-----------+-------------+------+-----+---------+----------------+
# id        | int(11)     | NO   | PRI | NULL    | auto_increment |
# author    | varchar(64) | YES  |     |         |                |
# title     | varchar(64) | YES  |     |         |                |
# publisher | varchar(32) | YES  |     |         |                |
# year      | varchar(4)  | YES  |     |         |                |
# isbn      | varchar(16) | YES  |     |         |                |
# flags     | int(11)     | YES  |     | 0       |                |
# pic_id    | varchar(16) | YES  |     |         |                |
#-----------+-------------+------+-----+---------+----------------+

    if pif.form.has('save'):
        return add_book_final(pif)
    elif pif.form.has('clone'):
        return add_book_ask(pif, pif.form.get_int('id'))
    return add_book_ask(pif)


def add_book_ask(pif, book_id=None):
    book = {}
    if book_id:
	book = pif.dbh.fetch('book', where="id=%s" % book_id, tag='mass_book')
	book = book[0] if book else {}

    header = '<form name="mass" action="mass.cgi">' + pif.create_token()
    entries = [
	{'title': "ID:", 'value': pif.render.format_text_input("id", 64, 64, value='') +
				  pif.render.format_button_input('clone')},
    ]
    lsections = [dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer='<br>')]
    entries = [
	{'title': "Author:", 'value': pif.render.format_text_input("author", 64, 64, value=book.get('book.author', ''))},
	{'title': "Title:", 'value': pif.render.format_text_input("title", 64, 64, value=book.get('book.title', ''))},
	{'title': "Publisher:", 'value': pif.render.format_text_input("publisher", 32, 32, value=book.get('book.publisher', ''))},
	{'title': "Year:", 'value': pif.render.format_text_input("year", 4, 4, value=book.get('book.year', ''))},
	{'title': "ISBN:", 'value': pif.render.format_text_input("isbn", 16, 16, value=book.get('book.isbn', ''))},
	{'title': "Hidden:", 'value': pif.render.format_checkbox('hidden', [('1', 'yes')])},
	{'title': "Picture ID:", 'value': pif.render.format_text_input("pic_id", 16, 16, value=book.get('book.pic_id', ''))},
	{'title': "Picture URL:", 'value': pif.render.format_text_input("pic_url", 256, 80, value='')},
	{'title': '', 'value': pif.render.format_button_input('save') + pif.render.format_button_reset('mass') +
			       pif.render.format_button('book', 'biblio.cgi?edit=1') +
			       pif.render.format_button('edit', 'editor.cgi?table=book')},
    ]
    footer = pif.render.format_hidden_input({'type': 'book'}) + "</form><p>"
    lsections.append(dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, footer=footer))
    return pif.render.format_template('simplelistix.html', llineup=dict(section=lsections), nofooter=True)


def add_book_final(pif):
    ostr = str(pif.form) + '<br>'
    if not pif.form.has('title'):
	raise useful.SimpleError("No title supplied.")
    if pif.form.get_str('isbn'):
	if pif.dbh.fetch('book', where="isbn='%s'" % pif.form.get_str('isbn'), tag='mass_book'):
	    raise useful.SimpleError("That isbn is already in use.")
    if pif.form.get_str('pic_id') and pif.form.get_str('pic_url'):
	if pif.dbh.fetch('book', where="pic_id='%s'" % pif.form.get_str('pic_id'), tag='mass_book'):
	    raise useful.SimpleError("That pic_id is already in use.")
	images.grab_url_file(pif.form.get_str('pic_url'), '.' + config.IMG_DIR_BOOK, pif.form.get_str('pic_id'))
    vals = {
	'author': pif.form.get_str('author'),
	'title': pif.form.get_str('title'),
	'publisher': pif.form.get_str('publisher'),
	'year': pif.form.get_str('year'),
	'isbn': pif.form.get_str('isbn'),
	'flags': pif.dbh.FLAG_ITEM_HIDDEN if pif.form.get_int('flags') else 0,
	'pic_id': pif.form.get_str('pic_id'),
    }
    ostr += str(vals)
    ostr += str(pif.dbh.write('book', vals, newonly=True, tag='mass_book', verbose=True)) + '<br>'
    if vals['pic_id']:
	ostr += pif.render.format_image_required(vals['pic_id'], pdir='.' + config.IMG_DIR_BOOK)
    return pif.render.format_template('blank.html', content=ostr)

# ------- ads ------------------------------------------------------

def add_ads(pif):
    if pif.form.has('save'):
        return add_ads_final(pif)
    return add_ads_ask(pif)
    #'base_id': ['id', 'first_year', 'model_type'='AD', 'rawname', 'description', 'flags'=0],
    #'publication': ['id', 'country', 'section_id'='ca'],


def add_ads_ask(pif):
    ad_id = pif.form.get_str('id')
    ad = pif.dbh.fetch_publication(ad_id)
    if ad:
	raise useful.SimpleError('Duplicate ID.')
    o_ad_id = pif.form.get_str('id')
    yr = pif.form.get_str('year')
    cy = pif.form.get_str('country')
    desc = pif.form.get_str("description")
    ad = {}
    if ad_id.startswith('ad'):
	ad = pif.dbh.fetch_publication(ad_id)
	ad = ad if ad else {}
    elif yr and cy:
	ad_id = 'ad' + cy.lower() + str(yr)
	ads = pif.dbh.fetch_publications(country=cy, year=yr, order='base_id.id', model_type='AD')
	ad_id += chr(ord(ads[-1]['base_id.id'][8]) + 1) if ads else 'a'

    header = '<form name="mass" action="mass.cgi">' + pif.create_token()
    if desc == ad_id and '_' in desc:
	desc = desc[desc.find('_') + 1:].replace('_', ' ').title()
    if not yr and not cy and ad_id.startswith('ad'):
	if ad_id[4:8].isdigit():
	    yr = ad_id[4:8]
	cy = ad_id[2:4].upper()
    name = 'Advertisement'
    name += ' ;- ' + mbdata.get_countries().get(cy, 'International')
    if yr:
	name += ' - ' + yr
    entries = [
	{'title': "ID:", 'value': pif.render.format_text_input("id", 64, 64, value=ad_id)},
	{'title': "Raw Name:", 'value': pif.render.format_text_input("rawname", 64, 64, value=name)},
	{'title': "Description:", 'value': pif.render.format_text_input("description", 64, 64, desc)},
	{'title': "Year:", 'value': pif.render.format_text_input("first_year", 4, 4, value=yr)},
	{'title': "Country:", 'value': pif.render.format_text_input("country", 16, 16, value=cy)},
	{'title': '', 'value': pif.render.format_button_input('save') + pif.render.format_button_reset('mass')},
    ]
    footer = pif.render.format_hidden_input({'type': 'ads'})
    footer += pif.render.format_hidden_input({'o_id': o_ad_id})
    footer += "</form><p>" + pif.render.format_image_required(o_ad_id, pdir=config.IMG_DIR_ADS)
    lsections = []
    lsections.append(dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer))
    return pif.render.format_template('simplelistix.html', llineup=dict(section=lsections), nofooter=True)


def add_ads_final(pif):
    ostr = str(pif.form) + '<br>'
    if not pif.form.has('id'):
	raise useful.SimpleError("No id supplied.")
    ad_id = pif.form.get_str('id')
    ad = pif.dbh.fetch_publication(ad_id)
    if ad:
	raise useful.SimpleError('Duplicate ID.')
    ostr += str(pif.dbh.add_new_base_id({
	'id': ad_id,
	'first_year': pif.form.get_str('first_year'),
	'model_type': 'AD',
	'rawname': pif.form.get_str('rawname'),
	'description': pif.form.get_str('description'),
	'flags': 0,
    })) + '<br>'
    #'publication': ['id', 'country', 'section_id'='ca'],
    ostr += str(pif.dbh.add_new_publication({
	'id': ad_id,
	'country': pif.form.get_str('country'),
	'section_id': 'ca',
    })) + '<br>'
    o_id = pif.form.get_str('o_id')
    if o_id and o_id != ad_id and os.path.exists('.' + config.IMG_DIR_ADS + '/' + o_id + '.jpg'):
	useful.file_mover('.' + config.IMG_DIR_ADS + '/' + o_id + '.jpg', '.' + config.IMG_DIR_ADS + '/' + ad_id + '.jpg', mv=True)
    return pif.render.format_template('blank.html', content=ostr)

# ------- matrix ---------------------------------------------------

# should be able to either edit an existing or create a new matrix here
def add_matrix(pif):
    if pif.form.has('save'):
	add_matrix_save(pif)
    elif pif.form.get_str('section_id'):
	return add_matrix_form(pif)
    return add_matrix_ask(pif)


def add_matrix_ask(pif):
    pid = pif.form.get_str('id')
    if '.' in pid:
	pid = pid[pid.find('.') + 1:]
    header = '<form action="mass.cgi">' + pif.create_token()
    entries = [
	{'title': 'Year:', 'value': pif.render.format_text_input("year", 4, 4)},
	{'title': 'Page ID:', 'value': pif.render.format_text_input("page_id", 24, 24)},
	{'title': 'Section ID:', 'value': pif.render.format_text_input("section_id", 12, 12, value=pid)},
	{'title': 'Number of Models:', 'value': pif.render.format_text_input("num", 4, 4)},
	{'title': '', 'value': pif.render.format_button_input()},
    ]
    footer = pif.render.format_hidden_input({'type': 'matrix'})
    footer += pif.render.format_hidden_input({'verbose': '1'})
    footer += "</form>"
    lsection = dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)
    return pif.render.format_template('simplelistix.html', llineup=dict(section=[lsection]), nofooter=True)


def add_matrix_form(pif):
    # add picture info.  add vs ref info.
    year = pif.form.get_str('year')
    page_id = pif.form.get_str('page_id')
    section_id = pif.form.get_str('section_id')
    page = pif.dbh.fetch_page(id=page_id)
    section = pif.dbh.fetch_section(page_id=page_id, sec_id=section_id)
    category = ''
    useful.write_message('page', str(page))
    useful.write_message('section', str(section))

    header = '<hr>\n'
    header += str(pif.form) + '<hr>\n'
    header += '<form action="mass.cgi">\n' + pif.create_token()
    header += '<input type="hidden" name="verbose" value="1">\n'
    header += '<input type="hidden" name="type" value="matrix">\n'

    if page:
	header += id_attributes(pif, 'page_info', page)
    else:
	page = {
	    'page_info.id': page_id,
	    'page_info.flags': 1,
	    'page_info.format_type': 'matrix',
	    'page_info.pic_dir': 'pic/prod/series',
	}

    if section:
	header += id_attributes(pif, 'section', section)
    else:
	section = {
	    'section.id': section_id,
	    'section.page_id': page_id,
	    'section.columns': 4,
	}

    linmod = pif.dbh.fetch_lineup_model(where="mod_id='%s' and picture_id='%s'" % (page_id, section_id))
    linmod = linmod[0] if linmod else {
	'lineup_model.id': 0, # delete later
	'lineup_model.base_id': '%sX1100' % year,
	'lineup_model.mod_id': page_id,
	'lineup_model.number': 0,
	'lineup_model.flags': 0,
	'lineup_model.style_id': '',
	'lineup_model.picture_id': section_id,
	'lineup_model.region': 'X.11',
	'lineup_model.year': year,
	'lineup_model.name': section.get('section.name', ''),
	'lineup_model.page_id': 'year.' + year,
    }

    llistix = {'section': [], 'note': header}
    llistix['section'].append(entry_form(pif, 'page_info', page))
    llistix['section'].append(entry_form(pif, 'section', section))
    llistix['section'].append(entry_form(pif, 'lineup_model', linmod,
	note=pif.render.format_checkbox('nope', [('1', 'nope')], ['1'] if not linmod['lineup_model.id'] else [])))

    mm, category = add_matrix_model(pif, section)
    llistix['section'].append(mm)
    llistix['section'][0]['range'][-1]['entry'].append({'title': 'category', 'type': 'varchar(8)', 'value': category,
			'new_value': pif.render.format_text_input('category', 8, 8, value=category) + ' for variation_select'})

    footer = ''
    footer += pif.render.format_button_input("save")
    footer += '</form>'
    llistix['section'][-1]['footer'] = footer

    return pif.render.format_template('simplelistix.html', llineup=llistix)


def add_matrix_model(pif, section):
    category = ''
    cols = ['display_order', 'mod_id', 'var_id', 'name', 'range_id', 'flags', 'edit']
    mmodels = {x + 1: {'matrix_model.display_order': x + 1, 'vars': []} for x in range(pif.form.get_int('num'))}
    mmodelsdb = pif.dbh.fetch_matrix_models_variations(section['section.page_id'], section=section['section.id'])
    for mmdb in mmodelsdb:
	if mmdb['vs.sub_id'] and mmdb['vs.sub_id'] != section['section.id']:
	    continue
	if mmdb['vs.category']:
	    category = mmdb['vs.category']
	dispo = mmdb['matrix_model.display_order']
	if dispo not in mmodels:
	    mmodels[dispo] = {'matrix_model.display_order': dispo, 'vars': []}
	if mmodels[dispo].get('matrix_model.id'):
	    useful.write_message('duplicate matrix_model entry found:', mmodels[dispo]['matrix_model.id'], mmdb['matrix_model.id'])
	mmodels[dispo].update(mmdb)
	if mmdb['v.var']:
	    mmodels[dispo]['vars'].append(mmdb['v.var'])

    def mod_name(mod):
	if mod.get('matrix_mode.name'):
	    return mod['matrix_model.name']
	return mod.get('base_id.rawname', '')

    entries = [
	{
	    'mod_id': pif.render.format_hidden_input({'mm.id.%s' % key: mod.get('matrix_model.id', '0'),
			'mm.matrix_id.%s' % key: mod.get('matrix_model.matrix_id', '')}) +
		   pif.render.format_link("single.cgi?id=%s" % mod.get('matrix_model.mod_id', ''), mod.get('matrix_model.mod_id', '')) + ' ' +
	           pif.render.format_text_input("mm.mod_id.%s" % key, 8, 8, value=mod.get('matrix_model.mod_id', '')),
	    'var_id': pif.render.format_text_input("mm.var_id.%s" % key, 20, 20, value='/'.join(sorted(set(mod.get('vars', []))))),
	    'display_order': 'disp ' + pif.render.format_text_input("mm.display_order.%s" % key, 3, 3, value=mod.get('matrix_model.display_order', '')),
	    'edit': pif.render.format_button('edit', link=pif.dbh.get_editor_link('matrix_model',
			pif.dbh.make_id('matrix_model', mod, 'matrix_model' + '.'))) + str(mod.get('matrix_model.id', '')),
	    'name': pif.render.format_text_input("mm.name.%s" % key, 80, 20, value=mod_name(mod)),
	    'range_id': pif.render.format_text_input("mm.range_id.%s" % key, 4, value=mod.get('matrix_model.range_id', mod.get('matrix_model.display_order', '0'))),
	    'flags': pif.render.format_text_input("mm.flags.%s" % key, 4, value=str(mod.get('matrix_model.flags', 0))),
	}
	for key, mod in sorted(mmodels.items())]

    return dict(columns=cols, range=[{'entry': entries}], noheaders=True, header='matrix_model<br>'), category


def add_matrix_save(pif):
    category = pif.form.get_str('category', '')
    page_info = pif.form.get_dict(start='page_info.')
    section = pif.form.get_dict(start='section.')
    lineup_model = pif.form.get_dict(start='lineup_model.')
    #useful.write_message(page_info)
    pif.dbh.insert_or_update_page(page_info)
    #useful.write_message(section)
    pif.dbh.insert_or_update_section(section)
    if not pif.form.get_int('nope'):
	#useful.write_message(lineup_model)
	pif.dbh.insert_lineup_model(lineup_model, newonly=False)
    thisis = {'page_id': page_info['id'], 'section_id': section['id']}
    modvars = []
    for root in pif.form.roots(start='mm.id'):
	mm = pif.form.get_dict(start='mm.', end=root)
	if not mm.get('mod_id'):
	    continue
	if 'id' in mm and (not mm['id'] or not int(mm['id'])):
	    del mm['id']
	if 'var_id' in mm:
	    modvars.extend([(mm['mod_id'], x) for x in mm['var_id'].split('/')])
	    del mm['var_id']
	mm.update(thisis)
	useful.write_message('matrix_model', mm)
	pif.dbh.insert_or_update_matrix_model(mm, verbose=True)
    pif.dbh.update_variation_selects_for_ref(modvars, ref_id=page_info['id'], sub_id=section['id'], category=category)
    useful.write_message(modvars, page_info['id'], section['id'], category)
    return

    if pif.form.has('o_id'):  # update existing records
	pif.dbh.update_matrix_models(mms)
	pif.dbh.update_variation_select_matrix(pms, pif.form.get_str('matrix.page_id'), pif.form.get_str('o_id'))

	p_table_info = pif.dbh.table_info['matrix']
	if pif.form.get_str('o_id') != pif.form.get_str('matrix.id'):  # change id of matrix
	    pif.dbh.update_variation_select_subid(pif.form.get_str('matrix.id'), pif.form.get_str('matrix.page_id'), pif.form.get_str('o_id'))
# ok, this is pretty cool.  I should do this.
	    if os.path.exists(pif.render.pic_dir + '/' + pif.form.get_str('o_id') + '.jpg'):
		os.rename(pif.render.pic_dir + '/' + pif.form.get_str('o_id') + '.jpg', pif.render.pic_dir + '/' + pif.form.get_str('matrix.id') + '.jpg')
	pif.dbh.update_matrix(pif.form.get_str('o_id'), {x: pif.form.get_str('matrix.' + x) for x in p_table_info['columns']})

	p_table_info = pif.dbh.table_info['base_id']
	pif.dbh.update_base_id(pif.form.get_str('o_id'), {x: pif.form.get_str('base_id.' + x) for x in p_table_info['columns']})

    else:  # add new records
	pif.dbh.add_new_matrix_models(pms)
	pif.dbh.update_variation_select_matrix(pms, pif.form.get_str('matrix.page_id'), pif.form.get_str('o_id'))
	pif.dbh.add_new_matrix(pif.dbh.make_values('matrix', pif.form, 'matrix.'))
	pif.dbh.add_new_base_id(pif.dbh.make_values('base_id', pif.form, 'base_id.'))

    # now do lineup_model separately
    if not pif.form.get_int('nope'):
	values = pif.dbh.make_values('lineup_model', pif.form, 'lineup_model.')
	if pif.form.get_int('lineup_model.id'):
	    #print 'update line_model', values, '<br>'
	    pif.dbh.update_lineup_model({'id': pif.form.get_int('lineup_model.id')}, values)
	else:
	    #print 'new line_model', values, '<br>'
	    linmod = pif.dbh.fetch_lineup_model(where="mod_id='%s'" % values['mod_id'])
	    if not linmod:  # goddamn bounciness
		#print 'already<br>'
		del values['id']
		pif.dbh.insert_lineup_model(values)

    #print pif.render.format_link("matrixs.cgi?page=%s&id=%s" % (pif.form.get_str('matrix.section_id'), pif.form.get_str('matrix.id')), "matrix")

# ------- attr_pics ------------------------------------------------

def add_attr_pics(pif):
    if pif.form.has('save'):
	add_attr_pics_save(pif)
    elif pif.form.get_str('attr_type'):
	return add_attr_pics_form(pif)
    return add_attr_pics_ask(pif)


def add_attr_pics_ask(pif):
    header = '<form action="mass.cgi">' + pif.create_token()
    entries = [
	{'title': 'Type:', 'value': pif.render.format_select('attr_type', mbdata.image_adds_list, blank='')},
	{'title': '', 'value': pif.render.format_button_input() + ' ' +
		pif.render.format_button('customs', link='/cgi-bin/custom.cgi') + ' ' +
		pif.render.format_button('errors', link='/cgi-bin/errors.cgi') + ' ' +
		pif.render.format_button('prepros', link='/cgi-bin/prepro.cgi')}
    ]
    footer = pif.render.format_hidden_input({'type': 'attrpics'})
    footer += pif.render.format_hidden_input({'verbose': '1'})
    footer += "</form>"
    lsection = dict(columns=['title', 'value'], range=[{'entry': entries}], note='', noheaders=True, header=header, footer=footer)
    return pif.render.format_template('simplelistix.html', llineup=dict(section=[lsection]), nofooter=True)


def add_attr_pics_form(pif):
    pref = pif.form.get_str('attr_type')
    photogs = [(x.photographer.id, x.photographer.name) for x in pif.dbh.fetch_photographers(pif.dbh.FLAG_ITEM_HIDDEN)]
    credits = {x['photo_credit.name']: x['photo_credit.photographer_id'] for x in
		    pif.dbh.fetch_photo_credits(path=config.IMG_DIR_ADD[1:])}
    fl, rl = get_attr_pics(pif, pref)

    def attr_pic_rec(rec, recid):
	img = pref + '_' + rec['mod_id'].lower()
	if rec['picture_id']:
	    img += '-' + rec['picture_id']
	return {
	    'pic':
		pif.render.format_link('upload.cgi?m=%s&suff=%s&d=%s' %
			(rec['mod_id'], rec['picture_id'], '.' + config.IMG_DIR_ADD),
		    pif.render.fmt_img(img, alt='', pdir=config.IMG_DIR_ADD, required=True)),
	    'desc': pif.render.format_link('single.cgi?id=%s' % rec['mod_id'], rec['mod_id']) + ' ' +
		pif.render.format_button('edit', link=pif.dbh.get_editor_link('attribute_picture', {'id': recid})) + '<br>' +
		pif.render.format_text_input('pic_id.%s' % recid, maxlength=4, showlength=4, value=rec['picture_id']) + ' ' +
		pif.render.format_checkbox('do.%s' % recid, [('1', 'save')], checked=rec['do']) +
		pif.render.format_checkbox('rm.%s' % recid, [('1', 'del')]) + '<br>' +
		pif.render.format_hidden_input({'mod_id.%s' % recid: rec['mod_id'], 'img.%s' % recid: img}) + '<br>' +
		pif.render.format_text_input('desc.%s' % recid, maxlength=128, showlength=40, value=rec['description']) + '<br>' +
		'Credit: ' + pif.render.format_select('crd.%s' % recid, photogs, selected=credits.get(img), blank=''),
	}


    header = '<hr>\n'
    header += '<form action="mass.cgi" method="post">\n' + pif.create_token()
    header += pif.render.format_hidden_input({'verbose': 1, 'type': 'attrpics', 'attr_type': pref})

    llistix = {'section': [], 'note': header}
    entries = [attr_pic_rec(rec, rec['id']) for rec in rl]
    lsec = dict(columns=['pic', 'desc'], range=[{'entry': entries}], noheaders=True)
    llistix['section'].append(lsec)

    entries = [attr_pic_rec(rec, 'n%s' % num) for num, rec in fl]
    lsec = dict(columns=['pic', 'desc'], range=[{'entry': entries}], noheaders=True)
    llistix['section'].append(lsec)

    footer = ''
    footer += pif.render.format_button_input("save")
    footer += '</form>'
    llistix['section'][-1]['footer'] = footer

    return pif.render.format_template('simplelistix.html', llineup=llistix)


def get_attr_pics(pif, pref):
    filelist = os.listdir('.' + config.IMG_DIR_ADD)
    filelist = sorted(list(set([x for x in filelist if x.startswith(pref + '_') and x.endswith('.jpg')])))
    rl = []

    pics = pif.dbh.fetch_attribute_pictures_by_type(pref)
    for pic in pics:
	if not pic.get('base_id.id'):
	    print pic,'<br>'
	    continue
	if pic['attribute_picture.picture_id']:
	    pic_name = '%s_%s-%s.jpg' % (pic['attribute_picture.attr_type'], pic['base_id.id'].lower(), pic['attribute_picture.picture_id'])
	else:
	    pic_name = '%s_%s.jpg' % (pic['attribute_picture.attr_type'], pic['base_id.id'].lower())
	rec = {'mod_id': pic['base_id.id'], 'attr_id': pic['attribute_picture.attr_id'], 'attr_type': pref, 'picture_id': pic['attribute_picture.picture_id'], 'description': pic['attribute_picture.description'], 'id': pic['attribute_picture.id'], 'do': ['1']}
	rl.append(rec)
	if pic_name in filelist:
	    filelist.remove(pic_name)
	else:
	    pass#print 'no pic for', pic_name
    rl.sort(key=lambda x: (x['mod_id'].lower(), x['picture_id'],))
    num = 1
    fl = []
    for fn in filelist:
	if fn.startswith(pref + '_') and fn.endswith('.jpg'):
	    fn = fn[2:-4]
	    mod_id, pic_id = fn.split('-', 1) if '-' in fn else [fn, '']
	    base_id = pif.dbh.fetch_base_id(mod_id)
	    if base_id:
		mod_id = base_id['base_id.id']
# look mod_id up to get casing
	    rec = {'mod_id': mod_id, 'attr_id': 0, 'attr_type': pref, 'picture_id': pic_id, 'description': '', 'do': []}
	    fl.append((num, rec,))
	    num += 1
    return fl, rl


def add_attr_pics_save(pif):
    add_dir = '.' + config.IMG_DIR_ADD
    pref = pif.form.get_str('attr_type')
    for apid in pif.form.roots(start='mod_id.'):
	inp = pif.form.get_dict(end='.' + apid)
	oimg = pif.form.get_str('img.' + apid)
	nimg = pref + '_' + inp['mod_id'].lower()
	if inp['pic_id']:
	    nimg += '-' + inp['pic_id']
	print apid, inp, nimg
	rec = {'mod_id':  pif.form.get_str('mod_id.' + apid), 'picture_id': pif.form.get_str('pic_id.' + apid),
		'description': pif.form.get_str('desc.' + apid), 'attr_id': 0, 'attr_type': pref,
	}

	if pif.form.get_bool('rm.' + apid):
	    print 'del', pif.dbh.delete_attribute_picture(apid)
	if pif.form.get_bool('do.' + apid):
	    if apid.startswith('n'):
		print 'add', pif.dbh.add_attribute_picture(rec)
	    else:
		print 'upd', pif.dbh.update_attribute_picture(rec, apid)

	if oimg != nimg and not os.path.exists(add_dir + '/' + nimg + '.jpg'):
	    useful.file_mover(add_dir + '/' + oimg + '.jpg', add_dir + '/' + nimg + '.jpg', mv=True)
	    if pif.form.get_str('crd.' + apid, config.IMG_DIR_ADD[1:], oimg):
		print 'crd', pif.dbh.delete_photo_credit(config.IMG_DIR_ADD[1:], oimg)

	if pif.form.get_str('crd.' + apid):
	    print 'crd', pif.dbh.write_photo_credit(pif.form.get_str('crd.' + apid), config.IMG_DIR_ADD[1:], oimg)

	print '<br>'

# ------- photogs --------------------------------------------------

def photogs_main(pif):
    if pif.form.has('save'):
	add_photogs_save(pif)
    return add_photogs_form(pif)


def add_photogs_form(pif):
    pref = pif.form.get_str('attr_type')
    photographers = sorted(pif.dbh.fetch_photographers(), key=lambda x: x['photographer.name'])

    def photog_rec(rec):
	recid = rec['id']
	return {
	    'X': pif.render.format_checkbox('X.%s' % recid, [('1', '')], checked='1' if not rec['flags'] & pif.dbh.FLAG_ITEM_HIDDEN else ''),
	    'id': pif.render.format_text_input('id.%s' % recid, maxlength=4, showlength=4, value=rec['id']),
	    'name': pif.render.format_text_input('name.%s' % recid, maxlength=32, showlength=32, value=rec['name']),
	    'url': pif.render.format_text_input('url.%s' % recid, maxlength=128, showlength=64, value=rec['url']),
	}


    header = '<hr>\n'
    header += '<form action="mass.cgi" method="post">\n' + pif.create_token()
    header += pif.render.format_hidden_input({'verbose': 1, 'type': 'photogs'})

    footer = ''
    footer += pif.render.format_button_input("save")
    footer += pif.render.format_button('add', link='/cgi-bin/editor.cgi?table=photographer&id=&add=1')
    footer += '</form>'

    entries = [photog_rec(rec) for rec in photographers]
    lsec = dict(columns=['X', 'id', 'name', 'url'], range=[{'entry': entries}], noheaders=True, footer=footer)
    llistix = {'section': [lsec], 'note': header}

    return pif.render.format_template('simplelistix.html', llineup=llistix)


def add_photogs_save(pif):
    for phid in pif.form.roots(start='id.'):
	inp = pif.form.get_dict(end='.' + phid)
	flags = pif.dbh.FLAG_ITEM_HIDDEN if inp.get('X') else 0
	print phid, inp, flags
	rec = {
	    'id': inp['id'],
	    'name': inp['name'],
	    'url': inp['url'],
	    'flags': flags,
	}

	print '<br>'


# ------- ----------------------------------------------------------

mass_mains_list = [
    ('lineup', add_lineup_main),
    ('casting', add_casting_main),
    ('pub', add_pub_main),
    ('var', add_var_main),
    ('related', edit_casting_related),
    ('pack', add_pack),
    ('links', add_links),
    ('book', add_book),
    ('ads', add_ads),
    ('matrix', add_matrix),
    ('attrpics', add_attr_pics),
]

mass_mains_hidden = {
    'lineup_desc': lineup_desc_main,
    'dates': dates_main,
    'photogs': photogs_main,
}

def mass_sections(pif):
    return '\n'.join([pif.render.format_button(section[0], link='?type=' + section[0]) for section in mass_mains_list])
