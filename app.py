from flask import Flask, jsonify, request
import logging
from services.stats.gdp import selenium_get_gdp_url

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route("/")
def serve():
    return jsonify(success=True)


@app.route("/test", methods=["GET"])
def get_test():
    return jsonify({"message": "The lambda is working"})


@app.route("/get_gdp_url", methods=["POST"])
def get_gdp_url():
    req = request.get_json()
    month, year = req["month"], req["year"]
    try:
        gdp_csv_url = selenium_get_gdp_url(year, month)
        return jsonify({"message": gdp_csv_url})
    except Exception as err:
        return jsonify({"Error": str(err)})
