from app import db
from model.user import User, does_user_exist

def load():
    # Add test data
    test_users = [
        User(
            username='rzalog',
            email='rzalog@gmail.com',
            name='Robert Zalog',
            role='admin',
            password='password'
        ),
        User(
            username='maggie',
            email='maggie@gmail.com',
            name='Maggie Huang',
            role='member',
            password='password'
        )
    ]

    try:
        for user in test_users:
            if not does_user_exist(user.username):
                db.session.add(user)
                db.session.commit()
    except Exception as e:
        print("Could not load in mock data", e)

if __name__=="__main__":
    load()
