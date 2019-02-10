import json
from math import radians, cos, sin, asin, sqrt
import string


def distBetween(lon1, lat1, lon2, lat2):
  lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
  # haversine formula
  dlon = lon2 - lon1
  dlat = lat2 - lat1
  a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
  c = 2 * asin(sqrt(a))
  r = 6371  # Radius of earth in kilometers. Use 3956 for miles
  return(c * r)


'''
with urllib.request.urlopen(data_url) as url:
    python_obj = json.loads(url.read().decode())["result"]["records"]
'''


def filterByRadius(dict, lat, long, radius):
  # python_obj = json.loads(json_str)["result"]["records"]
  python_obj = dict.get('result').get('records')
  geoJsonDicts = {"type": "FeatureCollection"}
  arrayOfObjects = []

  for object in python_obj:
    if (object["lat"] == None or object["long"] == None or object["month"] == None or object["year"] == None or object["occurred_on_date"] == None):
      continue

    lat1 = float(object["lat"])
    long1 = float(object["long"])
    month = object["month"]
    year = object["year"]
    date = object["occurred_on_date"]
    print(str(distBetween(long1, lat1, long, lat)))

    if (distBetween(long1, lat1, long, lat) <= radius):
      arrayOfObjects.append({
          "type": "Feature",
          "geometry": {
              "type": "Point",
              "coordinates": [long1, lat1]
          },
          "properties": {
              "Offense decription": object["offense_description"][0] + object["offense_description"][1:].lower(),
              "Date": month + "/" + date[8:10] + "/" + year,
              "Time": date[11:],
              "District": object["district"],
              "Street": object["street"].title()
          }
      })
      geoJsonDicts["features:"] = arrayOfObjects
  return (geoJsonDicts)
