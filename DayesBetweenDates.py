def isleapyear(y):
	# a function takes the year as it's input and returns,
	# "True" if it's a leap year, else it returns "False"
	#https://en.wikipedia.org/wiki/Leap_year#Algorithm
	if (y % 4) != 0:
		return False
	if (y % 100) != 0:
		return True
	if (y % 400) != 0:
		return False
	else:
		return True

def days_of_month(x):
	leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	nonleap_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if isleapyear(x):
		return leap_days
	else:
		return nonleap_days

#dividing the total period to three periods
# first:  the in between years which equals the no. of years * 365 + leap days
#Second: starting year = rest of days of starting month + rest of months in the year
#third : ending year = starting month before ending month + no. of days of ending month

def DaysBetweenDates(y1, m1, d1, y2, m2, d2):
	# assuming that starting date(d1/m1/y1) comes before ending date(d2/m2/y2):

	# First period calculations

	years_in_between = []
	n = y1 +1
	while y1 < n < y2:
		years_in_between.append(n)
		n += 1

	days_of_common_years = len(years_in_between) * 365

	#leap days calculations

	leap_days = 0
	for y in years_in_between:
		if isleapyear(y):
			leap_days += 1
	period_1 = days_of_common_years + leap_days
	# print (period_1)
	# print ('no. of in between years',days_of_common_years) 
	# print ('leap days', leap_days)
	#-----------------------

	#Second period calculations
	days_of_starting_month = days_of_month(y1)[m1-1] - d1
	if (y1 == y2):
		rest_month_of_starting_year = days_of_month(y1)[m1:m2-1]
	else:
		rest_month_of_starting_year = days_of_month(y1)[m1:]

	#rest of starting year calculations
	rest_of_starting_year = 0
	for i in rest_month_of_starting_year:
		rest_of_starting_year += i

	period_2 = days_of_starting_month + rest_of_starting_year
	# print (days_of_starting_month, rest_month_of_starting_year , rest_of_starting_year, period_2)
	# print ('days_of_starting_month', days_of_starting_month)
	# print ('rest_month_of_starting_year', rest_month_of_starting_year)
	# print ('rest_of_starting_year', rest_of_starting_year)
	#------------------------

	#third period calculations
	if y1 == y2:
		month_befor_ending_month = days_of_month(y2)[m1:m2-1]
	else:
		month_befor_ending_month = days_of_month(y2)[:m2-1]
	days_before_ending_date = 0
	for i in month_befor_ending_month:
		days_before_ending_date += i
	period_3 = days_before_ending_date + d2
	# print ('days_before_ending_date', days_before_ending_date)
	# print ('month_befor_ending_month', month_befor_ending_month)

	#Final result

	if y1 == y2:
		if m1 == m2:
			return (d2 - d1)
		else:
			days = period_1 + period_2 + d2
			return days
		return days

	days = period_1 + period_2 + period_3

	return days

print (DaysBetweenDates(2012,1,1,2012,2,28))