#!/usr/local/bin/python

import datetime, os, sys
import logging
import logging.config
import config

crawlers = [  # precluded from normal url tracking
    'Aboundex/0.3 (http://www.aboundex.com/crawler/)',
    'BacklinkCrawler (http://www.backlinktest.com/crawler.html)',
    'CCBot/2.0 (http://commoncrawl.org/faq/)',
    'Curious George - www.analyticsseo.com/crawler',
    'DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)',
    'Domain Re-Animator Bot (http://domainreanimator.com) - support@domainreanimator.com',
    'GG PeekBot 2.0 ( http://gg.pl/ http://info.gadu-gadu.pl/praca )',
    'GarlikCrawler/1.2 (http://garlik.com/, crawler@garlik.com)',
    'Googlebot/2.1 (+http://www.google.com/bot.html)',
    'Java/1.6.0_04',
    'Java/1.8.0_40',
    'Kyoto-Tohoku-Crawler/v1 (Mozilla-compatible; kyoto-crawler-contact@nlp.ist.i.kyoto-u.ac.jp; http://nlp.ist.i.kyoto-u.ac.jp/?crawling-kt)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0 ; Claritybot)',
    'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1; +http://www.apple.com/go/applebot)',
    'Mozilla/5.0 (TweetmemeBot/4.0; +http://datasift.com/bot.html) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 6.1) (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)',
    'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko (compatible; Zombiebot/2.1; +http://www.zombiedomain.net/robot/)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6 - James BOT - WebCrawler http://cognitiveseo.com/bot.html',
    'Mozilla/5.0 (compatible; 007ac9 Crawler; http://crawler.007ac9.net/)',
    'Mozilla/5.0 (compatible; AhrefsBot/5.0; +http://ahrefs.com/robot/)',
    'Mozilla/5.0 (compatible; AhrefsBot/5.1; +http://ahrefs.com/robot/)',
    'Mozilla/5.0 (compatible; AhrefsBot/5.1; +http://ahrefs.com/robot/)',
    'Mozilla/5.0 (compatible; AhrefsBot/5.2; +http://ahrefs.com/robot/)',
    'Mozilla/5.0 (compatible; Applebot/0.3; +http://www.apple.com/go/applebot)',
    'Mozilla/5.0 (compatible; BLEXBot/1.0; +http://webmeup-crawler.com/)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; Cliqzbot/1.0 +http://cliqz.com/company/cliqzbot)',
    'Mozilla/5.0 (compatible; DeuSu/5.0.2; +https://deusu.de/robot.html)',
    'Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)',
    'Mozilla/5.0 (compatible; Findxbot/1.0; +http://www.findxbot.com)',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://import.io)',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; GrapeshotCrawler/2.0; +http://www.grapeshot.co.uk/crawler.php)',
    'Mozilla/5.0 (compatible; IstellaBot/1.23.15 +http://www.tiscali.it/)',
    'Mozilla/5.0 (compatible; LinkpadBot/1.07; +http://www.linkpad.ru)',
    'Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/2.0; +http://go.mail.ru/help/robots)',
    'Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)',
    'Mozilla/5.0 (compatible; MJ12bot/v1.4.7; http://mj12bot.com/)',
    'Mozilla/5.0 (compatible; MegaIndex.ru/2.0; +http://megaindex.com/crawler)',
    'Mozilla/5.0 (compatible; MetaJobBot; http://www.metajob.de/crawler)',
    'Mozilla/5.0 (compatible; MixrankBot; crawler@mixrank.com)',
    'Mozilla/5.0 (compatible; NetSeer crawler/2.0; +http://www.netseer.com/crawler.html; crawler@netseer.com)',
    'Mozilla/5.0 (compatible; Plukkie/1.6; http://www.botje.com/plukkie.htm)',
    'Mozilla/5.0 (compatible; RSSMicro.com RSS/Atom Feed Robot)',
    'Mozilla/5.0 (compatible; SEOdiver/1.0; +http://www.seodiver.com/bot)',
    'Mozilla/5.0 (compatible; SEOkicks-Robot; +http://www.seokicks.de/robot.html)',
    'Mozilla/5.0 (compatible; SemrushBot/0.99~bl; +http://www.semrush.com/bot.html)',
    'Mozilla/5.0 (compatible; SemrushBot/1.1~bl; +http://www.semrush.com/bot.html)',
    'Mozilla/5.0 (compatible; SemrushBot/1.2~bl; +http://www.semrush.com/bot.html)',
    'Mozilla/5.0 (compatible; SemrushBot/1~bl; +http://www.semrush.com/bot.html)',
    'Mozilla/5.0 (compatible; SemrushBot/1~bl; +http://www.semrush.com/bot.html)',
    'Mozilla/5.0 (compatible; SeznamBot/3.2-test1; +http://fulltext.sblog.cz/)',
    'Mozilla/5.0 (compatible; SeznamBot/3.2; +http://fulltext.sblog.cz/)',
    'Mozilla/5.0 (compatible; WBSearchBot/1.1; +http://www.warebay.com/bot.html)',
    'Mozilla/5.0 (compatible; XoviBot/2.0; +http://www.xovibot.net/)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)',
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; linkdexbot/2.0; +http://www.linkdex.com/bots/)',
    'Mozilla/5.0 (compatible; linkdexbot/2.2; +http://www.linkdex.com/bots/)',
    'Mozilla/5.0 (compatible; spbot/4.4.2; +http://OpenLinkProfiler.org/bot )',
    'Mozilla/5.0 (compatible; spbot/5.0.1; +http://OpenLinkProfiler.org/bot )',
    'Mozilla/5.0 (compatible; spbot/5.0.2; +http://OpenLinkProfiler.org/bot )',
    'Mozilla/5.0 (compatible; spbot/5.0.3; +http://OpenLinkProfiler.org/bot )',
    'Mozilla/5.0 (compatible; spbot/5.0; +http://OpenLinkProfiler.org/bot )',
    'Mozilla/5.0 (compatible; yoozBot-2.2; http://yooz.ir; info@yooz.ir)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Applebot/0.3; +http://www.apple.com/go/applebot)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; bingbot/2.0;  http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    'NextGenSearchBot 1 (for information visit http://www.zoominfo.com/About/misc/NextGenSearchBot.aspx)',
    'Personal Private Crawler; You can block this crawler by the UserAgent; regex(PPC2938731);',
    'SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)',
    'SafeAds.xyz bot',
    'SafeDNS search bot/Nutch-1.9 (https://www.safedns.com/searchbot; support [at] safedns [dot] com)',
    'SafeDNSBot (https://www.safedns.com/searchbot)',
    'SafeSearch microdata crawler (https://safesearch.avira.com, safesearch-abuse@avira.com)',
    'SiteSucker/2.4.6',
    'Spiderbot/Nutch-1.7',
    'TurnitinBot (https://turnitin.com/robot/crawlerinfo.html)',
    'Wotbox/2.01 (+http://www.wotbox.com/bot/)',
    'Y!J-ASR/0.1 crawler (http://www.yahoo-help.jp/app/answers/detail/p/595/a_id/42716/)',
    'betaBot',
    'bhcBot',
    'crawler4j (http://code.google.com/p/crawler4j/)',
    'ia_archiver',
    'istellabot-nutch/Nutch-1.10',
    'istellabot/Nutch-1.10',
    'istellabot/Nutch-1.10',
    'istellabot/Nutch-1.11',
    'istellabot/t.1',
    'istellabot/t.1',
    'linkapediabot (+http://www.linkapedia.com)',
    'msnbot/2.0b (+http://search.msn.com/msnbot.htm)',
    'tbot-nutch/Nutch-1.10',
    'webcrawler101/Nutch-1.9',

]

# you were looking for pretty?  hah.
class Logger(object):
    def __init__(self):
	logdate = datetime.datetime.now().strftime('%Y%m')

	env = config.ENV
	LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'single': {
            'format': '%(asctime)s [%(process)d] %(levelname)s ' + str(config.USER_ID) + ' - %(message)s',
        },
        'serious': {
            'format': '%(asctime)s [%(process)d] %(levelname)s ' + str(config.USER_ID) + ' %(filename)s:%(lineno)d - %(message)s',
        },
        'informational': {
            'format': '%(asctime)s %(levelname)s ' + str(config.USER_ID) + ' - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'informational'
        },
        'file': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'formatter': 'informational',
            'class': 'logging.FileHandler',
            'filename': '/home/bamca/logs/' + env + '.file.log',
        },
        'upload': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'formatter': 'informational',
            'class': 'logging.FileHandler',
            'filename': '/home/bamca/logs/' + env + '.upload.log',
        },
        'url': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'formatter': 'serious',
            'class': 'logging.FileHandler',
            'filename': '/home/bamca/logs/' + env + '.url' + logdate + '.log',
        },
        'dbq': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'formatter': 'single',
            'class': 'logging.FileHandler',
            'filename': '/home/bamca/logs/' + env + '.dbq' + logdate + '.log',
        },
        'bot': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'formatter': 'serious',
            'class': 'logging.FileHandler',
            'filename': '/home/bamca/logs/' + env + '.bot' + logdate + '.log',
        },
        'count': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'formatter': 'informational',
            'class': 'logging.FileHandler',
            'filename': '/home/bamca/logs/' + env + '.count.log',
        },
        'refer': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'formatter': 'informational',
            'class': 'logging.FileHandler',
            'filename': '/home/bamca/logs/' + env + '.refer.log',
        },
        'debug': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'formatter': 'serious',
            'class': 'logging.FileHandler',
            'filename': '/home/bamca/logs/' + env + '.debug.log',
        },
        'root': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'formatter': 'serious',
            'class': 'logging.FileHandler',
            'filename': '/home/bamca/logs/' + env + '.root.log',
        },
    },
    'loggers': {
        'console': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'file': {
            'level': 'INFO',
            'handlers': ['file'],
            'propagate': False,
        },
        'upload': {
            'level': 'INFO',
            'handlers': ['upload'],
            'propagate': False,
        },
        'url': {
            'level': 'INFO',
            'handlers': ['url'],
            'propagate': False,
        },
        'dbq': {
            'level': 'INFO',
            'handlers': ['dbq'],
            'propagate': False,
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['bot'],
            'propagate': False,
        },
        'count': {
            'level': 'INFO',
            'handlers': ['count'],
            'propagate': False,
        },
        'refer': {
            'level': 'INFO',
            'handlers': ['refer'],
            'propagate': False,
        },
        'debug': {
            'level': 'INFO',
            'handlers': ['debug'],
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['root'],
        'level': os.environ.get('LOG_LEVEL', 'DEBUG'),
    },
}

	logging.config.dictConfig(LOGGING)

        self.console	= logging.getLogger('console')
        self.file	= logging.getLogger('file')
        self.upload	= logging.getLogger('upload')
        self.url	= logging.getLogger('url')
        self.dbq	= logging.getLogger('dbq')
        self.bot	= logging.getLogger('bot')
        self.count	= logging.getLogger('count')
        self.refer	= logging.getLogger('refer')
        self.debug	= logging.getLogger('debug')
	self.root	= logging.getLogger('root')
