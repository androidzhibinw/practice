# -*- coding: utf-8 -*-
from app.mod_item.models import Item,Price
from app import db,app


def query_item():
    return Item.query.all()

def update_item_title(item_link,title=None):
    item = Item.query.filter(Item.link==item_link).first()
    app.logger.info('update_item_title')
    if item and title and (item.title is None):
        app.logger.info('update title' + title)
        item.title = title
        db.session.commit()

def save_price(item_link,price):
    item = Item.query.filter(Item.link==item_link).first()
    app.logger.info('save price')
    if item and price:
        app.logger.info('save price:' + str(price))
        p = Price(item.id,price)
        item.prices.append(p)
        db.session.commit()
