# -*- coding: utf-8 -*-

# models.py


# - Imports -
import logging

from google.appengine.ext import ndb
from google.appengine.api import memcache as mc


def flush_mc(keys=None):
	if not (type(keys) is str or type(keys) is list or keys is None):
		raise TypeError

	max_retries = 50

	if type(keys) is str:
		for _ in xrange(max_retries):
			if mc.delete(keys):
				break
		else:
			return False
	elif type(keys) is list:
		for _ in xrange(max_retries):
			if mc.delete_multi(keys):
				break
		else:
			return False
	else:
		for _ in xrange(max_retries):
			if mc.flush_all():
				break
		else:
			return False

	return True


# - Keys -
def model_key(kind, name='default'):
	return ndb.Key(kind, name)


# - Models -
class Data(ndb.Model):
	device_id = ndb.IntegerProperty(required=True)
	value = ndb.IntegerProperty(required=True)
	generated = ndb.DateTimeProperty(auto_now=True)

	@classmethod
	def get_data(cls, limit=50):
		data = mc.get('data')

		if not data:
			q = cls.query(ancestor=model_key(cls)).order(-cls.generated)
			data = q.fetch(limit)

			if data:
				data = list(data)
				mc.set('data', data)

		return data
