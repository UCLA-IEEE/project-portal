from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db = SQLAlchemy(app)


# Here because of circular imports
from routes.user import user_bp
app.register_blueprint(user_bp, url_prefix='/user')

from routes.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

# Simple route for testing purposes
@app.route("/")
def hello():
    return '<p>Hello from Project Portal API<p>'
