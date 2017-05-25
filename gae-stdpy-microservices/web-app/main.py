# -*- coding: utf-8 -*-

# gae-stdenv-plantilla main.py

# - Imports -
import webapp2

from scripts.handlers import *

# - Handler mapping -
app = webapp2.WSGIApplication([('/', Index),
                               ('/show_data', ShowData),
                               ('/.*', Error404)],
                              debug=True)
