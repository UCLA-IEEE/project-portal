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
