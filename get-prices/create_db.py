from app import db
from app.mod_item.models import Item,Price
from datetime import datetime

db.drop_all()
db.create_all()


item = Item('title1','link-test')

d = datetime.now()
price = Price(item.id,d,"100.99")
db.session.add(item)
item.prices.append(price)
db.session.commit()
