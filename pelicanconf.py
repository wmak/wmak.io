#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'William Mak'
SITENAME = u':(){:|:&};:'
#SITEURL = 'http://wmak.io'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll

# Social widget
SOCIAL = (
        ('github', 'https://github.com/wmak'),
        ('google', 'https://plus.google.com/u/0/+WilliamMak'),
        ('LinkedIn', 'http://www.linkedin.com/pub/william-mak/66/b1b/a52'),
        ('resume', SITEURL + '/content/resume.pdf'),
        )

DEFAULT_PAGINATION = 10

GOOGLE_ANALYTICS = "UA-48091655-1"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./theme"

STATIC_PATHS = ['images', 'extra/CNAME', 'content', 'selenate.html']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
