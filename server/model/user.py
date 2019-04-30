import sqlalchemy
import bcrypt

from app import db
from common.errors import ResourceExistsError, ResourceDoesNotExistError, MissingFieldsError

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'role': self.role
        }

    def check_pw(self, raw):
        return bcrypt.checkpw(raw, self.password) == self.password

def does_user_exist(name):
    return User.query.filter_by(name=name).count() != 0

def create_user(user_data):
    try:
        if does_user_exist(user_data['username']):
            raise ResourceExistsError
    except KeyError:
        raise MissingFieldsError

    try:
        salt = bcrypt.getsalt()
        hashed = bcrypt.hashpw(data['password'])

        new_user = User(
            username=data['username'],
            email=data['email'],
            name=data['name'],
            role=['member'],
            password=hashed
        )
    except KeyError:
        raise MissingFieldsError
    
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_all_users():
    return User.query.all()

def get_user(name):
    if not does_user_exist(name):
        raise ResourceDoesNotExistError

    return User.query.filter_by(name=name).first()

def delete_user(name):
    if not does_user_exist(name):
        raise ResourceDoesNotExistError
    
    user = User.query.filter_by(name=name).first()
    db.session.delete(user)
    db.session.commit()

    return user