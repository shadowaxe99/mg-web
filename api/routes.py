from flask import Blueprint, request, jsonify
from api.utils import generate_ai_response, validate_user, process_feature_activation, process_monetization_event
from api.exceptions import InvalidUsage

routes = Blueprint('routes', __name__)

@routes.route('/api/conversation', methods=['POST'])
def conversation():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')

    if not user_id or not message:
        raise InvalidUsage('User ID and message are required.', status_code=400)

    if not validate_user(user_id):
        raise InvalidUsage('Invalid user ID.', status_code=404)

    response = generate_ai_response(INFLUENCER_NAME, message)
    return jsonify({'message': response}), 200

@routes.route('/api/features', methods=['POST'])
def features():
    data = request.get_json()
    user_id = data.get('user_id')
    feature_name = data.get('feature_name')

    if not user_id or not feature_name:
        raise InvalidUsage('User ID and feature name are required.', status_code=400)

    if not validate_user(user_id):
        raise InvalidUsage('Invalid user ID.', status_code=404)

    result = process_feature_activation(user_id, feature_name)
    return jsonify(result), 200

@routes.route('/api/monetization', methods=['POST'])
def monetization():
    data = request.get_json()
    user_id = data.get('user_id')
    monetization_type = data.get('monetization_type')
    details = data.get('details')

    if not user_id or not monetization_type:
        raise InvalidUsage('User ID and monetization type are required.', status_code=400)

    if not validate_user(user_id):
        raise InvalidUsage('Invalid user ID.', status_code=404)

    result = process_monetization_event(user_id, monetization_type, details)
    return jsonify(result), 200

@routes.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Add more routes as needed for additional functionality.