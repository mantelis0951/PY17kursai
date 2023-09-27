import datetime

now = datetime.datetime.today()

days_to_month = 0.03287671
seconds_to_hours = 0.00027778
seconds_to_minutes = 0.01666667
# print(now.year, now.month, now.day)
# print(now.hour, now.minute, now.second)

print(now)
print(now - datetime.timedelta(days =5))
print(now + datetime.timedelta(hours=8))
print(now.strftime("%Y %m %d, %H:%M:%S"))
