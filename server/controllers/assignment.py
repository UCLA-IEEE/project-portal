import model.assignment

def create_assignment(name, content):
    new_assignment = model.assignment.create_assignment(name, content)
    return new_assignment

def get_all_assignments():
    assignments = model.assignment.get_all_assignments()
    return assignments

def get_assignment(name):
    assignment = model.assignment.get_assignment(name)
    return assignment