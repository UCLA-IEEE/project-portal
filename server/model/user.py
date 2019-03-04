users = [
    {
        'name': 'rzalog',
        'project': 'Micromouse'
    },
    {
        'name': 'maggie',
        'project': 'OPS'
    }
]

def create_user(name, project):
    new_user = {
        'name': name,
        'project': project
    }
    users.append(new_user)
    return new_user

def get_all_users():
    return users

def get_user(name):
    for user in users:
        if user['name'] == name:
            return user