from app import db
from app.mod_post.models import Item

db.drop_all()
db.create_all()


item = Item('title1','link-test')
db.session.add(item)
db.session.commit()
