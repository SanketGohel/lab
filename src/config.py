#src/config.py

import os

class Development(object):
	"""
	Development environment configuration
	"""
	DEBUG = True
	TESTING = False


class Production(object):
	"""
	Production environment configuration
	"""
	DEGUG = False
	TESTING = False

app_config = {
	'development' : Development,
	'production' : Production,	
}