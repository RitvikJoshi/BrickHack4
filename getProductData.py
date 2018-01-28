####################################

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json


def getProductData(params):
    Results={}
    headers = {
        # Request headers
        'Product-Subscription-Key': '0f9b424c7a6b4e2e9fc2f88af01d40c0',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSIsImtpZCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSJ9.eyJhdWQiOiJodHRwczovL3dlZ21hbnMtZXMuYXp1cmUtYXBpLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0Zi8iLCJpYXQiOjE1MTcxMjg3MjAsIm5iZiI6MTUxNzEyODcyMCwiZXhwIjoxNTE3MTMyNjIwLCJhaW8iOiJZMk5nWUpDMXFOVVVXSE1wWXo3LzF1VWQzYlBUQUE9PSIsImFwcGlkIjoiMmZhOGY3MWYtY2VjNS00OWU5LWJkMGEtMjI3ODBkYzI2YTliIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMTMxOGQ1N2YtNzU3Yi00NWIzLWIxYjAtOWIzYzM4NDI3NzRmLyIsIm9pZCI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInN1YiI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInRpZCI6IjEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0ZiIsInV0aSI6ImlxNC04cDRrR1VteVdFZEczRzBSQUEiLCJ2ZXIiOiIxLjAifQ.AZOInK2QMXxeHnKY-IgPakhwoc56Eo0yzn0a8OKt0xT5qDq6l2H6HppdEBqK7WVnFS928E9Z-aFuk10sXkT7u7oB6nFL4KUoMXlnG7NIBvkLSJTiFj8qb_kpoVbA6MOV6961tkdq4oI_c0Axhea3qwoNaegjG0JZUz8n85CCEoJVSqYPo-3PaKmiBfGRxEAjCUmdoYJ6bEb9FnhTf6f-Hq36Kuls8xaU5nVCTD3xMoeS3au1Wv0qAFyyWO9dlIAjbusLewNQEFBtqCLgJgeETw4E5bXsbIOcQfLSIhonjYAJNrcOsqT6REtBehSz2baGwVUohKdjtrKsAdmp-UZB2g',
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
