import http.client, urllib.request, urllib.parse, urllib.error, base64,json

def getPriceData(ItemNumber):
    Results={}
    headers = {
        # Request headers
        'Price-Subscription-Key': '0f9b424c7a6b4e2e9fc2f88af01d40c0',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSIsImtpZCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSJ9.eyJhdWQiOiJodHRwczovL3dlZ21hbnMtZXMuYXp1cmUtYXBpLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0Zi8iLCJpYXQiOjE1MTcxMjg0NjcsIm5iZiI6MTUxNzEyODQ2NywiZXhwIjoxNTE3MTMyMzY3LCJhaW8iOiJZMk5nWUZnOXB5SmlsOFNDZXhGVlBycDdOL2FLQWdBPSIsImFwcGlkIjoiMmZhOGY3MWYtY2VjNS00OWU5LWJkMGEtMjI3ODBkYzI2YTliIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMTMxOGQ1N2YtNzU3Yi00NWIzLWIxYjAtOWIzYzM4NDI3NzRmLyIsIm9pZCI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInN1YiI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInRpZCI6IjEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0ZiIsInV0aSI6Ii1oWjJGRUJTQlVXZVRxYjZDNUFTQUEiLCJ2ZXIiOiIxLjAifQ.iUKc5lQ2PQ8vm9IsBL4QbDDKWbuPbO0_KoGFkYR-vBh2MjvYa49Lh_jgllzyTFbL1B-Eo3gCbuBIrArlaBjy9pxzCaavEjCkBl2Qeqcsn2lOBCw_xXN1gxOhUmL3KFS66B60j2nQaWvP8aS28byHXWgvYwadlmw4NDZw4sy4fduNIm39mPHbGWeDoxA_bwwlbYLFDewGgQhwV0paqlf6bdXGTVULoXrd6eV8Humngw1Pq3uk78usz1-3t_MD-_pWHs3xxylT3B5-us4h6V9dwRKbsRw7eeFFxlPupO2noXLiGiQSw32U6S6463hqNehu9ULuTMvPB2wbLp6Hw9axpA'
    }

    params = ItemNumber

    try:
        conn = http.client.HTTPSConnection('wegmans-es.azure-api.net')
        conn.request("GET", "/pricepublic/pricing/current_prices/"+str(params), "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        jsonData = json.loads(data)
        #print(jsonData)

        #print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return jsonData
