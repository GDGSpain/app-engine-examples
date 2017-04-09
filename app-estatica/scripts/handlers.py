# -*- coding: utf-8 -*-

# gae-stdenv-plantilla handlers.py


# - Imports -
import os
import webapp2
import jinja2
import logging


# - Initialize Jinja2 environment -
template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


# - Handlers -
class MainHandler(webapp2.RequestHandler):
	def render(self, template, params=None):
		if not params:
			params = {}

		t = jinja_env.get_template(template)

		self.response.out.write(t.render(params))


class StaticPage(MainHandler):
	def get(self):
		path = self.request.path[1:].replace('/', '-')

		logging.debug(path)

		if path == '':
			path = 'index'

		try:
			self.render('{}.html'.format(path))
		except jinja2.TemplateNotFound:
			self.error(404)

			self.render('error-404.html')
