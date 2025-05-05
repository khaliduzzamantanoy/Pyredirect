from flask import Flask, redirect, request
from datetime import datetime

app = Flask(__name__)

# Optional: Log all requests
@app.before_request
def log_requests():
    print(f"[{datetime.now()}] Redirecting: {request.url}")

# Main redirect logic
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """Redirect all requests to the external result portal"""
    return redirect(f'https://diuresult-929938982260.us-central1.run.app/{path}', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
