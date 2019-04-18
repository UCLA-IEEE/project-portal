from app import db
from common.errors import ResourceExistsError, ResourceDoesNotExistError

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    project = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'project': self.project
        }

# Add test data
test_users = [
    User(name="robert", project="Micromouse"),
    User(name="maggie", project="OPS")
]

def does_user_exist(name):
    return User.query.filter_by(name=name).count() != 0

for user in test_users:
    if not does_user_exist(user.name):
        db.session.add(user)
        db.session.commit()

def create_user(name, project):
    if does_user_exist(name):
        raise ResourceExistsError

    new_user = User(name=name, project=project)
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