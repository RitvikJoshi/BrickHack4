####################################

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64


def getLocationData(itemNumber):

    headers = {
        # Request headers
        'Product-Subscription-Key': '{subscription key}',
        'Authorization': '{access token}',
    }

    params = itemNumber

    try:
        conn = http.client.HTTPSConnection('wegmans-es.azure-api.net')
        conn.request("GET", "/productpublic/productlocations/"+params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

        ####################################


def storeLocation(storeNumber):
    headers = {
        # Request headers
        'Location-Subscription-Key': '{subscription key}',
        'Authorization': '{access token}',
    }

    params = storeNumber

    try:
        conn = http.client.HTTPSConnection('wegmans-es.azure-api.net')
        conn.request("GET", "/locationpublic/location/stores/"+params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    ####################################