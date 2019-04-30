from flask import jsonify

def error(msg, code=400):
    return jsonify({'error': msg}), 400

class ResourceExistsError(Exception):
    pass

class ResourceDoesNotExistError(Exception):
    pass

class MissingFieldsError(Exception):
    pass