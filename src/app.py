#src/app.py


from flask import Flask,request,json,Response
from .config import app_config
from .models import DemoModel as dm






def create_app(env_name):
	"""
	Create app
	"""

	#app initialization 
	app = Flask(__name__)
	app.config.from_object(app_config[env_name])


	#Creating Endpoint for getting single User Methods = GET
	@app.route('/user/<int:id>',methods =['GET'])
	def index(id):
		"""
		Single User
	
		"""
		user = dm.DemoModel()
		if id:
			res = user.get_user(id) #checking for single user with id
			return custom_response(res,200)
		else:
			return custom_response("Please provide the ID",201)



	#Creating Endpoint for getting all the users Methods = GET
	@app.route('/users/',methods =['GET'])
	def get_all_users():
		"""
		Multiple User

		"""
		users = dm.DemoModel()
		res = users.get_users()

		return custom_response(res,200)


		
    
	#Creating Endpoint for inserting the user Methods = POST
	@app.route('/add/',methods =['POST'])
	def create():
		"""
		Inserting 4 Parameters 'id', 'first_name','last_name', 'phone'

		"""
		values = dm.DemoModel()
		cre_data = request.get_json()

		print(cre_data)
		res = values.add(cre_data)

		return custom_response(res,200)

	# @app.route('/',methods =['PUT'])
	# def put():
	# 	"""
	# 	example endpoint

	# 	"""
	# 	return 'Conguratulation! Your second endpoint is working'

	@app.route('/me',methods =['DELTE'])
	def delete():
		"""
		Removing single user

		"""
		user = dm.DemoModel()
		res = 


	def custom_response(res, status_code):

		"""
		Custom Response Function
		"""
		return Response(
			mimetype="application/json",
		    response=json.dumps(res),
		    status=status_code
		)



	return app