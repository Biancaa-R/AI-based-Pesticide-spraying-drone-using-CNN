from flask_1 import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    db.relationship('Post',backref='author',lazy=True)
    #additional query in background

    def __repr__(self):
        return f"User('{self.username},'{self.email}','{self.image_file}')"
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    date_posted=db.Column(db.Date,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    #table name and the column name
    def __repr__(self):
        return f"Post('{self.username},'{self.email}','{self.image_file}')"