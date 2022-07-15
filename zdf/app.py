from flask import Flask, jsonify
import logging

#https://towardsdatascience.com/deploy-a-python-api-on-aws-c8227b3799f0
#https://ianwhitestone.work/zappa-serverless-docker/
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route("/")
def serve():
    return jsonify(success=True)

@app.route('/test', methods=['GET'])
def get_test():
    return jsonify({'message': 'The lambda is working'})
