import json
from math import radians, cos, sin, asin, sqrt
import urllib.request

json_data = "[{\"offense_description\": \"INVESTIGATE PROPERTY\", \"shooting\": null, \"district\": \"D4\", \"offense_code\": \"03114\", \"hour\": \"18\", \"reporting_area\": \"136\", \"_full_text\": \"'-02':10 '-05':11 '-71.07978844':24,26 '00':14 '03114':2 '136':8 '18':12,18 '2':16 '2019':9,15 '26':13 '42.35256908':23,25 'd4':7 'i192009557':1 'investigate':3,5 'marlborough':21 'part':19 'property':4,6 'st':22 'three':20 'tuesday':17\", \"occurred_on_date\": \"2019-02-05 18:26:00\", \"day_of_week\": \"Tuesday\", \"month\": \"2\", \"street\": \"MARLBOROUGH ST\", \"ucr_part\": \"Part Three\", \"long\": \"-71.07978844\", \"year\": \"2019\", \"lat\": \"42.35256908\", \"incident_number\": \"I192009557\", \"_id\": 1, \"offense_code_group\": \"Investigate Property\", \"location\": \"(42.35256908, -71.07978844)\"}, {\"offense_description\": \"SICK/INJURED/MEDICAL - PERSON\", \"shooting\": null, \"district\": \"C11\", \"offense_code\": \"03006\", \"hour\": \"11\", \"reporting_area\": \"361\", \"_full_text\": \"'-02':10 '-05':11 '-71.06391719':24,26 '00':14 '03006':2 '11':12,18 '2':16 '2019':9,15 '25':13 '361':8 '42.29313171':23,25 'assistance':4 'c11':7 'centre':21 'i192009397':1 'medical':3 'part':19 'person':6 'sick/injured/medical':5 'st':22 'three':20 'tuesday':17\", \"occurred_on_date\": \"2019-02-05 11:25:00\", \"day_of_week\": \"Tuesday\", \"month\": \"2\", \"street\": \"CENTRE ST\", \"ucr_part\": \"Part Three\", \"long\": \"-71.06391719\", \"year\": \"2019\", \"lat\": \"42.29313171\", \"incident_number\": \"I192009397\", \"_id\": 3, \"offense_code_group\": \"Medical Assistance\", \"location\": \"(42.29313171, -71.06391719)\"}, {\"offense_description\": \"VANDALISM\", \"shooting\": null, \"district\": \"B2\", \"offense_code\": \"01402\", \"hour\": \"19\", \"reporting_area\": \"904\", \"_full_text\": \"'-02':8 '-04':9 '-71.08200715':22,24 '00':12 '01402':2 '18':11 '19':10,16 '2':14 '2019':7,13 '42.32924494':21,23 '904':6 'b2':5 'i192009262':1 'monday':15 'part':17 'st':20 'two':18 'vandalism':3,4 'zeigler':19\", \"occurred_on_date\": \"2019-02-04 19:18:00\", \"day_of_week\": \"Monday\", \"month\": \"2\", \"street\": \"ZEIGLER ST\", \"ucr_part\": \"Part Two\", \"long\": \"-71.08200715\", \"year\": \"2019\", \"lat\": \"42.32924494\", \"incident_number\": \"I192009262\", \"_id\": 5, \"offense_code_group\": \"Vandalism\", \"location\": \"(42.32924494, -71.08200715)\"}, {\"offense_description\": \"PROPERTY - ACCIDENTAL DAMAGE\", \"shooting\": null, \"district\": \"B2\", \"offense_code\": \"03106\", \"hour\": \"15\", \"reporting_area\": \"327\", \"_full_text\": \"'-02':12 '-03':13 '-71.07533873':26,28 '00':15,16 '03106':2 '15':14,20 '2':18 '2019':11,17 '327':10 '42.31601099':25,27 'accidental':7 'b2':9 'beauford':23 'damage':5,8 'i192009126':1 'ln':24 'part':21 'property':3,6 'related':4 'sunday':19 'three':22\", \"occurred_on_date\": \"2019-02-03 15:00:00\", \"day_of_week\": \"Sunday\", \"month\": \"2\", \"street\": \"BEAUFORD LN\", \"ucr_part\": \"Part Three\", \"long\": \"-71.07533873\", \"year\": \"2019\", \"lat\": \"42.31601099\", \"incident_number\": \"I192009126\", \"_id\": 7, \"offense_code_group\": \"Property Related Damage\", \"location\": \"(42.31601099, -71.07533873)\"}, {\"offense_description\": \"MISSING PERSON - LOCATED\", \"shooting\": null, \"district\": \"B2\", \"offense_code\": \"03502\", \"hour\": \"8\", \"reporting_area\": \"281\", \"_full_text\": \"'-02':12 '-04':13 '-71.08051941':26,28 '00':16 '03502':2 '08':14 '2':18 '2019':11,17 '281':10 '33':15 '42.32696802':25,27 '8':20 'b2':9 'greenville':23 'i192009058':1 'located':5,8 'missing':3,6 'monday':19 'part':21 'person':4,7 'st':24 'three':22\", \"occurred_on_date\": \"2019-02-04 08:33:00\", \"day_of_week\": \"Monday\", \"month\": \"2\", \"street\": \"GREENVILLE ST\", \"ucr_part\": \"Part Three\", \"long\": \"-71.08051941\", \"year\": \"2019\", \"lat\": \"42.32696802\", \"incident_number\": \"I192009058\", \"_id\": 8, \"offense_code_group\": \"Missing Person Located\", \"location\": \"(42.32696802, -71.08051941)\"}]"

data_url = "https://data.boston.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%2212cb3883-56f5-47de-afa5-3b1cf61b257b%22"

with urllib.request.urlopen(data_url) as url:
    python_obj = json.loads(url.read().decode())["result"]["records"]

    #print(len(python_obj["result"]["records"]))

    for object in python_obj:
        if (object["month"] and object["year"] and object["occurred_on_date"] and object["lat"] and object["long"]):
            print("")
            print("Date (mm/dd/yyyy): " + object["month"] + "/" + object["occurred_on_date"][8:10] + "/"+object["year"])
            print("Latitude: " + object["lat"])
            print("Longitude: " + object["long"])
    print("\n")

    # def distBetween(lon1, lat1, lon2, lat2):
    #     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    #     # haversine formula
    #     dlon = lon2 - lon1
    #     dlat = lat2 - lat1
    #     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    #     c = 2 * asin(sqrt(a))
    #     r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    #     return(c * r)
    #
    # def filterByRadius(radius):
    #     for object in python_obj:
    #         if distBetween(object["long"], object["lat"], userLon, userLat) <= radius:
    #def geoJson():
