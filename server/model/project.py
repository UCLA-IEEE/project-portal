from app import db
from common.errors import ResourceExistsError, ResourceDoesNotExistError

class Project(db.Model):
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Project %r>' % self.name
    
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description
        }

# Add test data
test_projects = [
    Project(name="OPS", description="circuits"),
    Project(name="Micromouse", project="autonomous maze-solving robot")
]

def does_project_exist(name):
    return Project.query.filter_by(name=name).count() != 0

for project in test_projects:
    if not does_project_exist(project.name):
        db.session.add(project)
        db.session.commit()

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

<<<<<<< HEAD
    return project
=======
return project
>>>>>>> 2b18dc803bbd26c6094352f2e31859c7437cc7dc
