from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from ccps610 import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    firstname = db.Column(db.String(30), unique=True, nullable=False)
    lastname = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    usertype = db.Column(db.String(60), nullable=False, default='User')
    admin_flag = db.Column(db.String(60), nullable=False, default=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # Create a token that expires in 30 mins. The token will be used to 
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.usertype}', '{self.adminflag}', '{self.firstname}', '{self.lastname}')"


class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    post_category = db.Column(db.String(20), nullable=False, default="Not Applicable")
    post_type = db.Column(db.String(20), nullable=False, default ="Gaming")
    status = db.Column(db.String(10), nullable=False, default="Draft")
    support_count = db.Column(db.Integer, nullable=False, default=0)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.post_category}', '{self.post_type}', '{self.status}', '{self.support_count}')"   