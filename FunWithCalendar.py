'''
from datetime import datetime as dt
import pytz
import calendar
print(dt.now())  #current time
tz=pytz.timezone('Singapore')
print(dt.now(tz))
print(len(pytz.all_timezones))
print(calendar.weekday(2024,10,27))
'''
import calendar
def check_leap(y):
    if(y%400==0 or (y%100!=0 and y%4==0)):
        return True
    else:
        return False

def check_valid_date(dt,m,y,l):
    if(l):
        if(m==2):
            if(dt<30):
                return True
            else:
                return False
        else:
            if(m<8):
                if(m%2==1):
                    if(dt<32):
                        return True
                    else:
                        return False
                else:
                    if(dt<31):
                        return True
                    else:
                        return False
            else:
                if (m % 2 == 0):
                    if (dt < 32):
                        return True
                    else:
                        return False
                else:
                    if (dt < 31):
                        return True
                    else:
                        return False
    else:
        if (m == 2):
            if (dt < 29):
                return True
            else:
                return False
        else:
            if (m < 8):
                if (m % 2 == 1):
                    if (dt < 32):
                        return True
                    else:
                        return False
                else:
                    if (dt < 31):
                        return True
                    else:
                        return False
            else:
                if (m % 2 == 0):
                    if (dt < 32):
                        return True
                    else:
                        return False
                else:
                    if (dt < 31):
                        return True
                    else:
                        return False

def get_day(day_index):
    list_of_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return list_of_days[day_index]

year=int(input("Enter the year(from 1970):"))
while(year<1970):
    year=int(input("Enter year starting from 1970:"))

month=int(input("Enter the month(1-12):"))
while(month<1 or month>12):
    month=int(input("Enter the month(1-12):"))

leap=check_leap(year)

date=int(input("Enter the date:"))
while(date>0 and check_valid_date(date,month,year,leap)==False):
    date=int(input("Enter a valid date:"))
day_index=calendar.weekday(year,month,date)
day=get_day(day_index)
print(f"{date}/{month}/{year} falls on {day}")