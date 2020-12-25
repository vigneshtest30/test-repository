import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()  #parser used to parse the incoming JSON request
    parser.add_argument('username',
       type=str,
       required=True,
       help="This field cannot be blank."
       )

    parser.add_argument('password',
       type=str,
       required=True,
       help="This field cannot be blank."
       )

    def post(self):
        data = UserRegister.parser.parse_args()  #to use the parser

        if UserModel.find_by_username(data['username']):   #same as if User.find_by_username(data['username']) is not None
            return {"message": "A user with that name already exists"}, 400   #400 is bad http RC

        user = UserModel(**data) #**data is same as data['user'], data['password']..parameter unpacking..
        user.save_to_db()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO users VALUES(NULL, ?, ?)"  #user id is auto incremented. hence null.
        # cursor.execute(query, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()

        return {"message": "User created successfully."}, 201
