url = "https://data.boston.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%2212cb3883-56f5-47de-afa5-3b1cf61b257b%22"

out = getRequest(url)

saveToFile(out)
