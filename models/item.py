# import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):  #returns a JSON representation of a model(aka dictionary)
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #same as SELECT * FROM items WHERE name=name LIMIT 1. returns ItemModel object

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))  #(name,) is a tuple.
        # row = result.fetchone()
        # connection.close()
        #
        # if row:  #same as if row is not None
        #     return cls(*row) #returns each element in row list - row[0] and row[1]. parameter unpacking.

    def save_to_db(self):  #does upserting data. insert and update.
        db.session.add(self)
        db.session.commit()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO items VALUES(?, ?)"
        # cursor.execute(query, (self.name, self.price))
        # #items.append(item)  #appends the item dictionary to the end of items list.
        #
        # connection.commit()
        # connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "UPDATE items SET price=? WHERE name=?"
        # cursor.execute(query, (self.price, self.name))
        #
        # connection.commit()
        # connection.close()
