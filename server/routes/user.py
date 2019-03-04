from flask import Blueprint, jsonify, request
import controllers.user

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = controllers.user.create_user(data['name'], data['project'])
    print('HI')
    return jsonify(new_user)

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = controllers.user.get_all_users()
    return jsonify(users)

@user_bp.route("/<name>")
def get_user(name):
    user_obj = controllers.user.get_user(name)
    return jsonify(user_obj)