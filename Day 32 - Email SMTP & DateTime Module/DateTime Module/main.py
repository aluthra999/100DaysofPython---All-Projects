import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
date = now.date()
time = now.time()
today = now.today()

print(now)
print(year)
print(month)
print(day)
print(day_of_week)
print(date)
print(time)
print(today)
