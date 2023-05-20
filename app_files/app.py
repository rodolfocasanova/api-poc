# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os
  
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
  
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class API(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        return jsonify({'status': '200','response': 'Flask up and running'})
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json()     # status code
        return jsonify({'status': '200','response': data}), 201
  
  
  
# adding the defined resources along with their corresponding urls
api.add_resource(API, '/')

  
  
# driver function
if __name__=='__main__':
    app.run( debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)) )