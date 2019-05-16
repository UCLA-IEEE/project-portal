from flask import Blueprint, request, jsonify
from model.user import get_user
from common.errors import error, ResourceExistsError, ResourceDoesNotExistError, MissingFieldsError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return error("must include username and password")

    try:
        username, password = data['username'], data['password']
    except KeyError:
        return error("must include username and password")
    
    try:
        user = get_user(username)
        if user.check_pw(password):
            return jsonify(user.to_dict())
        else:
            return error("invalid password", 401)
    except ResourceDoesNotExistError:
        return error("user {} does not exist".format(username))

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return 'logout'