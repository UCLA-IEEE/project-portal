from app import db

print("WARNING: This will drop all data in the DB. Are you sure you want to do this?")
resp = input("(Y/n): ")

if resp.lower() == "yes" or resp.lower() == "y":
    db.drop_all()
<<<<<<< HEAD
    db.create_all()
=======
db.create_all()
>>>>>>> temp changes
