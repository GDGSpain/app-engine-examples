# -*- coding: utf-8 -*-

# gae-stdenv-plantilla handlers.py


import json

# - Imports -
import webapp2

from models import *


class DateTimeEncoder(json.JSONEncoder):
	def default(self, obj):
		if hasattr(obj, 'isoformat'):
			return obj.isoformat()
		else:
			return json.JSONEncoder.default(self, obj)


# - Handlers -
class MainHandler(webapp2.RequestHandler):
	def render_json(self, dict_list):
		if type(dict_list) is not list:
			dict_list = [dict_list]

		res = json.dumps([d for d in dict_list], cls=DateTimeEncoder)

		self.response.headers['Content-Type'] = 'application/json'

		self.response.out.write(res)


class Index(MainHandler):
	def get(self):
		self.response.out.write('Hello, world! api-backend service')


class GetData(MainHandler):
	def get(self):
		data = Data.get_data()

		data_dict = [d.to_dict() for d in data] if data else None

		self.render_json(data_dict)
