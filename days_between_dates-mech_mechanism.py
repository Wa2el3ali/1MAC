from IsLeap import isleap
import time

start_time = time.clock()

days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def next_day(y, m, d):
    d += 1
    if isleap(y):
        if d > leap_days_of_month[m-1]:
                d = 1
                m += 1
    elif d > days_of_month[m-1]:
                d = 1
                m += 1
    if m > 12:
            m = 1
            y += 1
    return y, m, d
# print next_day(2013, 1, 30)


def is_after(y1, m1, d1, y2, m2, d2):
    if y2 > y1:
        return True
    if y2 == y1:
        if m2 > m1:
            return True
    if m2 == m1:
        if d2 > d1:
            return True
    return False
# print is_after(2013, 6, 28, 2013, 6, 29)


def days_between_dates(y1, m1, d1, y2, m2, d2):

    assert not is_after(y2, m2, d2, y1, m1, d1)
    days = 0
    n = [y1, m1, d1]

    # if not is_after(n[0], n[1], n[2], y2, m2, d2) and [y1, m1, d1] != [y2, m2, d2]:
    #     return -1

    while is_after(n[0], n[1], n[2], y2, m2, d2):
        n = next_day(n[0], n[1], n[2])
        # print n
        days += 1

    return days, (time.clock() - start_time) * 1000

print days_between_dates(2018, 5, 5, 2018, 6, 9)