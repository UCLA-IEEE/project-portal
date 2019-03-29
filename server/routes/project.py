from flask import Blueprint, jsonify, request
import controllers.project

project_bp = Blueprint('project', __name__)

@project_bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    new_project = controllers.project.create_project(data['name'], data['description'])
    return jsonify(new_project)

@project_bp.route('/', methods=['GET'])
def get_all_projects():
    projects = controllers.project.get_all_projects()
    return jsonify(projects)

@project_bp.route("/<name>")
def get_project(name):
    project_obj = controllers.project.get_project(name)
    return jsonify(project_obj)