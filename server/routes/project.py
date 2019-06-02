from flask import Blueprint, jsonify, request, abort
import controllers.project
from common.errors import error, ResourceExistsError, ResourceDoesNotExistError

project_bp = Blueprint('project', __name__)

@project_bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()

    try:
        new_project = controllers.project.create_project(data['name'], data['description'])
    except KeyError:
        return error('bad request')
    except ResourceExistsError:
        return error('project already exists')

    return jsonify(new_project)

@project_bp.route('/', methods=['GET'])
def get_all_projects():
    projects = controllers.project.get_all_projects()
    return jsonify(projects)

@project_bp.route("/<name>", methods=['GET', 'DELETE'])
def get_project(name):
    if request.method == 'GET':
        try:
            project_obj = controllers.project.get_project(name)
            return jsonify(project_obj)
        except ResourceDoesNotExistError:
            return error(f"Project '{name}' not found.", 404)

    elif request.method == 'DELETE':
        try:
            project_obj = controllers.project.delete_project(name)
            return jsonify(project_obj)
        except ResourceDoesNotExistError:
            return error(f"Project '{name}' not found.", 404)

@project_bp.route("/assignment/", methods=['POST'])
def add_assignment():
    data = request.get_json()

    try:
        added_assignment = controllers.project.add_assignment(data['project'], data['assignment'])
    except KeyError:
        return error('bad request')
    except ResourceExistsError:
        return error('Assignment/Project already exists')

    return jsonify(added_assignment)