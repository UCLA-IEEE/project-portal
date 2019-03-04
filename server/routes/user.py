from flask import Blueprint, jsonify, request
import controllers.user

user_bp = Blueprint('user', __name__)
assignment_bp = Blueprint('assignment', __name__)

@assignment_bp.route('/', methods=['POST'])
def create_assignment():
    data = request.get_json()
    new_assignment = controllers.user.create_assignment(data['name'], data['content'])
    return jsonify(new_assignment)

@assignment_bp.route('/', methods=['GET'])
def get_all_assignments():
    assignment = controllers.user.get_all_assignments()
    return jsonify(assignment)

@assignment_bp.route("/<name>")
def get_user(name):
    assignment_obj = controllers.user.get_assignment(name)
    return jsonify(assignment_obj)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = controllers.user.create_user(data['name'], data['project'])
    return jsonify(new_user)

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = controllers.user.get_all_users()
    return jsonify(users)

@user_bp.route("/<name>")
def get_user(name):
    user_obj = controllers.user.get_user(name)
    return jsonify(user_obj)