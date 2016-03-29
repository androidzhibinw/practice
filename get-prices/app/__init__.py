from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from app.mod_item.controllers import mod_item

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

app.register_blueprint(mod_item)
@app.route('/')
def hello():
    return render_template('index.html')


