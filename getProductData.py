import http.client, urllib.request, urllib.parse, urllib.error, base64, json


def getProductData(params):
    Results={}
    headers = {
        # Request headers
        'Product-Subscription-Key': '0f9b424c7a6b4e2e9fc2f88af01d40c0',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSIsImtpZCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSJ9.eyJhdWQiOiJodHRwczovL3dlZ21hbnMtZXMuYXp1cmUtYXBpLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0Zi8iLCJpYXQiOjE1MTcxNDQ3MzksIm5iZiI6MTUxNzE0NDczOSwiZXhwIjoxNTE3MTQ4NjM5LCJhaW8iOiJZMk5nWUxqajhVejNnMUc2a2JISUhyWmJZam8zQUE9PSIsImFwcGlkIjoiMmZhOGY3MWYtY2VjNS00OWU5LWJkMGEtMjI3ODBkYzI2YTliIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMTMxOGQ1N2YtNzU3Yi00NWIzLWIxYjAtOWIzYzM4NDI3NzRmLyIsIm9pZCI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInN1YiI6ImY0NTIwYmRmLTc1NWItNGY5Yi1iNWJkLTI4NGJiYTI2MTEwOSIsInRpZCI6IjEzMThkNTdmLTc1N2ItNDViMy1iMWIwLTliM2MzODQyNzc0ZiIsInV0aSI6InBUUkJ3STBVdDBHaWpTX2hJcmdVQUEiLCJ2ZXIiOiIxLjAifQ.HyQBrW2YTHQYfHpRz6vphxcul8gCJKQEso_tuZOjPspUmff0nRdBnNTlQ370G5BWjibKj9OmWlHFsUZFpQEVkZFzujfuEZ1-PXBK7SB6EQtDchfG-H6YCWjwngXMt8RzQYf9zEcRZedO1NMnr3ET_ls4CDpKCS5m8vdeLjgh7fZbLAIU84NmXB3NyxkomgJmsIjfwvLYn0g8L8BGyxoXDKa9cZD7xOvMbmuHmfDZ9VZrtc6HaUWNlJimXDtX9ujq136HgQGEK0gVKabFi303fKOJ14GNCOWGlBxOoVPFRecYDUxzwQs6MAV7hi6kfXPHu5tI0w0UcG9-CZgKrhV0kA'
    }

    #params = 'sugar'

    try:
        conn = http.client.HTTPSConnection('wegmans-es.azure-api.net')
        conn.request("GET", "/productpublic/products/search?criteria="+params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(response.status)
        if(response.status == 200):
            print(data)
            jsonData = json.loads(data)
            Results = jsonData['Results']
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


    return Results

    ####################################
