from app import db
from app.mod_item.models import Item,Price
from datetime import datetime

db.drop_all()
db.create_all()


item = Item(None,'http://item.jd.com/1856581.html','jd')

d = datetime.now()
price = Price(item.id,d,"100.99")
db.session.add(item)
item.prices.append(price)
db.session.commit()
