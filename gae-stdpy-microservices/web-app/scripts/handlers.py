# -*- coding: utf-8 -*-

# gae-stdenv-plantilla handlers.py


# - Imports -
import webapp2
import os
import jinja2
import json
import logging

from google.appengine.api import urlfetch


# API_URL = 'http://api-backend.codelab-test-mmog.appspot.com/api/v1/get_data'
API_URL = 'http://localhost:8081/api/v1/get_data'


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


class Index(MainHandler):
	def get(self):
		self.response.out.write('Hello, world! web-app service')


class ShowData(MainHandler):
	def get(self):
		error = ''

		try:
			res = urlfetch.fetch(API_URL)
			if res.status_code == 200:
				data_json = res.content
			else:
				self.response.status_int = res.status_code

				error = 'Se ha producido un error en la respuesta del servicio'
		except urlfetch.Error:
			self.error(500)

			error = 'Se ha producido un error en la conexion del servicio'

		if not error:
			data = json.loads(data_json)

			params = {'data': [{'device_id': d.get('device_id'),
			                    'value': d.get('value'),
			                    'generated': d.get('generated')} for d in data]}

			self.render('show_data.html', params)
		else:
			self.response.out.write(error)


class Error404(MainHandler):
	def get(self):
		self.error(404)

		self.render('error_404.html')
