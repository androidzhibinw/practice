from flask import Blueprint,render_template,request

from app import db
from app.mod_item.forms import ItemForm
from app.mod_item.models import Item
mod_item = Blueprint('item', __name__, url_prefix='/item')

@mod_item.route('/all')
def items():
    return  render_template('item/all.html')

@mod_item.route('/new', methods=['GET','POST'])
def new_item():
    form = ItemForm()
    if request.method == 'POST' and form.validate_on_submit():
        item = Item(None,form.link.data)
        db.session.add(item)
        db.session.commit()
    return render_template('item/new.html',form=form)

@mod_item.route('/delete/<int:id>', methods=['POST'])
def del_item(id):
    return 'delete %d' %id

@mod_item.route('/update/<int:id>', methods=['GET','POST'])
def update_item(id):
    return 'update %d' % id

@mod_item.route('/view/<int:id>')
def view_item(id):
    return 'view post %d' % id
