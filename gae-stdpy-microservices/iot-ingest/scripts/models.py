# -*- coding: utf-8 -*-

# models.py


# - Imports -
import logging

from google.appengine.ext import ndb
from google.appengine.api import memcache as mc


# - Keys -
def model_key(kind, name='default'):
	return ndb.Key(kind, name)


# - Models -
class Data(ndb.Model):
	device_id = ndb.IntegerProperty(required=True)
	value = ndb.IntegerProperty(required=True)
	generated = ndb.DateTimeProperty(auto_now=True)

	@classmethod
	def validate_values(cls, device_id, value):
		try:
			device_id = int(device_id)
			value = int(value)
		except ValueError:
			raise ValueError

		if not value or type(value) is not int or value > 1000:
			raise ValueError

		return True

	@classmethod
	def generate_data(cls, device_id, value):
		d = cls(device_id=device_id,
		        value=value,
		        parent=model_key(cls))
		d.put()

		mc.delete('data')

		return d
