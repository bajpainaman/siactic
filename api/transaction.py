# sciatic_protocol/api/transaction.py

from flask import Blueprint, request, jsonify
from schema.transaction import TrainingRequest, InferenceRequest, TransactionResponse

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/train', methods=['POST'])
def train():
    req_data = request.get_json()
    req = TrainingRequest(**req_data)

    # Example response
    resp = TransactionResponse(status="Success", details={"task_id": "12345"})

    return jsonify(resp.dict())

@transaction_bp.route('/infer', methods=['POST'])
def infer():
    req_data = request.get_json()
    req = InferenceRequest(**req_data)

    # Example response
    resp = TransactionResponse(status="Success", details={"result": {}})

    return jsonify(resp.dict())
