from app import db
from common.errors import ResourceExistsError, ResourceDoesNotExistError
from model.assignment import Assignment, does_assignment_exist

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    assignments = db.relationship('Assignment', backref='project', lazy=True)
    def __repr__(self):
        return '<Project %r>' % self.name
    
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description
        }

def does_project_exist(name):
    return Project.query.filter_by(name=name).count() != 0

# for project in test_projects:
#     if not does_project_exist(project.name):
#         db.session.add(project)
#         db.session.commit()

def create_project(name, description):
    if does_project_exist(name):
        raise ResourceExistsError

    new_project = Project(name=name, description=description)
    db.session.add(new_project)
    db.session.commit()
    return new_project

def get_all_projects():
    return Project.query.all()

def get_project(name):
    if not does_project_exist(name):
        raise ResourceDoesNotExistError

    return Project.query.filter_by(name=name).first()

def delete_project(name):
    if not does_project_exist(name):
        raise ResourceDoesNotExistError
    
    project = Project.query.filter_by(name=name).first()
    db.session.delete(project)
    db.session.commit()

    return project

def add_assignment(p_name, a_name):
    if not does_assignment_exist(a_name):
        raise ResourceDoesNotExistError
    project = Project.query.filter_by(name=p_name).first()
    assignment = Assignment.query.filter_by(name=a_name).first()

    project.assignments.append(assignment)
    return assignment
    