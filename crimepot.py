#!/usr/bin/env python3

from flask import Flask, request
import datetime

app = Flask(__name__)

#localhost:5000/crime_map?lat=31.29734&long=29.32948&radius=1km&time=1mo
@app.route('/crime_map')
def query_map():
    lat = request.args['lat']
    long = request.args['long']
    radius = request.args['radius']
    minutes = int(request.args['minutes'])
    hours = int(request.args['hours'])
    days = int(request.args['days'])
    weeks = int(request.args['weeks'])
    #'2019-02-09T19:08:07.332185'
    #'2019-02-09 19:08:00'
    datestring = target_date(minutes, hours, days, weeks).isoformat()
    datestring_formatted = datestring[:10] + " " + datestring[11:19]
    return datestring_formatted


def create_time_delta(minutes, hours, days, weeks):
    return datetime.timedelta(days=(days if days is not None else 0), seconds=0, microseconds=0, milliseconds=0,
    minutes=(minutes if minutes is not None else 0),
     hours=(hours if hours is not None else 0),
     weeks=(weeks if weeks is not None else 0))

def target_date(minutes, hours, days, weeks):
    return datetime.datetime.now() - create_time_delta(minutes, hours, days, weeks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
