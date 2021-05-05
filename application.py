import flask
from flask import request, jsonify

from database import get_latest_co2_readings, insert_co2_reading, init_database

init_database()
app = flask.Flask(__name__)

@app.route('/get_latest_co2', methods=['GET'])
def home():
    co2_readings_query_result = get_latest_co2_readings()

    co2_readings = []
    for row in co2_readings_query_result:
        d = dict(zip(row.keys(), row))
        co2_readings.append(d)

    return jsonify(co2_readings)


@app.route('/post_co2_reading', methods=['POST'])
def post_co2_reading():
    co2_reading = request.form['co2']
    insert_co2_reading(co2_reading)
    return success_response()


def success_response():
    return jsonify(success=True)
