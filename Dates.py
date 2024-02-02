#####Dates######
from datetime import datetime #IMPORTO libreria

now = datetime.now()#Todo en base a este momento
print(now.year)
print(now.month)
print(now.day)
print(now.minute)

timestamp = now.timestamp()
print(timestamp) #Formato post six

year_2024 = datetime(2025,2,1) #año mes dia

def print_date(fecha):
    print(fecha.year)
    print(fecha.month)
    print(fecha.day)
    print(fecha.minute)
    print(fecha.timestamp())

print_date(year_2024)
 
from datetime import time

current_time = time(21,6,0)

print(current_time.hour)
print(current_time.min)
print(current_time.second)

from datetime import date
#current_date = date(2024,2,1)
current_date = date.today( )
print(current_date)
print(current_date.year+1)

diff = year_2024 - now # De datetime
print(diff)


from datetime import timedelta
time_delta = timedelta(200)#Dias
segundo = timedelta(100)#Dias
print(time_delta+segundo)

