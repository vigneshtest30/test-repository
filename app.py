import os   #this gives access to operating system environment variables
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
#from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') #if the environment variable with the DB details not found then use the default sqllite value.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to turn off flask sqlalchemy change tracker so that our app consumes less resources. This can be tracked directly by sqlalchemy tracker.
app.secret_key = 'Jose'
api = Api(app)

# @app.before_first_request
# def create_tables():  #creates data.db and all the tables under it unless they already exists before the first request comes into this app.
#     db.create_all()

jwt = JWT(app,authenticate, identity)  #/auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
#api.add_resource is same as @app.route.

if __name__ == '__main__':  #used so that when app.py is imported by other progs the below statement will not run
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)  #debug=True gives a nice html page which helps in debugging errors
