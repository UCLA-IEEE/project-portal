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
    completed_assignments = db.relationship('Assignment', backref = 'user', lazy=True)

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

<<<<<<< HEAD
    def check_pw(self, raw):
        return bcrypt.checkpw(raw, self.password) == self.password
=======
# Add test data
#test_users = [
#   User(name="robert", project="Micromouse"),
#    User(name="maggie", project="OPS")
#]
>>>>>>> 785113f83912cf5ba918efa93a4b770b5687a46e

def does_user_exist(name):
    return User.query.filter_by(name=name).count() != 0

<<<<<<< HEAD
def create_user(user_data):
    try:
        if does_user_exist(user_data['username']):
            raise ResourceExistsError
    except KeyError:
        raise MissingFieldsError

    try:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(data['password'])
=======
#for user in test_users:
    #if not does_user_exist(user.name):
        #db.session.add(user)
       # db.session.commit()
>>>>>>> 785113f83912cf5ba918efa93a4b770b5687a46e

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

def add_completed_assignment(u_name, a_name):
    if not does_user_exist(name):
        raise ResourceDoesNotExistError
    
    a = Assignment(name=a_name, user=u_name)
    user = User.query.filter_by(name=u_name).first();
    user.completed_assignments.append(a);

    return a