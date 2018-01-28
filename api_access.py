import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
headers = {
    # Request headers

    'Product-Subscription-Key': '637b5db2be95435eae859dc7aaf52765',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSIsImtpZCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSJ9.eyJhdWQiOiJodHRwczovL3dlZ21hbnMtZXMuYXp1cmUtYXBpLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0Zi8iLCJpYXQiOjE1MTcxMDE0NzcsIm5iZiI6MTUxNzEwMTQ3NywiZXhwIjoxNTE3MTA1Mzc3LCJhaW8iOiJZMk5nWURoVnZMaEpZNDlCZDRYMm9VaFJrZlF6QUE9PSIsImFwcGlkIjoiMmZhOGY3MWYtY2VjNS00OWU5LWJkMGEtMjI3ODBkYzI2YTliIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMTMxOGQ1N2YtNzU3Yi00NWIzLWIxYjAtOWIzYzM4NDI3NzRmLyIsIm9pZCI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInN1YiI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInRpZCI6IjEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0ZiIsInV0aSI6IlFwRGJvNF9oejBxcWJLQ3RwcGNQQUEiLCJ2ZXIiOiIxLjAifQ.TmaRnPYdKoN8iDtcPSoeDVWax1JDQdbFZHGD5yHlYAi3kQFQ9c7hooiL9uAm8t0XBpE_V4qPjN-iHEJGMpyioUOExsx3q7hxgd6-eWk8WfV8HEdoGnAvHEzA1n4z2_dgfe4zxsyDpjFu9ztFmOkXBj9Qb_kE6dIqrtfE9bLcwpcmqhmeiTdXG32XpTQz3M2z8Sh19zrmd8mEsRuRfcgwJBdFOtRHGe5BE6hGh9d-1d0iGZE7o9g3SeyZtiaci1-WQTE-0qDHidab3rqccdM6lpPUi7QcaBH0nfDEGQCV0hs40D329oW6Fym6MefL1LnuMUR8OIx2_AjpztambdTa1w'}

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
    if not "error" in data:
        data = json.loads(data)
        itemID = data['Results'][0]['ItemNumber']
        #print(data)
        #print(itemID)
        conn.request("GET", "/productpublic/productavailability/"+str(itemID)+"/stores?" + item, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        data = data.decode('ASCII')
        data = json.loads(data)
        print(item+" Product Avilable\n" if len(data['StoreAvailability'])>0 else "Unavilable")
        print(data)
        #print(data)


    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))