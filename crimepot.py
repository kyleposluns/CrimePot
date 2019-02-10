#!/usr/bin/env python3

from flask import Flask, request
import datetime
import crimequery as cquery
import geojsoncompat as gjc
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#localhost:5000/crime_map?lat=31.29734&long=29.32948&radius=1km&time=1mo
@app.route('/crime_map')
@cross_origin()
def query_map():
    lat = float(request.args['lat'])
    long = float(request.args['long'])
    radius = float(request.args['radius'])
    days = int(request.args['days'])
    #'2019-02-09T19:08:07.332185'
    #'2019-02-09 19:08:00'
    target_date_string = target_date(days).isoformat()
    target_date_string_formatted = target_date_string[:10] + " " + target_date_string[11:19]
    json_dict = cquery.complete_get_request(datetime.datetime.now().isoformat(), target_date_string_formatted)
    return json.dumps(gjc.filterByRadius(json_dict, lat, long, radius))

def create_time_delta(days):
    return datetime.timedelta(days=days)

def target_date(days):
    return datetime.datetime.now() - create_time_delta(days)

if __name__ == '__main__':
    app.run(port=5000)
