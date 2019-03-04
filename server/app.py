from flask import Flask

from routes.user import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')