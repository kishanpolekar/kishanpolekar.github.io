from urllib.request import urlopen
import json

to_curr='INR'
to_curr_name='Indian Rupee'
curl='https://currency-api.appspot.com/api/{}/{}.json'.format('USD',to_curr)
f3=urlopen(curl)
json_string2=json.loads(f3.read())
f3.close()
print('Price in {} = {} {}'.format(to_curr_name,to_curr,json_string2['amount']))
