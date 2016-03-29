from flask import Blueprint,render_template

mod_post = Blueprint('post', __name__, url_prefix='/post')

@mod_post.route('/all')
def posts():
    return  render_template('post/all.html')

@mod_post.route('/new', methods=['GET','POST'])
def new_post():

    return render_template('post/new.html')

@mod_post.route('/delete/<int:id>', methods=['POST'])
def del_post(id):
    return 'delete %d' %id

@mod_post.route('/update/<int:id>', methods=['GET','POST'])
def update_post(id):
    return 'update %d' % id

@mod_post.route('/view/<int:id>')
def view_post(id):
    return 'view post %d' % id
