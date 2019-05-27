import model.user

def create_user(data):
    new_user = model.user.create_user(data)
    return new_user.to_dict()

def get_all_users():
    users = model.user.get_all_users()
    return [user.to_dict() for user in users]

def get_user(username):
    user = model.user.get_user(username)
    return user.to_dict()

def delete_user(username):
    user = model.user.delete_user(username)
    return user.to_dict()
