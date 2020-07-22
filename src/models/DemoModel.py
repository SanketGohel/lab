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

		return 'Record has been added Sucessfully'


	# Searching for single User with ID Parameter
	def get_user(self,id):
		if id in d.keys():
			return d.get(id)
		else:
			return 'Key not Found'

	# Return all the users
	def get_users(self):
		return d



	# Removing single user with the ID 
	def del_user(self,id):
		
		if id in d.keys():
			d.pop(id)
			return 'Record has been removed from the database'
		else:
			return 'Key not Found'

	def update_user(self,record):

		if record['id'] in d.keys():
			if 'first_name' in record.keys():
				d[record['id']]['first_name'] = record['first_name']
			if 'last_name' in record.keys():	
				d[record['id']]['last_name'] = record['last_name'] 
			if 'phone' in record.keys():
				d[record['id']]['phone'] = record['phone']

			return 'New Value has been updated'
		else:
			return 'Key not Found'





			



