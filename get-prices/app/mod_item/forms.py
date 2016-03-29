from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class ItemForm(Form):
    link = StringField('link',validators=[DataRequired()])
