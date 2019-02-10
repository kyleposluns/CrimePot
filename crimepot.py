#!/usr/bin/env python3

from flask import Flask, request
import datetime
import crimequery as cquery
import geojsoncompat as gjc

app = Flask(__name__)

#localhost:5000/crime_map?lat=31.29734&long=29.32948&radius=1km&time=1mo
@app.route('/crime_map')
def query_map():
    lat = float(request.args['lat'])
    long = float(request.args['long'])
    radius = float(request.args['radius'])
    minutes = int(request.args['minutes'])
    hours = int(request.args['hours'])
    days = int(request.args['days'])
    weeks = int(request.args['weeks'])
    #'2019-02-09T19:08:07.332185'
    #'2019-02-09 19:08:00'
    target_date_string = target_date(minutes, hours, days, weeks).isoformat()
    target_date_string_formatted = target_date_string[:10] + " " + target_date_string[11:19]
    json = cquery.complete_get_request(datetime.datetime.now().isoformat(), target_date_string_formatted)
    return str(gjc.filterByRadius(json, lat, long, radius))

def create_time_delta(minutes, hours, days, weeks):
    return datetime.timedelta(days=(days if days is not None else 0), seconds=0, microseconds=0, milliseconds=0,
    minutes=(minutes if minutes is not None else 0),
     hours=(hours if hours is not None else 0),
     weeks=(weeks if weeks is not None else 0))

def target_date(minutes, hours, days, weeks):
    return datetime.datetime.now() - create_time_delta(minutes, hours, days, weeks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
