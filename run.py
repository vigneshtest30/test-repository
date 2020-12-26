from app import app
from db import db

db.init_app(run)

@app.before_first_request
def create_tables():  #creates data.db and all the tables under it unless they already exists before the first request comes into this app.
    db.create_all()
