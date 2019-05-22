from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Here because of circular imports 
from routes.user import user_bp
<<<<<<< HEAD
from routes.assignment import assignment_bp
from routes.project import project_bp

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(assignment_bp, url_prefix ='/assignment')
app.register_blueprint(project_bp, url_prefix='/project')
=======
app.register_blueprint(user_bp, url_prefix='/user')

from routes.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

# Simple route for testing purposes
@app.route("/")
def hello():
    return '<p>Hello from Project Portal API<p>'
>>>>>>> 1aef29259506baa3a4e6e86ca4014b56f56563b8
