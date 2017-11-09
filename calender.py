date1=input("Enter the date in dd/mm/yyyy format: ")
date=date1.split('/')
day,month2,year,odd_days,i,j,leap,k=int(date[0]),int(('0'+date[1])[-2:]),int(date[2]),0,0,0,0,''
if year%4==0:
    if year%100==0:
        if year%400==0:
            leap=1
    leap=1
odd_days+=(((year/400)-1)%4)*5
year2=(year-((year/100)*100))-1
odd_days+=(year2+(year2/4))%7
months={1:"jan",2:"feb",3:"mar",4:"apr",5:"may",6:"jun",7:"jul",8:"aug",9:"sep",10:"oct",11:"nov",12:"dec"}
month1=list(months.keys())
month1.sort()
while i==0:
    if month2==month1[j]:
        i=1
        break
    j+=1
month=months[j+1]
Month={"01jan":31,"02feb":28,"03mar":31,"04apr":30,"05may":31,"06jun":30,"07jul":31,"08aug":31,"09sep":30,"10oct":31,"11nov":30,"12dec":31}
Month1=list(Month.keys())
Month1.sort()
i,j=0,0
while i==0:
    if month==Month1[j][2:5]:
        i=1
        break
    k=Month1[j]
    odd_days+=Month[k]%7
    if (j==1 and leap==1):
        odd_days+=1
    j+=1
odd_days+=day%7
odd_day=odd_days%7
Day=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print("The given date occurs on",Day[odd_day])
