
"""This module will serve the api request for the User related"""

from config import client, USER_DATA
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
import imp
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api
from datetime import datetime
from bson import json_util
# from flask.ext.bcrypt import Bcrypt
import base64

# Import the helpers module
helper_module = imp.load_source('*', './app/helpers.py')
# Select the database
db = client.blog
# Select the collection
collection = db.author
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class UserListResource(Resource):

    @auth.login_required
    def get(self):
        """
        To get the User listing
        """
        try:
            # Return all the records as query string parameters are not available
            records_fetched = collection.find()

            if records_fetched.count() > 0:
                json_docs = [ doc for doc in records_fetched]
                for rec in json_docs:
                    rec['_id'] = str(rec['_id'])
                    if 'created_time' in rec and isinstance(rec['created_time'], datetime):
                        rec['created_time'] = rec['created_time'].isoformat()
                return {"resp": json_docs}
            else:
                # Return empty array if no users are found
                return {"resp":"No Records found!"}
        except Exception as e:
            return {"error":"Error Found, "+str(e)}, 500


    @auth.login_required
    def post(self):
        """
        Create User API: With one document or bulk document insertion
        """
        try:
            # Create new users
            try:
                body = ast.literal_eval(json.dumps(request.get_json()))
            except Exception as e:
                return {"error": "Error Found, "+str(e)}, 400

                #TODO: Need to check for the password hash issue
                # if user_pass != " ":
                #     password_hash =  base64.b64encode(user_pass)
                #     body[i]['password'] = password_hash

            record_created = collection.insert(body)

            # Prepare the response
            if isinstance(record_created, list):
                # Return list of Id of the newly created item
                return {'resp': [str(v) for v in record_created]}, 201
            else:
                # Return Id of the newly created item
                return {'resp': str(record_created)}, 201
        except Exception as e:
            return {"error":"Error found, "+str(e)}, 500

api.add_resource(UserListResource, '/user')  
