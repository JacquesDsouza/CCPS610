from flask import render_template, request, Blueprint
from ccps610.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(status='Approved').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/browse")
def browse():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(status='Pending Approval').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('browse.html', title='Browse, Support and track User Content Feedback', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
