# -*- coding: utf-8 -*-

# gae-stdenv-plantilla handlers.py


# - Imports -
import webapp2
import logging

from models import *


# - Handlers -
class Index(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello, world! iot-ingest service')


class NewData(webapp2.RequestHandler):
	def put(self):
		device_id = self.request.get('device_id')
		data_value = self.request.get('data_value')

		error = False

		try:
			Data.validate_values(device_id, data_value)
		except ValueError:
			error = 'Device ID or data value errors'

		if not error:
			Data.generate_data(int(device_id), int(data_value))

			self.response.out.write('OK')
		else:
			self.error(400)

			self.response.out.write(error)
