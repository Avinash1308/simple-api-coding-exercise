from api.app import app, db
from flask import request, jsonify
from api.app.models import User, Company, Client, ClientUser

# Endpoint to list app Users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({
            'username': user.username,
            'email': user.email,
            'phone': user.phone
        })
    return jsonify(users_list), 200

# Endpoint to replace some User fields at once
@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    # Implementation to update user
    pass

# Endpoint to create some Client
@app.route('/clients', methods=['POST'])
def create_client():
    # Implementation to create client
    pass

# Endpoint to change any Client field
@app.route('/clients/<client_id>', methods=['PATCH'])
def update_client(client_id):
    # Implementation to update client
    pass

if __name__ == '__main__':
    app.run(debug=True)

