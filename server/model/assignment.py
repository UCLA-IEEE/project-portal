import sqlalchemy
import bcrypt

from app import db
from common.errors import ResourceExistsError, ResourceDoesNotExistError

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable="False")

    def __repr__(self):
        return '<Assignment %r>' % self.name
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content,
        }

def does_assignment_exist(name):
    return Assignment.query.filter_by(name=name).count() != 0

#for user in test_users:
    #if not does_user_exist(user.name):
        #db.session.add(user)
       # db.session.commit()

def create_assignment(name, content):
    if does_assignment_exist(name):
        raise ResourceExistsError

    new_assignment = Assignment(name=name, content=content)
    db.session.add(new_assignment)
    db.session.commit()
    return new_assignment

def get_all_assignments():
    return Assignment.query.all()

def get_assignment(name):
    if not does_assignment_exist(name):
        raise ResourceDoesNotExistError

    return Assignment.query.filter_by(name=name).first()

def delete_assignment(name):
    if not does_assignment_exist(name):
        raise ResourceDoesNotExistError
    
    assignment = Assignment.query.filter_by(name=name).first()
    db.session.delete(assignment)
    db.session.commit()

    return assignment