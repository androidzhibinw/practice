from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from app.mod_post.controllers import mod_post

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

app.register_blueprint(mod_post)
@app.route('/')
def hello():
    return render_template('index.html')


