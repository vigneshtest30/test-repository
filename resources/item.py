# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):  #Item class inherits Resource class
    parser = reqparse.RequestParser()
    parser.add_argument('price',
       type = float,
       required = True,
       help = "This field cannot be left blank!"
    )
    parser.add_argument('store_id',
       type = int,
       required = True,
       help = "Every item needs a store id."
    )

    @jwt_required()
    def get(self,name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        #item = next(filter(lambda x: x['name'] == name, items), None)  #next gives the first item found by the lambda function. filter creates a filter object out of it. If nothing found returns None.
        #return {'item': item}, 200 if item else 404  #return 200 RC if item exists else return 404. this is turnary operator.
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404  #404 is http item not found RC

    def post(self,name):
        #data = request.get_json(force=True)  #force=True makes it work even if content type is not set in POSTMAN
        #data = request.get_json(silent=True) #silent=True does not throw an error even if there is.. and just returns None.
        #if next(filter(lambda x:x['name'] == name,items), None):
            #return {'message': "An item with name '{}' already exists.".format(name)}, 400  #400 is bad request

        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400  #http 400 bad request RC

        data = Item.parser.parse_args()

        item = ItemModel(name, **data) #**data is parameter unpacking
        try:
            item.save_to_db()
        except:
            return {"message": "An error occured inserting the item."}, 500 #500 is html RC for internal server error

        return item.json(), 201  #http create success return code '201'

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}
        # global items  #to inform python the next overwrite is for global items variable.
        # items = list(filter(lambda x: x['name'] != name, items)) #overwrite all elements except the item passed.
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query, (name,))  #(name,) is the tuple
        #
        # connection.commit()
        # connection.close()
        # return {'message': 'Item deleted'}

    def put(self, name):
        #data = request.get_json()
        data = Item.parser.parse_args()
        #print(data['another'])
        # item = next(filter(lambda x:x['name'] == name,items), None)
        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])

        if item is None:
            item = ItemModel(name, **data) #**data is parameter unpacking
            # try:
            #     updated_item.insert()
            # except:
            #     return {"message": "An error occured inserting the item."}, 500
        else:
            item.price = data['price']

        item.save_to_db()
            # try:
            #     updated_item.update()
            # except:
            #     return {"message": "An error occured updating the item."}, 500
        return item.json()


class ItemList(Resource):
    def get(self):
        #return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))} #map() is mapping of function to elements.
        return {'items': [item.json() for item in ItemModel.query.all()]} #pull all items and return it in json format.list comprehension.
        # return {'items': items}
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        #
        # items = []
        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})
        #
        # connection.close()
        # return {'items': items}
