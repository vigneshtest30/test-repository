import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))  #can give 80 to limit the variable size to this length.
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        #self.id = _id  #id is a python keyword. Hence using _id. self.id is fine.
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod   #class method because we are not using self object anywhere in the method
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() #returns the first row of username within user table
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()  #cursor needed to run the db commands in sqlite3
        #
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))  #query and parameters
        # row = result.fetchone()
        # if row:    #short form for if row is not None
        #     user = cls(*row)  #passing as set of positional arguments. same as row[0], row[1], row[2]
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod   #class method because we are not using self object anywhere in the method
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()  #cursor needed to run the db commands in sqlite3
        #
        # query = "SELECT * FROM users WHERE id=?"
        #
        #
        # result = cursor.execute(query, (_id,))  #query and parameters
        # row = result.fetchone()
        # if row:    #short form for if row is not None
        #     user = cls(*row)  #passing as set of positional arguments. same as row[0], row[1], row[2]
        # else:
        #     user = None
        #
        # connection.close()
        # return user
