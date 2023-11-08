import calendar
from datetime import date
from datetime import datetime
from datetime import timedelta


# def count_days(year,month,day):
#     c = calendar.monthcalendar(year,month)
#     dayCount = 0
#     for tempWeek in c:
#         if tempWeek[day] != 0:
#             dayCount += 1
    
#     return dayCount


# testyear = 2023
# testmonth = 11
# testday = 0
# result = count_days(testyear, testmonth, testday)
# print(result)

texp = datetime.now() - timedelta(weeks=1)
today = date.today()
# days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# print("Tomorrow will be "+days[today.weekday()+1])

tomorrow = today+timedelta(days=1)
print(tomorrow)
tomorrow = date(today.year,today.month,today.day+1)
print(tomorrow)