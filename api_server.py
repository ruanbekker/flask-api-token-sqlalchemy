from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'randomsecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ruan/workspace/python-projects/api-db-auth/db.sqlite'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50))
    name = db.Column(db.String(50))
    password= db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

@app.route('/api/v1/user', methods=['GET'])
def get_all_users():

    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users': output})

@app.route('/api/v1/user/<public_id>', methods=['GET'])
def get_one_user(public_id):

	return jsonify({'user': ''})

@app.route('/api/v1/user', methods=['POST'])
def create_user():

	return jsonify({'message': ''})

@app.route('/api/v1/user/<public_id>', methods=['PUT'])
def promote_user(public_id):

	return jsonify({'message': ''})

@app.route('/api/v1/user/<public_id>', methods=['DELETE'])
def delete_user(public_id):

	return jsonify({'message': ''})


if __name__ == '__main__':
	app.run(port=5000, debug=True)
