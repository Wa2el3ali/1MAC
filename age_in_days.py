
import datetime
import time
from IsLeap import isleap

start_time = time.clock()

def age_in_days(year, month, day):

    # Getting date of today
    d = datetime.datetime.now().strftime("%Y-%m-%d")
    today = [int(d[:4]), int(d[5:7]), int(d[8:])]            # [year, month, day]
    # print 'today', today

    # leap days
    leap_days = 0
    for i in range(year+1, today[0]):
        if isleap(i):
            leap_days += 1
    # print 'leap_days', leap_days

    # Days of in_between years
    years_in_between = (today[0]-year-1) * 365

    # Year of birth
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_after_birthday = 0
    for i in range(month, 12):
        month_after_birthday += days_of_month[i]
    if isleap(year) and month < 3 and day != 29:
        month_after_birthday += 1
    # print 'month_after_birthday', month_after_birthday

    # days after birthday
    rest_of_birth_month = days_of_month[month-1] - day
    if rest_of_birth_month < 0:
        rest_of_birth_month = 0
    # print 'rest_of_birth_month', rest_of_birth_month

    # Current year
    month_before_today = 0
    for i in range(today[1]-1):
        month_before_today += days_of_month[i]
    if isleap(today[0]) and today[1] > 2:
        month_before_today += 1
    # print 'month_before_today', month_before_today

    # days = 0
    # for i in range(today[1]-1):               # days in current year
    #     days += days_of_month[i]
    # print 'days', days
    #
    # leap_days = 0
    # for i in range(year+1, today[0]):
    #     if isleap(i):
    #         leap_days += 1
    # if isleap(today[0]) and today[2] > 2:      # if current year is leap
    #     leap_days += 1
    # if isleap(year) and month > 2:             # if year of birth is leap
    #     leap_days += 1
    #     print 'leap_days', leap_days

    age = rest_of_birth_month + month_after_birthday + years_in_between + leap_days + month_before_today + today[2]
    # print time.clock() - start_time, "seconds"
    return age, (time.clock() - start_time) * 1000

# print age_in_days(1985, 4, 13)
# print age_in_days(1995, 5, 8)
# print age_in_days(2017, 3, 19)
# print age_in_days(2000, 1, 1)
# print age_in_days(1987, 3, 5)
# print age_in_days(1999, 11, 11)
# print age_in_days(2000, 2, 29)
print age_in_days(2018, 5, 15)
# print age_in_days(1907, 7, 7), time.clock() - start_time, "seconds"

# import time
#
# start_time = time.clock()
# main()
# print time.clock() - start_time, "seconds"