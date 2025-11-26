from flask import Flask, request, jsonify
from auth import authenticate

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username', '')
    password = data.get('password', '')
    if not username or not password:
        return jsonify({'error': 'username and password required'}), 400
    token = authenticate(username, password)
    if not token:
        return jsonify({'error': 'invalid credentials'}), 401
    return jsonify({'token': token}), 200

if __name__ == '__main__':
    app.run(debug=True)
