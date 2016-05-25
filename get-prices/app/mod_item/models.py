from app import db
from app.mod_base.models import Base

class Item(Base):
    __table_name__ = 'item'
    title = db.Column(db.String())
    domain = db.Column(db.String(),nullable=False)
    link = db.Column(db.Text, nullable=False,unique=True)
    prices = db.relationship('Price',backref='item',lazy='dynamic')

    def __init__(self, title, link,domain):
        self.title = title
        self.link = link
        self.domain = domain
    def __repr__(self):
        return '<Item:(%s,%s,%s)>' % (self.title,self.link,self.domain)
class Price(Base):
    __table_name__ = 'price'
    date_time = db.Column(db.DateTime(),nullable=False)
    price = db.Column(db.Float(),nullable=False)
    item_id = db.Column(db.Integer(),db.ForeignKey("item.id"))
    def __init__(self,item_id,date_time,price):
        self.item_id = item_id
        self.date_time = date_time
        self.price = price
    def __repr__(self):
        return '<Price %r,%r,%r>' % self.item_id,self.date_time,self.price
