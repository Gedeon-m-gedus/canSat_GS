# # this will be merged with the cansat codes

apiKey = 'QJH42Y3NDGV1PW63'
temp = 23.1
hum = 64
alt = 1702
pres = 809

import httplib#2 as httplib
import urllib
import time

def pushdata():
    while True:
        params = urllib.urlencode({'field1': temp, 'field2': hum, 'field3': alt,'field4': pres, 'key':apiKey}) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print ("Upload status: ", response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
pushdata()