# flask api with just one endpoint


import pickle
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource

import prediction as p

app = Flask(__name__)
api = Api(app)
CORS(app)

class Test(Resource):
    def get(self):
        return jsonify({"message": "Hello World"})
    def post(self):
        data = request.get_json()
        return jsonify(data)
    
api.add_resource(Test, "/test")

class getPredictionImage(Resource):
    def get(self):
        return jsonify({"error": "Please send a POST request"})
    def post(self):
        try:
            data = request.get_json()
            date = data["date"]
            model = None
            with open("model.pkl", "rb") as f:
                model = pickle.load(f)     
            url = p.uploadForecastToCloudinary(model, date)
            return jsonify({"url": url})
        except Exception as e:
            return jsonify({"error": str(e)})
    
api.add_resource(getPredictionImage, "/getPredictionImage")

if __name__ == "__main__":
    app.run(debug=True)
    

