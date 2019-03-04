import model.user

def create_assignment(name, content):
    new_assignment = model.user.create_assignment(name, content)
    return new_assignment

def get_all_assignments():
    assignments = model.user.get_all_assignments()
    return assignments

def get_assignment(name):
    assignment = model.user.get_assignment(name)
    return assignment

def create_user(name, project):
    new_user = model.user.create_user(name, project)
    return new_user

def get_all_users():
    users = model.user.get_all_users()
    return users

def get_user(name):
    user = model.user.get_user(name)
    return user

