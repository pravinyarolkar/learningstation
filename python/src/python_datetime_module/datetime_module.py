import datetime
print(datetime.MINYEAR, datetime.MAXYEAR)

timevar = datetime.time(2,20)

print(timevar)
print(datetime.date.today())
day = datetime.date.today()
print(day.year, day.month, day.day)

print(day.ctime())

from datetime import datetime

mydatetime = datetime(2023, 12, 15, 11, 55, 58)
print(mydatetime)
print(mydatetime.year, mydatetime.month)

from datetime import date
date1 = date(2023, 12,15)
date2 = date(2022, 12, 20)
print(date1 - date2)
date_diff = date1 - date2
print(type(date_diff))

mydatetime1 = datetime(2023, 12, 20, 14, 55, 58)
mydatetime2 = datetime(2023, 12, 15, 12, 55, 58)

print(mydatetime1 - mydatetime2)
print(type(mydatetime1 - mydatetime2))