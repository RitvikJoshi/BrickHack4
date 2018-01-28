import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
headers = {
    # Request headers

    'Product-Subscription-Key': '637b5db2be95435eae859dc7aaf52765',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSIsImtpZCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSJ9.eyJhdWQiOiJodHRwczovL3dlZ21hbnMtZXMuYXp1cmUtYXBpLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0Zi8iLCJpYXQiOjE1MTcwOTA0ODQsIm5iZiI6MTUxNzA5MDQ4NCwiZXhwIjoxNTE3MDk0Mzg0LCJhaW8iOiJZMk5nWUREOE80bS9KM0R1OUlmVFl5YzVUZmQ5QlFBPSIsImFwcGlkIjoiMmZhOGY3MWYtY2VjNS00OWU5LWJkMGEtMjI3ODBkYzI2YTliIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMTMxOGQ1N2YtNzU3Yi00NWIzLWIxYjAtOWIzYzM4NDI3NzRmLyIsIm9pZCI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInN1YiI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInRpZCI6IjEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0ZiIsInV0aSI6InptUnBCTGxxblVxNHNEODFnSTRNQUEiLCJ2ZXIiOiIxLjAifQ.fk3Sx3BwhYcxSa36FqWcll_wmfViKg01CYxk6wIeV8ENHiLdWM5VH4LrCDhh6DuZEWKz7OsgLBPw8e_01GupPk9g8lGQvXAbOKJ7L9q_0tLwLOxAbncLuzcYpEDpA2kKwNOgsAeSeThKlhCl_pWu1stDT1fMCHcJcYR-rwlLr5DrPV1EP3yrw1yw4Rzi2D7a8320QsV-slZl-7IaYQoEU_hBlVd0vuPdlt03p9EAye8jC1Gc0RnnCYskxWlVWdeZLsPOK4HF8rJ5NqFytWK9PQUhiMCokO2z99MLWKN7YWMgKJeLJP2dvoxQXCPopZFrRhfHLLexTUXD8cE3ZhOVAw'}

params = urllib.parse.urlencode({
})

try:
    item = "fluff"
    conn = http.client.HTTPSConnection('wegmans-es.azure-api.net')
    print(type(headers))
    conn.request("GET", "/productpublic/products/search?criteria="+item,"{body}",headers)
    response = conn.getresponse()
    data = response.read()
    data = data.decode('ASCII')
    data = json.loads(data)
    itemID = data['Results'][0]['ItemNumber']
    #print(data)
    #print(itemID)
    conn.request("GET", "/productpublic/productavailability/"+str(itemID)+"/stores?" + item, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    data = data.decode('ASCII')
    data = json.loads(data)
    print(item+" Product Avilable" if len(data['StoreAvailability'])>0 else "Unavilable")

    #print(data)


    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))