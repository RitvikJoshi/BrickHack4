import http.client, urllib.request, urllib.parse, urllib.error, base64,json

def getPriceData(ItemNumber):
    Results={}
    headers = {
        # Request headers
        'Price-Subscription-Key': '0f9b424c7a6b4e2e9fc2f88af01d40c0',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSIsImtpZCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSJ9.eyJhdWQiOiJodHRwczovL3dlZ21hbnMtZXMuYXp1cmUtYXBpLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0Zi8iLCJpYXQiOjE1MTcxNDQ4MDUsIm5iZiI6MTUxNzE0NDgwNSwiZXhwIjoxNTE3MTQ4NzA1LCJhaW8iOiJZMk5nWURnd3hlVlFnaXVicisrQy8zbEdURW9XQUE9PSIsImFwcGlkIjoiMmZhOGY3MWYtY2VjNS00OWU5LWJkMGEtMjI3ODBkYzI2YTliIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMTMxOGQ1N2YtNzU3Yi00NWIzLWIxYjAtOWIzYzM4NDI3NzRmLyIsIm9pZCI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInN1YiI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInRpZCI6IjEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0ZiIsInV0aSI6IkNRajJPVWZabEVHNzNkWWt6b0lUQUEiLCJ2ZXIiOiIxLjAifQ.bL0UP6OvAL7wpNy203TQiSd1VVHLGsU-AO6m5QisL3700JaP9PQdcMoxRe3iVQXrB4HTKmZx-PImboPVYaLweDu6nvh3FeBrnsoBq5AXltJQu96jFjFJDNhiMtVSBpxtGbM_QsDNhMB6ZWXY1eSO-PNiiFl4Kpr7OAtBySN7fQNXIm5Y3HKxzIx6mb8VcOl32TxEPB_04bSgFDljD_dPexO9--ZKNRa1KD5kLU3aS4xb4JiLGMRukk2LeVYexuCqVMlKMTXG_9iKaGsD1LMx6v-nq7DnADkdVfuPsGzJ8r6I5mcIOosNomjNrw2460LY-2eCqePXK71Va3jNAm_wPA'
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
