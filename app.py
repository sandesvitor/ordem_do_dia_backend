from flask import Flask
from flask_restful import Api
from resources.users import Users, User


app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:user_id>')
 

if __name__ == '__main__': 
    app.run(debug=True)