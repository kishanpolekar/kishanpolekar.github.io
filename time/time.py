import ntplib
from time import ctime

c=ntplib.NTPClient()
response=c.request('europe.pool.ntp.org')
print (ctime(response.tx_time))
