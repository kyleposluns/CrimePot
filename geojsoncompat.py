import json
from math import radians, cos, sin, asin, sqrt


def distBetween(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return(c * r)
'''
with urllib.request.urlopen(data_url) as url:
    python_obj = json.loads(url.read().decode())["result"]["records"]
'''

def filterByRadius(dict, lat, long, radius):
    #python_obj = json.loads(json_str)["result"]["records"]
    python_obj = dict.get('result').get('records')
    geoJsonDicts = {"type": "FeatureCollection"}
    arrayOfObjects = []

    for object in python_obj:
        if (object["month"] and object["year"] and object["occurred_on_date"] and object["lat"]
        and object["long"] and distBetween(float(object["long"]), float(object["lat"]), long, lat) <= radius):
            arrayOfObjects.append({
            "type": "Feature",
            "geometry": {
            "type": "Point",
            "coordinates": [object["long"], object["lat"]]
            },
            "properties": {
                "Offense decription": object["offense_description"][0] + object["offense_description"][1:].lower(),
                "Date": object["month"] + "/" + object["occurred_on_date"][8:10] + "/"+object["year"],
                "Time": object["occurred_on_date"][11:],
                "District": object["district"],
                "Street": object["street"]
                }
            })
            geoJsonDicts["features:"] = arrayOfObjects
    return (geoJsonDicts)
