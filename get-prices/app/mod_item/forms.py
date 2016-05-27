# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class ItemForm(Form):
    link = StringField('',validators=[DataRequired()],render_kw={"placeholder": u"输入链接地址"})
