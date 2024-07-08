# sciatic_protocol/api/execution.py

from flask import Blueprint, request, jsonify
from schema.execution import ExecutionRequest, ExecutionResponse, ProgressUpdate

execution_bp = Blueprint('execution', __name__)

@execution_bp.route('/execute', methods=['POST'])
def execute():
    req_data = request.get_json()
    req = ExecutionRequest(**req_data)

    # Example response
    updates = [ProgressUpdate(task_id="12345", progress=50)]
    resp = ExecutionResponse(status="In Progress", progress_updates=updates)

    return jsonify(resp.dict())
