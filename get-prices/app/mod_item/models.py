# -*- coding:utf-8 -*-
from app import db
from app.mod_base.models import Base

class Item(Base):
    __table_name__ = 'item'
    title = db.Column(db.String())
    domain = db.Column(db.String(),nullable=False)
    link = db.Column(db.Text, nullable=False,unique=True)
    current_price = db.Column(db.Float())
    prices = db.relationship('Price',backref='item',lazy='dynamic')

    def __init__(self, title, link,domain,cur_price):
        self.title = title
        self.link = link
        self.domain = domain
        self.current_price = cur_price
    def __repr__(self):
        return '<Item:(%s,%s,%s)>' % (self.title,self.link,self.domain)
class Price(Base):
    __table_name__ = 'price'
    price = db.Column(db.Float(),nullable=False)
    item_id = db.Column(db.Integer(),db.ForeignKey("item.id"))
    def __init__(self,item_id,price):
        self.item_id = item_id
        self.price = price
    def __repr__(self):
        return '<Price (%r,%r)>' % (self.item_id,self.price)
