

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
from bson.objectid import ObjectId
from bson import json_util

# Import the helpers module
helper_module = imp.load_source('*', './app/helpers.py')
# Select the database
db = client.test
# Select the collection
collection = db.author
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class UserResource(Resource):

    @auth.login_required
    def put(self, user_id):
        """
        Update the User information
        """
        try:
            # Get the value which needs to be updated
            try:
                body = ast.literal_eval(json.dumps(request.get_json()))
            except Exception as e:
                return {"error": "Error found, "+str(e)}, 400

            # Updating the user
            records_updated = collection.update_one({"id": int(user_id)}, 
                {"$set": {"phone":body['phone'], "location":body['location']}}, upsert=False)
            # Check if resource is updated
            if records_updated.modified_count > 0:
                return {"resp": "User Updated Succefully on ID: "+user_id+" !"}, 200
            else:
                return "", 404
        except Exception as e:
            return {'error': "Error Found, "+str(e)}, 500

    """
    Function to remove the user.
    """
    def delete(self, user_id):
        """
        Delete the User
        """
        try:
            # Delete the user
            delete_user = collection.delete_one({"_id": ObjectId(user_id)})
            if delete_user.deleted_count > 0 :
                # Prepare the response
                return {"resp":"User Deleted Successfully on ID: "+user_id+ " !!"}, 204
            else:
                # Resource Not found
                return "", 404
        except Exception as e:
            return {'error': str(e)}, 500
            

    @auth.login_required
    def get(self, user_id):
        """
        Get User based on user ID
        """
        try:
            # Fetch all the record(s)
            records_fetched = collection.find({"_id": ObjectId(user_id)})
            if records_fetched.count() > 0:
                json_docs = [json.dumps(doc, default=json_util.default) for doc in records_fetched]
                return {"resp": json_docs}
            else:
                # No records are found
                return {"resp": "No records found"}, 404
        except Exception as e:
            return {"error": "Error found, "+str(e)}, 500  

api.add_resource(UserResource, '/user/<user_id>')  