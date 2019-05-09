import model.project

def create_project(name, description):
    new_project = model.project.create_project(name, description)
    return new_user.to_dict()

def get_all_projects():
    projects = model.project.get_all_projects()
    return [project.to_dict() for project in projects]

def get_project(name):
    project = model.project.get_project(name)
    return project.to_dict()

def delete_project(name):
    project = model.project.delete_project(name)
    return project.to_dict()