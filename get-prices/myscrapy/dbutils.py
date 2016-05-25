# -*- coding: utf-8 -*-
from app.mod_item.models import Item
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
