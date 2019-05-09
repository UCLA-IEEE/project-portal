import model.user

def create_user(data):
    new_user = model.user.create_user(data)
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

def add_completed_assignment(a_name, u_name):
    assignment = model.user.add_completed_assignment
    return assignment.to_dict()