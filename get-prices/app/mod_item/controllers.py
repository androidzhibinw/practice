from flask import Blueprint,render_template

mod_item = Blueprint('item', __name__, url_prefix='/item')

@mod_item.route('/all')
def items():
    return  render_template('item/all.html')

@mod_item.route('/new', methods=['GET','POST'])
def new_item():

    return render_template('item/new.html')

@mod_item.route('/delete/<int:id>', methods=['POST'])
def del_item(id):
    return 'delete %d' %id

@mod_item.route('/update/<int:id>', methods=['GET','POST'])
def update_item(id):
    return 'update %d' % id

@mod_item.route('/view/<int:id>')
def view_item(id):
    return 'view post %d' % id
