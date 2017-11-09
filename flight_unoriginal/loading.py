
import time
import os
import sys
import ntplib
from time import ctime

os.system('clear')
#---------------------------------------------- time
c=ntplib.NTPClient()
response=c.request('europe.pool.ntp.org')
ctime=ctime(response.tx_time).split()
print ('Current date and time: {0} {1} {2}, {4}. {3}'.format(ctime[0],ctime[1],ctime[2],ctime[3],ctime[4]))

#---------------------------------------------- loading_screen
airline_name='/\/\/\ MID-WESTERN AIRLINES'
toolbar_width=len(airline_name)

print ('\tWELCOME TO')
#setup toolbar
sys.stdout.write('%s' % ('' * toolbar_width))
sys.stdout.flush()

for i in range(toolbar_width):
    time.sleep(0.12)
    # update the bar
    sys.stdout.write(airline_name[i])
    sys.stdout.flush()

sys.stdout.write('\n')
#---------------------------------------------- location
from urllib.request import urlopen
import json

# Automatically geolocate the connecting IP
f = urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string) #json.loads converts byte stream to dict
print('Your current location is: {},{},{}'.format(location['city'],location['region_code'],location['country_code']))
#---------------------------------------------- nearest_airport
airport_url='http://maps.googleapis.com/maps/api/geocode/json?address=airport,{}&sensor=false'.format(location['city'])
f1 = urlopen(airport_url)
json_string1 = f1.read()
f1.close()
location1 = json.loads(json_string1)['results']
print('Nearest airport: ',location1[0]['formatted_address'])

#---------------------------------------------- currency
f2=open("Country Currency Code Mappings.txt","r")
to_curr='USD'
to_curr_name='USD'
rec=f2.readline()
while rec:
    r=rec.split(',')
    if r[1]==location['country_code']:
        to_curr=r[3].rstrip('\n')
        to_curr_name=r[2]
        break
    rec=f2.readline()
f2.close()
curl='https://currency-api.appspot.com/api/{}/{}.json'.format('USD',to_curr)
f3=urlopen(curl)
json_string2=json.loads(f3.read())
f3.close()
print('Price in {} = {} {}'.format(to_curr_name,to_curr,json_string2['amount']))

#---------------------------------------------- seats
ffirstnos=[]
fbusinessnos=[]
feconomynos=[]

fbusiness=4*(int(input('Enter the number of business class rows in the flight: ')))
bus_seats,first_seats,eco_seats=['A','B','E','F'],['A','B','E','F'],['A','B','C','D','E','F']
for i in range(fbusiness//4):
    for j in range(4):
        fbusinessnos.append(str(i+1)+bus_seats[j])
ffirst=4*(int(input('Enter the number of first class rows in the flight: ')))
for i in range(ffirst//4):
    for j in range(4):
        ffirstnos.append(str(i+1)+first_seats[j])
feconomy=6*(int(input('Enter the number of economy class rows in the flight: ')))
for i in range(feconomy//6):
    for j in range(6):
        feconomynos.append(str(i+1)+eco_seats[j])

print(ffirstnos)
print(fbusinessnos)
print(feconomynos)

#----------------------------------------------
