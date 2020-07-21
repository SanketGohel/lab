#src/models/DemoModel

class DemoModel():

	"""
	DemoModel methods POST = add(inserting Data), GET = get_user(single user) ,get_users(multiple user) 

	"""
	global d
	d= {}	

	#Inserting the data and 
	def add(self,record):

		d[record['id']] = record

		return d


	# Searching for single User with ID Parameter
	def get_user(self,id):
		if id in d.keys():
			return d.get(id)
		else:
			return 'Key not found'

	# Return all the users
	def get_users(self):
		return d



	# Removing single user with the ID 
	def del_user(self):
		if id in d.keys():
			



