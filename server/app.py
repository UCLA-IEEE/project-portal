from flask import Flask

from routes.user import user_bp
from routes.assignment import assignment_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(assignment_bp, url_prefix='/assignment')