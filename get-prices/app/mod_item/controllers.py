from flask import Blueprint, render_template, request, redirect

from app import app, db
from app.mod_item.forms import ItemForm
from app.mod_item.models import Item
from app.fetch import fetch_one
from app.domainutils import get_domain
mod_item = Blueprint('item', __name__, url_prefix='/')


@mod_item.route('/')
def items():
    items = Item.query.all()
    return render_template('item/all.html', items=items)


@mod_item.route('new', methods=['GET', 'POST'])
def new_item():
    form = ItemForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        domain = get_domain(form.link.data)
        if domain:
            app.logger.info('domain is:' + domain)
            # query before insert
            item_db = Item.query.filter(Item.link == form.link.data).first()
            if item_db is None:
                item = Item(None, form.link.data, domain, None)
                db.session.add(item)
                db.session.commit()
                fetch_one(item)
                return redirect('view/' + str(item.id))
            else:
                app.logger.info('item already have in db.')
                return redirect('view/' + str(item_db.id))
        else:
            app.logger.info('domain not support:' + form.link.data)
            error = "ulr not support"

    return render_template('item/new.html', form=form, error=error)


@mod_item.route('/delete/<int:id>', methods=['POST'])
def del_item(id):
    return 'delete %d' % id


@mod_item.route('/update/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    return 'update %d' % id


@mod_item.route('view/<int:id>')
def view_item(id):
    item = Item.query.filter(Item.id == id).first()
    if item:
        print item.link
    return render_template('item/item.html', item=item)
