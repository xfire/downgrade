#!/usr/bin/env python
#
# vim:syntax=python:sw=4:ts=4:expandtab

class Link(object):

    def __init__(self, name, url):
        self.name = name
        self.url = url


links = [ Link('github',             'http://github.com/xfire/'),
          Link('dotfiles',           'https://github.com/xfire/dotfiles/tree'),
          Link("copton's blog",      'http://blog.copton.net/'),
          Link("copton's ethz blog", 'http://blogs.ethz.ch/copton/'),
          Link("schula's blog",      'http://blog.spamt.net/'),
          Link("freaky's blog",      'http://www.freakysoft.de/blog/'),
        ]

if not 'site' in Site.CONTEXT:
    Site.CONTEXT.site = AttrDict(links = links)
else:
    Site.CONTEXT.site.links = links
