# sciatic_protocol/api/post_execution.py

from flask import Blueprint, request, jsonify
from schema.post_execution import PostExecutionRequest, PostExecutionResponse

post_execution_bp = Blueprint('post_execution', __name__)

@post_execution_bp.route('/post_execution', methods=['POST'])
def post_execution():
    req_data = request.get_json()
    req = PostExecutionRequest(**req_data)

    # Example response
    resp = PostExecutionResponse(status="Success", details={"feedback_id": "67890"})

    return jsonify(resp.dict())
