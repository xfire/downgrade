#!/usr/bin/env python
#
# vim:syntax=python:sw=4:ts=4:expandtab

class Link(object):

    def __init__(self, name, url):
        self.name = name
        self.url = url


projects = [ Link('growl',       'https://github.com/xfire/growl/tree'),
             Link('pydzen',      'https://github.com/xfire/pydzen/tree'),
             Link('python-wmii', 'https://github.com/xfire/python-wmii/tree'),
             Link('preplace',    'https://github.com/xfire/preplace/tree'),
             Link('jitertools',  'https://github.com/xfire/jitertools/tree'),
             Link('mailfilter',  'http://projects.spamt.net/mailfilter/'),
           ]

links = [ Link('github',             'http://github.com/xfire/'),
          Link('dotfiles',           'https://github.com/xfire/dotfiles/tree'),
          Link("copton's blog",      'http://blog.copton.net/'),
          Link("copton's ethz blog", 'http://blogs.ethz.ch/copton/'),
          Link("schula's blog",      'http://blog.spamt.net/'),
          Link("freaky's blog",      'http://www.freakysoft.de/blog/'),
        ]

updates = AttrDict(projects = projects, links = links)

if not 'site' in Site.CONTEXT:
    Site.CONTEXT.site = updates
else:
    Site.CONTEXT.site.update(updates)
