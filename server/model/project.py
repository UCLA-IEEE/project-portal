projects = [
    {
        'name': 'OPS',
        'description': 'circuits'
    },
    {
        'name': 'micromouse',
        'description': 'autonomous maze-solving robot'
    }
]

def create_project(name, description):
    new_project = {
        'name': name,
        'description': description
    }
    projects.append(new_project)
    return new_project

def get_all_projects():
    return projects

def get_project(name):
    for project in projects:
        if project['name'] == name:
            return project