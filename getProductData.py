####################################

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json


def getProductData(params):
    Results={}
    headers = {
        # Request headers
        'Product-Subscription-Key': '0f9b424c7a6b4e2e9fc2f88af01d40c0',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSIsImtpZCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSJ9.eyJhdWQiOiJodHRwczovL3dlZ21hbnMtZXMuYXp1cmUtYXBpLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0Zi8iLCJpYXQiOjE1MTcxMDIzNjAsIm5iZiI6MTUxNzEwMjM2MCwiZXhwIjoxNTE3MTA2MjYwLCJhaW8iOiJZMk5nWURnY2RQQks2cFZ5anRmL0pHYWt0ajI5RGdBPSIsImFwcGlkIjoiMmZhOGY3MWYtY2VjNS00OWU5LWJkMGEtMjI3ODBkYzI2YTliIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMTMxOGQ1N2YtNzU3Yi00NWIzLWIxYjAtOWIzYzM4NDI3NzRmLyIsIm9pZCI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInN1YiI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInRpZCI6IjEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0ZiIsInV0aSI6IlNGU2FNSlhUb0Vxb1BZYnFWZVlPQUEiLCJ2ZXIiOiIxLjAifQ.EL0LnISNspeyckrMTI6crhu0Kxd_2eMHKAE1DEwbYonAZRmICPPpgAEunIFTJUx799Za6TXymUcFdo0awWAYQq1N-7ihXygsHARwrZYuIcTdTJG_8FQ-qDKurdGZGXJcQf2sVJH6Q9YVPfDjpjDm_H8MVuk4EKdzlGhWMLgfX1hlk_kXrf2F2ugSHbKKjjY2SVXYtwmFUlnntHafUnvSf66XIkQ-sm1xVDk4PWVjnkHl00wrNe05P2ffZxiEMw2uk9kDch7vOWRoctl2r4xbWiwP_ONihRS_5osgDaOS1Uf4g4c8QESi9ts--d1PIgzaQ32lQdEzs49JTf5cBmJx6w',
    }

    #params = 'sugar'

    try:
        conn = http.client.HTTPSConnection('wegmans-es.azure-api.net')
        conn.request("GET", "/productpublic/products/search?criteria="+params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        jsonData = json.loads(data)
        Results = jsonData['Results']
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


    return Results

    ####################################
