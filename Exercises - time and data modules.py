import datetime



print(dir(datetime))

# date generation

from datetime import date

datetime_object = date(2013,5,10)
print(datetime_object)
print(datetime_object.month)

a = date.today().month
print(a)


#time generation

from datetime import time

b = time(3,45,16)
print(b)
print(b.second)

# date + time generation

from datetime import datetime

c= datetime(2020,7,29, 12, 25)
print(c)

#counting diffence between two dates

from datetime import datetime, date

t1 = date(2020,3,23)
t2 = date.today()
dif = t2-t1
print(dif)
print(type(dif))


from datetime import timedelta

t1 = timedelta(days =19, hours = 1, seconds = 33)
t2 = timedelta(2,5,1, 33)
print (t1)
print (t2)
print (t1 - t2)
print (f't1 in seconds: {t1.total_seconds()}')


#test

today= date.today()
fut = timedelta(days = 10)

print (today + fut)
