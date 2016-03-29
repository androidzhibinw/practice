from app import db


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_create = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_update = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())


class Post(Base):
    __table_name__ = 'post'
    title = db.Column(db.String(), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content
    def __repr__(self):
        return  '<Post %r,%r>' % self.title,self.content
