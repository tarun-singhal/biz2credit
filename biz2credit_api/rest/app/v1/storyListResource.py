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
from flask import make_response

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

class BlogListResource(Resource):

    @auth.login_required
    def post(self):
        """
        To create the Story
        """
        try:
            # Create new users story API
            try:
                body = ast.literal_eval(json.dumps(request.get_json()))
            except Exception as e:
                # Bad request as request body is not available
                return {"error": "Bad request call: "+str(e)}, 400

            record_created = collection.insert(body)

            # Prepare the response
            if isinstance(record_created, list):
                # Return list of Id of the newly created item
                return {'resp': [str(v) for v in record_created]}, 201
            else:
                # Return Id of the newly created item
                return {'resp': str(record_created)}, 201
        except Exception as e:
            return {"error": "Error Found, "+str(e)}, 500

    @auth.login_required
    def get(self):
        """
        Get all Story API
        """
        try:
            # Return all the records as query string parameters are not available
            records_fetched = collection.find()
            if records_fetched.count() > 0:
                records = {}
                json_docs = [ doc for doc in records_fetched]
                for rec in json_docs:
                    rec['_id'] = str(rec['_id'])
                    if 'updated_time' in rec and isinstance(rec['updated_time'], datetime):
                        rec['updated_time'] = rec['updated_time'].isoformat()

                return {'resp': json_docs}
            else:
                # Return empty array if no users are found
                return {"resp":"No Records found!"}
        except Exception as e:
            return {"error":"Error Found, "+str(e)}, 500


api.add_resource(BlogListResource, '/story')