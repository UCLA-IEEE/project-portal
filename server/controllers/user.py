import model.user

def create_user(name, project):
    new_user = model.user.create_user(name, project)
    return new_user.to_dict()

def get_all_users():
    users = model.user.get_all_users()
    return [user.to_dict() for user in users]

def get_user(name):
    user = model.user.get_user(name)
    return user.to_dict()

def delete_user(name):
    user = model.user.delete_user(name)
    return user.to_dict()