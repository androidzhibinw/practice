from flask import Blueprint,render_template,request

from app import app,db
from app.mod_item.forms import ItemForm
from app.mod_item.models import Item
mod_item = Blueprint('item', __name__, url_prefix='/')

@mod_item.route('/')
def items():
    items = Item.query.all()
    return  render_template('item/all.html',items=items)

@mod_item.route('/new', methods=['GET','POST'])
def new_item():
    form = ItemForm()
    if request.method == 'POST' and form.validate_on_submit():
        #query before insert
        item_db= Item.query.filter(Item.link == form.link.data).first()
        if item_db is None:
            item = Item(None,form.link.data)
            db.session.add(item)
            db.session.commit()
        else:
            app.logger.info('item already have in db.')

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
