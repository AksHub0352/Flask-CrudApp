from flask import Flask, request, json, Response
import pymongo
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import json


app = Flask(__name__)
client = pymongo.MongoClient(
    "mongodb+srv://aksapple1610:Mongo1234@cluster0.e68yfb6.mongodb.net/?retryWrites=true&w=majority")
db = client.User
test = db.test
app.secret_key = "secret-key"
app.config["MONGO_URI"] = "mongodb+srv://aksapple1610:Mongo1234@cluster0.e68yfb6.mongodb.net/?retryWrites=true&w=majority"


# connect db to pymongo library
mongo = PyMongo(app)


@app.route('/users', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']
    # return (_json)
    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        test.insert_one({'name': _name, 'email': _email,
                        'password': _hashed_password})
        return jsonify("User added Successfully")
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'User not found ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.route('/users')
def get_user():
    users = test.find()
    resp = json.loads(dumps(users))
    return (resp)
    # return Response(response=json.dumps(users), status=400, mimetype='application/json')


@app.route('/user/<id>')
def user(id):
    user = test.find_one({'_id': ObjectId(id)})
    resp = json.loads(dumps(user))
    return resp


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    test.delete_one({'_id': ObjectId(id)})
    resp = jsonify("User Deleted Succesfully")
    resp.status_code = 200
    return resp


@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    _json = request.json
    _id = id
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']
    # return (_json)
    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)
        test.update_one({'_id': ObjectId(_id) }, {'$set': {'name': _name, 'email': _email, 'password': _password}})
        resp = jsonify("User Updated SuccessFully")
        resp.status_code = 200
        return resp
    else:
        return not_found()


if __name__ == "__main__":
    app.run(debug=True)
