from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.mod_item.models import Item
from app import db

#engine = create_engine('sqlite:///app.db')

#connection = engine.connect()

#result  = connection.execute('select * from item;');

result = Item.query.all()
print result


def query_item():
    return Item.query.all()








