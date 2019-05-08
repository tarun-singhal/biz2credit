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
from bson.objectid import ObjectId
from bson import json_util

# Import the helpers module
helper_module = imp.load_source('*', './app/helpers.py')

# Select the database
db = client.test
# Select the collection
collection = db.story

api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class StoryResource(Resource):

    @auth.login_required
    def put(self, id):
        """
        Update Story API
        """
        try:
            # Get the value which needs to be updated
            try:
                body = ast.literal_eval(json.dumps(request.get_json()))
                body['updated_time'] = datetime.now()
                
            except Exception as e:
                return {"error": "Error Found, "+str(e)}, 400

            if 'user_id' not in request.args:
                return {"error": "Please provide valid user_id in query param"}

            # Updating the user
            records_updated = collection.update_one({"user_id": ObjectId(request.args['user_id']), "id": ObjectId(id)}, 
                                {"$set": body})

            # Check if resource is updated
            if records_updated.modified_count > 0: 
                # Prepare the response as resource is updated successfully
                return {"resp": "Story Updated Succefully !"}, 200
            else:
                return {"resp": "Records not found!"}, 404
        except Exception as e:
            return {"error": "Error found, "+str(e)}, 500

    @auth.login_required
    def get(self, id):
        """
        Get Story based on story ID
        """
        try:
            # Fetch all the record(s)
            records_fetched = collection.find({"_id": ObjectId(id)})
            if records_fetched.count() > 0:
                json_docs = [json.dumps(doc, default=json_util.default) for doc in records_fetched]
                return {"resp": json_docs}
            else:
                # No records are found
                return {"resp": "No records found"}, 404
        except Exception as e:
            return {"error": "Error found, "+str(e)}, 500 

    @auth.login_required
    def delete(self, id):
        """
        Delete Story API
        """
        try:
            # Delete the story
            delete_story = collection.delete_one({"_id": ObjectId(id)})
            if delete_story.deleted_count > 0:
                # Prepare the response
                return {"resp": "Story Deleted Successfully !!"}, 204
            else:
                # Resource Not found
                return {"resp": "Resource not found!!"}, 404
        except Exception as e:
            return {'error': "Error found, "+str(e)}, 500

api.add_resource(StoryResource, '/story/<id>')