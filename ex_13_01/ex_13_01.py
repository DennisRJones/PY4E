import urllib.request, urllib.parse, urllib.error
import json
import ssl

#uses a database from py4e to avoid google keys
api_key = False
#if you have a google places api key, enter it here
#api_key = '.....'
# https://developers.google.com/map/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verfy_mode = ssl.CERT_NONE

#start an opperating loop for program
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #add the users location and the key to the url with
    #urllib to ensure its in correct encoding
    parms = {}
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)

    #put the client response object from an 'open'
    #request into uh and decode it into data
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    #parse a json string and convert to a python dic
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js ['status'] != 'OK':
        print('==== Failure to retrieve ====')
        print(data)
        continue

    #print json in a indented way
    #print('dumps', json.dumps(js, indent = 4))

    #retrieve required data from the json object
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('Lat:', lat, 'Lng:', lng)
    location = js["results"][0]["formatted_address"]
    print('Location', location)
