#!/usr/local/bin/python

import basics
import config
import imglib
import mflags
import models
import useful


# -------- makes -----------------------------------

@basics.web_page
def makes_main(pif):
    useful.write_comment('privs', pif.privs)
    make_q = pif.dbh.depref('vehicle_make',
	pif.dbh.fetch_vehicle_makes(where='' if pif.is_allowed('a') else 'not (flags & %s)' % pif.dbh.FLAG_ITEM_HIDDEN))
    makelist = [(x['id'], x['name']) for x in make_q]
    makedict = {x['id']: x for x in make_q}
    makedict['unl'] = {'id': 'unl', 'name': 'Unlicensed', 'company_name': 'Unlicensed', 'flags': 0}
    makedict['unk'] = {'id': 'unk', 'name': 'unknown', 'company_name': 'Make unknown', 'flags': 0}
    footer = ''
    make = pif.form.get_str('make', '')
    makes = [make]

    pif.render.hierarchy_append('/', 'Home')
    pif.render.hierarchy_append('/database.php', 'Database')
    pif.render.hierarchy_append('/cgi-bin/makes.cgi', 'Models by Make')
    if make:
	pif.render.title = 'Models by Make: ' + makedict.get(make, {}).get('name', '')
    if make == 'text':
        pif.render.hierarchy_append(pif.request_uri, 'Search')
    elif make:
        pif.render.hierarchy_append(pif.request_uri, makedict.get(make, {'name': make})['name'])
    pif.render.print_html()

    if make == 'text':
        makename = pif.form.get_str('text')
        if makename:
            makes = []
            for m in makelist:
                if m[1].lower().startswith(makename.lower()):
                    makes.append(m[0])
            if not makes:
                makes = ['unk']
        else:
            make = ''
    elif make and make in makedict:
	links = pif.dbh.fetch_link_lines(page_id='makes', section=make)
	footer = '<ul>' + '\n'.join(['<li>' + pif.render.format_link(x['link_line.url'], x['link_line.name']) for x in links]) + '</ul>\n'
	if pif.is_allowed('a'):  # pragma: no cover
	    footer += pif.render.format_button('ADD LINK', 'editor.cgi?table=link_line&add=1&page_id=makes&section_id=%s&link_type=l' % make)

    if make:
        llineup = show_makes(pif, makedict, makes)
    else:
	makes = ['unk', 'unl'] + sorted([x[0] for x in makelist], key=lambda x: makedict[x]['name'])
        llineup = makes_form(pif, makedict, makes)
    pif.render.set_button_comment(pif, 'make=%s&text=%s' % (pif.form.get_str('make', ''), pif.form.get_str('text', '')))
    if pif.is_allowed('a'):  # pragma: no cover
	if make and make != 'text':
	    footer += pif.render.format_button('edit', link=pif.dbh.get_editor_link('vehicle_make', {'id': make}))
    llineup['footer'] = footer
    pif.render.format_matrix_for_template(llineup)
    return pif.render.format_template('simplematrix.html', llineup=llineup)


def makes_form(pif, makedict, makes):
    cols = 8
    #makelist.sort(key=lambda x: x[1])
    #makelist = [['unk', 'unknown'], ['unl', 'unlicensed']] + makelist
    #makes.cgi?make=alv

    def make_make_link(mdict):
	if not mdict:
	    return {'text': ''}
	pic = pif.render.fmt_img(mdict['id'], prefix='t', pdir=config.IMG_DIR_MAKE)
	name = pic + '<br>' + mdict['name'] if pic else mdict['name']
	return {'text': pif.render.format_link("makes.cgi?make=" + mdict['id'], name),
		'class': 'bgno' if mdict['flags'] else 'bgok'}

    ents = [make_make_link(makedict.get(x)) for x in useful.reflect(makes, cols)]
    llineup = {'id': '', 'name': '', 'columns': cols, 'section': [{'columns': cols, 'range': [{'entry': ents, 'id': 'makelist'}]}],
	'header': '<hr>Choose a make:<br>', 'footer': '<hr>' + str(len(makedict))}
    return llineup


