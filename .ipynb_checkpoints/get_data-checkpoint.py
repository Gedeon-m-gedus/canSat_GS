# this will be merged with the user interface codes

import thingspeak
import json

ch = thingspeak.Channel(id=1285446, api_key='AR5QVQ499RV99VD7',fmt='json')
data_from_thingspeak=ch.get({})
data_list_from_thingspeak=data_from_thingspeak.split(",")
data_list_from_thingspeak=data_from_thingspeak.split(",")

print(data_list_from_thingspeak)

temp = []
hum = []
alt = []
pres = []

i = 12
while i < len(data_list_from_thingspeak):
    #print(data_list_from_thingspeak[i:][2:6])
    for line in (data_list_from_thingspeak[i:][2:6]):
        data = line.split('"')
        data_entry = float(data[3])
        field = data[1]
        if field == 'field1':
            temp.append(data_entry)

        if field == 'field2':
            hum.append(data_entry)

        if field == 'field3':
            alt.append(data_entry)

        if field == 'field4':
            pres.append(data_entry)
    i += 6

print(temp,'\n',hum,'\n',alt,'\n',pres)