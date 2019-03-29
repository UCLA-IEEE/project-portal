import model.project

def create_project(name, description):
    new_project = model.project.create_project(name, description)
    return new_project

def get_all_projects():
    projects = model.projects.get_all_projects()
    return projects

def get_project(name):
    project = model.project.get_project(name)
    return project