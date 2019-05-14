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
            # 'assignments': [assignment.name for assignment in self.assignments]
        }

    def check_pw(self, raw):
        return bcrypt.checkpw(raw, self.password) == self.password

def does_user_exist(username):
    return User.query.filter_by(username=username).count() != 0

def create_user(user_data):
    try:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(user_data['password'].encode('utf-8'), salt)

        new_user = User(
            username=user_data['username'],
            email=user_data['email'],
            name=user_data['name'],
            role=user_data['role'],
            password=hashed
        )
    except KeyError:
        raise MissingFieldsError
    
    try:
        db.session.add(new_user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        raise ResourceExistsError

    return new_user

def get_all_users():
    return User.query.all()

def get_user(username):
    if not does_user_exist(username):
        raise ResourceDoesNotExistError

    return User.query.filter_by(username=username).first()

def delete_user(username):
    if not does_user_exist(username):
        raise ResourceDoesNotExistError
    
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()

    return user