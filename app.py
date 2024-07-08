# sciatic_protocol/app.py

from flask import Flask
from api.discovery import discovery_bp
from api.transaction import transaction_bp
from api.execution import execution_bp
from api.post_execution import post_execution_bp

app = Flask(__name__)

app.register_blueprint(discovery_bp, url_prefix='/api/v1')
app.register_blueprint(transaction_bp, url_prefix='/api/v1')
app.register_blueprint(execution_bp, url_prefix='/api/v1')
app.register_blueprint(post_execution_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
