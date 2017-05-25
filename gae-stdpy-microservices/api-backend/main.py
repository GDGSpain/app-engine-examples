# -*- coding: utf-8 -*-

# gae-stdenv-plantilla main.py

# - Imports -
import webapp2

from scripts.handlers import *

# - Handler mapping -
app = webapp2.WSGIApplication([('/', Index),
                               ('/api/v1/get_data', GetData)],
                              debug=True)
