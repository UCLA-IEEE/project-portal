from flask import Blueprint, jsonify, request, abort
import controllers.user
from common.errors import error, ResourceExistsError, ResourceDoesNotExistError, MissingFieldsError

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return error('must include user creation data')

    try:
        new_user = controllers.user.create_user(data)
    except KeyError:
        return error('bad request')
    except ResourceExistsError:
        return error('user already exists')
    except MissingFieldsError:
        return error('did not specify correct fields')

    return jsonify(new_user)

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = controllers.user.get_all_users()
    return jsonify(users)

@user_bp.route("/<username>", methods=['GET', 'DELETE'])
def get_user(username):
    if request.method == 'GET':
        try:
            user_obj = controllers.user.get_user(username)
            return jsonify(user_obj)
        except ResourceDoesNotExistError:
            return error(f"User '{username}' not found.", 404)

    elif request.method == 'DELETE':
        try:
            user_obj = controllers.user.delete_user(username)
            return jsonify(user_obj)
        except ResourceDoesNotExistError:
            return error(f"User '{username}' not found.", 404)