def show_make_selection(pif, make_id, makedict):
    casting_make = make_id
    lsec = dict()  #pif.dbh.fetch_sections({'page_id': pif.page_id})[0]
    make = makedict.get(make_id, {})
    lsec['anchor'] = make_id
    lsec['range'] = []
    lsec['note'] = ''
    lsec['id'] = ''
    lsec['columns'] = 4
    lsec['name'] = pif.render.fmt_img(make_id, prefix='t', pdir=config.IMG_DIR_MAKE) + '<br>' + make.get('company_name', make_id)
    lran = {'id': '', 'name': '', 'anchor': '', 'note': '', 'entry': []}
    where = '' if pif.is_allowed('a') else "section.page_id='manno'"
    if make_id == 'unk':
        casting_make = ''
    castings = pif.dbh.fetch_casting_list_by_make(casting_make, where)
    aliases = []  #pif.dbh.fetch_aliases(where="casting.make='%s'" % casting_make)
    mlist = []

    for mdict in castings:
        mlist.append(pif.dbh.modify_man_item(mdict))

    for mdict in aliases:
        mdict = pif.dbh.modify_man_item(mdict)
        if mdict.get('alias.ref_id'):
            mdict['picture_id'] = mdict['id']
            mdict['id'] = mdict['alias.id']
            #mdict['descs'] = mdict['descs']
            #mdict['descs'].append('same as ' + mdict['ref_id'])
        mlist.append(mdict)

    mlist.sort(key=lambda x: x['name'])
    for mdict in mlist:
        # input mdict:  id, (picture_id), made, country, link, linkid, name, descs, made, unlicensed, scale, (type)
        lran['entry'].append({'text': models.add_model_table_pic_link(pif, mdict, flago=models.flago)})

    lsec['range'].append(lran)
    return lsec


def show_makes(pif, makedict, makes):
    llineup = {'id': '', 'name': '', 'section': [], 'footer': ''}
    models.flago = mflags.FlagList()

    for make_id in makes:
        lsec = show_make_selection(pif, make_id, makedict)
        llineup['section'].append(lsec)
    return llineup


#---- commands ------------------------------

def add_casting_make(pif, mod_id, make_id):
    make = pif.dbh.fetch_vehicle_make(make_id)
    if make:
	print make['vehicle_make.name']
	pif.dbh.add_casting_make(mod_id, make_id)
	mod = pif.dbh.fetch_casting(mod_id)
	if not mod['make']:
	    pif.dbh.write_casting({'make': make_id}, mod_id)


def delete_casting_make(pif, mod_id, make_id):
    pif.dbh.delete_casting_make(mod_id, make_id=None)


def process_graphics(pif):
    for make in pif.dbh.fetch_vehicle_makes():
	mk = make['vehicle_make.id']
	print mk
	pth = '.' + config.IMG_DIR_MAKE + '/t_' + mk + '.gif'
	ofi = imglib.pipe_chain(open(pth),
		imglib.import_file(pth) +
		imglib.resize(x=50) +
		imglib.export_file('.gif', '.gif'),
		stderr=open('/dev/null', 'w'))
	open('.' + config.IMG_DIR_MAKE + '/u_' + mk + '.gif', 'w').write(ofi)


def find_make(pif, make_id):
    for make in pif.dbh.fetch_vehicle_makes():
	if make['vehicle_make.id'].startswith(make_id):
	    print '%-3s %-15s %s' % (make['vehicle_make.id'], make['vehicle_make.name'], make['vehicle_make.company_name'])


def create_make(pif, make_id, name, company=''):
    pif.dbh.add_vehicle_make(make_id, name, company)
    os.copy('.' + config.IMG_DIR_MAKE + '/t_unk.gif', '.' + config.IMG_DIR_MAKE + '/t_' + make_id + '.gif')


def command_help(pif, *args):
    pif.render.message("./vmakes.py [d|a] ...")
    pif.render.message("  d for delete: mod_id make_id")
    pif.render.message("  a for add attributes: mod_id make_id")
    pif.render.message("  g for process graphics")
    pif.render.message("  f for find: make_id")
    pif.render.message("  c for create make: make_id, make_name, company")


command_lookup = {
    'd': delete_casting_make,
    'a': add_casting_make,
    'g': process_graphics,
    'f': find_make,
    'c': create_make,
}


@basics.command_line
def commands(pif):
    if pif.filelist:
	command_lookup.get(pif.filelist[0], command_help)(pif, *pif.filelist[1:])
    else:
	command_help(pif)

#---- ---------------------------------------

if __name__ == '__main__':  # pragma: no cover
    commands(dbedit='')
