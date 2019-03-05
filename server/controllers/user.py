import model.user

def create_user(name, project):
    new_user = model.user.create_user(name, project)
    return new_user

def get_all_users():
    users = model.user.get_all_users()
    return users

def get_user(name):
    user = model.user.get_user(name)
    return user

