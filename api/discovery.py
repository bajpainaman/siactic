# sciatic_protocol/api/discovery.py

from flask import Blueprint, request, jsonify
from schema.discovery import DiscoveryRequest, DiscoveryResponse, Platform

discovery_bp = Blueprint('discovery', __name__)

@discovery_bp.route('/discover', methods=['POST'])
def discover():
    req_data = request.get_json()
    req = DiscoveryRequest(**req_data)

    # Example response
    platforms = [Platform(id="1", name="Platform A", description="ML Platform A", models=[])]
    resp = DiscoveryResponse(platforms=platforms)

    return jsonify(resp.dict())
