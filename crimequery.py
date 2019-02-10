import requests
from urllib.parse import urlparse

#  "12cb3883-56f5-47de-afa5-3b1cf61b257b"
# https://data.boston.gov/api/3/action/datastore_search_sql?sql=SELECT * from "12cb3883-56f5-47de-afa5-3b1cf61b257b"
# https://data.boston.gov/api/3/action/datastore_search_sql?sql=SELECT * from "12cb3883-56f5-47de-afa5-3b1cf61b257b" where occurred_on_date > yesterday
def generate_query(today, past_day):
    return "SELECT * from \"12cb3883-56f5-47de-afa5-3b1cf61b257b\""


def url(today, past_day):
    return "https://data.boston.gov/api/3/action/datastore_search_sql?sql=" + generate_query(today, past_day)

def complete_get_request(today, past_day):
    URL = url(today, past_day)
    request = requests.get(url=URL)
    return request.json()
