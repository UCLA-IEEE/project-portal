import model.assignment

def create_assignment(name, content):
    new_assignment = model.assignment.create_assignment(name, content)
    return new_assignment.to_dict()

def get_all_assignments():
    assignments = model.assignment.get_all_assignments()
    return [assignment.to_dict() for assignment in assignments]

def get_assignment(name):
    assignment = model.assignment.get_assignment(name)
    return assignment.to_dict()

def delete_assignment(name):
    assignment = model.assignment.delete_assignment(name)
    return assignment.to_dict()
