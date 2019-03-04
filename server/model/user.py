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

assignment = [
    {
        'name': "arduino-nano",
        'content': 'red-light-green-light'
    },

    {
        'name': 'radios',
        'content': 'red-light-green-light-in-space'
    }
]

def create_assignment(name, content):
    new_assignment = {
        'name': name,
        'content': content
    }
    assignment.append(new_assignment)
    return new_assignment
    
def get_all_assignments():
    return assignment

def get_assignment(name):
    for a in assignment:
        if a['name'] == name:
            return a

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