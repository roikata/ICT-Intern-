import datetime
#time
time = datetime.time(4,20,1)
print(time)
print("Hour: ",time.hour)
print("Minute: ",time.minute)
print("Second: ",time.second)
print("Microsecond: ",time.microsecond)
print("tzinfo: ", time.tzinfo)

print("Earliest: ", datetime.time.min)
print("Latest: ", datetime.time.max)
print("Resolution: ", datetime.time.resolution)


import datetime

today = datetime.date.today()
print(today)
print("ctime: ", today.ctime())
print("tuple: ", today.timetuple())
print("original: ", today.toordinal())
print("year: ", today.year)
print("month: ", today.month)
print("day: ", today.day)

print("Earliest: ", datetime.date.min)
print("Latest: ", datetime.date.max)
print("Resolution: ", datetime.date.resolution)