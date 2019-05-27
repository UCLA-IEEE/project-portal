from flask import Blueprint, jsonify, request, abort
import controllers.assignment
from common.errors import error, ResourceExistsError, ResourceDoesNotExistError

assignment_bp = Blueprint('assignment', __name__)

@assignment_bp.route('/', methods=['POST'])
def create_assignment():
    data = request.get_json()

    try:
        new_assignment = controllers.assignment.create_assignment(data['name'], data['content'])
    except KeyError:
        return error('bad request')
    except ResourceExistsError:
        return error('assignment already exists')

    return jsonify(new_assignment)

@assignment_bp.route('/', methods=['GET'])
def get_all_assignments():
    assignments = controllers.assignment.get_all_assignments()
    return jsonify(assignments)

@assignment_bp.route("/<name>", methods=['GET', 'DELETE'])
def get_assignment(name):
    if request.method == 'GET':
        try:
            assignment_obj = controllers.assignment.get_assignment(name)
            return jsonify(assignment_obj)
        except ResourceDoesNotExistError:
            return error(f"Assignment '{name}' not found.", 404)

    elif request.method == 'DELETE':
        try:
            assignment_obj = controllers.assignment.delete_assignment(name)
            return jsonify(assignment_obj)
        except ResourceDoesNotExistError:
            return error(f"Assignment '{name}' not found.", 404)
        
