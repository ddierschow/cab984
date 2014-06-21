#!/usr/local/bin/python

import sys
sys.path.append("../bin")

import cgi, os
import basics
import Cookie
import useful

if __name__ == '__main__':
    pwd = os.getcwd()
    pif = basics.GetPageInfo('editor')
    pif.render.PrintHtml()
    print pif.render.FormatHead( )
    useful.DumpDict("Globals", globals())
    useful.DumpDict("Basics", basics.__dict__)
    useful.DumpDict("PIF", pif.__dict__)
    useful.DumpDict("Render", pif.render.__dict__)
    print pif.render.FormatButton('reset')
    print pif.render.FormatButton('yodel')
    cgi.print_environ()
    if pif.cgiform:
	cgi.print_form(pif.cgiform)
    print "<h3>Processed form</h3>", pif.form
    cgi.print_directory()
    print "was", pwd
    cgi.print_environ_usage()
    print "<p><h3>Cookies</h3><p>"
    #c = pif.render.GetCookies()

    print 'HTTP_COOKIE =', os.environ.get('HTTP_COOKIE'), '<br>'
    cookie = Cookie.SimpleCookie()
    #cookie.load(os.environ.get('HTTP_COOKIE', ''))

    #file(os.environ['DOCUMENT_ROOT'] + '/bin/value-http', 'w').write(os.environ['HTTP_COOKIE'])
    #print c,'<br>'
    #if c:
	#print "id =", c['id'].value, '<br>'
    useful.DumpDict("Sys", sys.__dict__)

    pif.dbh.IncrementCounter('test')

    print '<form action="xtest.cgi">'
    print pif.render.FormatButtonInput()
    print pif.render.FormatButtonInput('delete')
    print pif.render.FormatButtonInput('yodel')
    print '</form>'

    print pif.render.FormatTail( )