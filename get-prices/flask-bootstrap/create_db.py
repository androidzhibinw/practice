from app import db
from app.mod_post.models import Post

db.drop_all()
db.create_all()


post = Post('title1','body1')
db.session.add(post)
db.session.commit()
