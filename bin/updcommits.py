#!/usr/local/bin/python

'''
This script takes commits from the git log and puts them
into the site activity table in the database.

It also does some other housekeeping: man2csv, and writing
the config file for php's use.
'''

import datetime, os, re, subprocess, sys
import basics
import mannum

# Start here


def main(pif):
    write_php_config_file()
    write_jinja2_config_file()


def read_commits(endtime):
    p = subprocess.Popen(["/usr/local/bin/git", "log"], stdout=subprocess.PIPE, stderr=None, close_fds=True)
    l = p.stdout.read()
    commits = list()
    #Date:   Fri Jun 13 19:26:34 2014 +0200
    date_re = re.compile('Date:\s*(?P<d>... ... \d+ \d+:\d+:\d+ \d+)')
    for log_msg in re.compile('\ncommit ', re.M).split(l):
        if log_msg.find('Merge: ') >= 0:
            continue
        m = date_re.search(log_msg)
        if not m:
            continue
        s = m.group('d')
        commit = dict()
        commit['by_user_id'] = 1
        commit['name'] = 'commit'
        commit['description'] = log_msg.split('\n', 4)[4].strip()
        commit['timestamp'] = datetime.datetime.strptime(s, '%a %b %d %X %Y')
        if commit['timestamp'] <= endtime:
            continue
        commits.append(commit)
    commits.sort(key=lambda x: x['timestamp'])
    return commits


def write_php_config_file():
    print "Writing PHP config file."
    configs = []
    fout = open('../bin/config.py').readlines()
    fout[0] = '<?php\n// Generated file.  Do not modify.\n'
    for idx in range(1, len(fout)):
        if fout[idx][0] == '#':
            fout[idx] = '//' + fout[idx][1:]
        elif fout[idx].find('=') >= 0:
	    configs.append(fout[idx][:fout[idx].find('=')].strip())
            fout[idx] = '$' + fout[idx].replace('\n', ';\n')
    fout.append('?>\n')
    open('../htdocs/config.php', 'w').writelines(fout)
    print


def write_jinja2_config_file():
    print "Writing Jinja2 config file."
    fout = open('../bin/config.py').readlines()
    fout[0] = '{# Generated file.  Do not modify. #}\n'
    for idx in range(1, len(fout)):
        if fout[idx][0] == '#':
            fout[idx] = '{# ' + fout[idx][1:] + fout[idx].replace('\n', ' #}\n')
        elif fout[idx].find('=') >= 0:
            fout[idx] = '{% set ' + fout[idx].replace('\n', ' %}\n')
    open('../templates/config.html', 'w').writelines(fout)
    print


if __name__ == '__main__':  # pragma: no cover
    pif = basics.get_page_info('editor', dbedit='')
    main(pif)
