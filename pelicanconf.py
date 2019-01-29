#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Didier Villers'
SITENAME = 'Bonjour'
SITEURL = 'https://didiervillers.github.io'

USE_FOLDER_AS_CATEGORY = True

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
LANG = 'fr_BE.UTF-8'
LOCALE = 'fr_BE'

CC_LICENSE = 'CC-BY-SA'

TYPOGRIFY = True

COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = 2018

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Site professionnel', 'https://dvillers.umons.ac.be/wiki/start'),
         ('SDDS', 'https://sdds.umons.ac.be/wiki/start'),
         ('UMONS', 'http://umons.ac.be'),
         ('ASBL LoLiGrUB', 'http://www.loligrub.be'),
         ('Jeudis du Libre', 'http://jeudisdulibre.be'),)

# Social widget
SOCIAL_WIDGET_NAME = "Contact"
SOCIAL = (('Twitter', 'https://twitter.com/linusable'),
          ('Github', 'https://github.com/didiervillers'),
          ('Facebook', 'https://www.facebook.com/didier.villers'),
          ('LinkedIn', 'https://www.linkedin.com/in/didier-villers-7587976/'),)
TWITTER_USERNAME = 'linusable'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Specify name of a built-in theme
THEME = './themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'united'
SHARIFF = True
SHARIFF_TWITTER_VIA = True
SHARIFF_LANG = 'fr'
SHARIFF_ORIENTATION = 'horizontal'
SHARIFF_SERVICES = '[&quot;twitter&quot;,&quot;facebook&quot;,&quot;googleplus&quot;,&quot;info&quot;]'
SHARIFF_THEME = 'grey'

HIDE_SIDEBAR = True

# Specify plugins
PLUGIN_PATHS = ['./plugins', ]
PLUGINS = ['i18n_subsites' ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
