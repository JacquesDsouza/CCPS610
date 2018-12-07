from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from ccps610 import db
from ccps610.models import Post
from ccps610.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and not current_user.admin_flag :
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.post_category = form.post_category.data
        post.post_type = form.post_type.data
        #post.status = form.status.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.post_category.data = post.post_category 
        form.post_type.data = post.post_type 
        #form.status.data = post.status
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and not current_user.admin_flag:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))



@posts.route("/post/<int:post_id>/support", methods=['GET', 'POST'])
@login_required
def support_post(post_id):
    post = Post.query.get_or_404(post_id)
    count = post.support_count
    if post.author != current_user and not current_user.admin_flag :
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.support_count = count +1 
        #post.status = form.status.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.post_category.data = post.post_category 
        form.post_type.data = post.post_type 
        #form.status.data = post.status
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')



@posts.route("/browse_my_post")
@login_required
def browse_my_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(user_id=current_user.id).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('browse_my_post.html', title='Browse, Support and track User Content Feedback', posts=posts)
    
@posts.route("/browse_moderate")
@login_required
def browse_moderate():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(status='Draft').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('browse_moderate.html', title='Browse, Support and track User Content Feedback', posts=posts)
    