from app import db
from model.user import User, does_user_exist, create_user
from model.project import Project, does_project_exist
from model.assignment import Assignment, does_assignment_exist

def load():
    # Add test data
    test_users = [
        {
            'username': 'rzalog',
            'email': 'rzalog@gmail.com',
            'name': 'Robert Zalog',
            'role': 'admin',
            'password': 'password'
        },
        {
            'username': 'maggie',
            'email': 'maggie@gmail.com',
            'name': 'Maggie Huang',
            'role': 'member',
            'password': 'password'
        }
    ]
    # Add test data
    test_projects = [
        Project(name="OPS", description="circuits"),
        Project(name="Micromouse", description="autonomous maze-solving robot")
    ]
    
    test_assignments = [
        Assignment(name="RedLightGreenLight", content="asdf"),
        Assignment(name="Radios", content="asdf")
    ]

    try:
        for user in test_users:
            if not does_user_exist(user['username']):
                create_user(user)
        # for project in test_projects:
        #     if not does_project_exist(project['name']):
        #         create_project(project['name'], project['description'])
        # for assignment in test_assignments:
        #     if not does_assignment_exist(assignment['name']):
        #         create_assignment(assignment['name'], assignment['content'])
    except Exception as e:
        print("Could not load in mock data", e)

if __name__=="__main__":
    load()
