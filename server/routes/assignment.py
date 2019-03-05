from flask import Blueprint, jsonify, request
import controllers.assignment

assignment_bp = Blueprint('assignment', __name__)

@assignment_bp.route('/', methods=['POST'])
def create_assignment():
    data = request.get_json()
    new_assignment = controllers.assignment.create_assignment(data['name'], data['content'])
    return jsonify(new_assignment)

@assignment_bp.route('/', methods=['GET'])
def get_all_assignments():
    assignment = controllers.assignment.get_all_assignments()
    return jsonify(assignment)

@assignment_bp.route("/<name>")
def get_user(name):
    assignment_obj = controllers.assignment.get_assignment(name)
    return jsonify(assignment_obj)
