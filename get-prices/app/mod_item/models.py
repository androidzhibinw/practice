from app import db
from app.mod_base.models import Base


class Item(Base):
    __table_name__ = 'item'
    title = db.Column(db.String())
    link = db.Column(db.Text, nullable=False,unique=True)

    def __init__(self, title, link):
        self.title = title
        self.link = link
    def __repr__(self):
        return  '<Item %r,%r>' % self.title,self.content
