from app import db
from model.user import User, create_user, does_user_exist

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

    try:
        for user in test_users:
            if not does_user_exist(user['username']):
                create_user(user)
    except Exception as e:
        print("Could not load in mock data", e)

if __name__=="__main__":
    load()
