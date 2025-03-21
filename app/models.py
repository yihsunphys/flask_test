from flask import current_app
from flask_login import UserMixin
import jwt
from app import db, login


@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable = False)  
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>'% self.username
    
    def generate_reset_password_token(self, expires_in=600):
        return jwt.encode({'id': self.id}, current_app.config['SECRET_KEY'], algorithm='HS256')
    
    def check_reset_password_token(self, token):
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            User.query.filter_by(id=data['id']).first()
        except:
            return