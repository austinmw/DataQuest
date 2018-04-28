import time

# A Unix timestamp is a floating point value with no explicit mention of day, month, or year. This value represents the number of seconds that have passed since the "epoch", or the first second of the year 1970.

# retrieve current unix timestamp
current_time = time.time()
print(current_time)

# We can convert a timestamp to a more human-readable form using the time.gmtime() function. This function takes a timestamp as an argument, and returns an instance of the struct_time class. 
import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
# hour is UTC time (Coordinated Universal Time)
# mean solar time at 0 longitude, or Greenwich Mean Time, except doesn't follow daylight savings
current_hour = current_struct_time.tm_hour
print(current_hour)
current_month = current_struct_time.tm_mon
print(current_month)


# datetime module
import datetime

current_datetime = datetime.datetime.now()
current_year = current_datetime.year
current_month = current_datetime.month
print(current_datetime)



# timedelta
import datetime

today = datetime.datetime.now()

diff = datetime.timedelta(days = 1)

tomorrow = today + diff
yesterday = today - diff



# strftime: datetime object to formatted string
march3 = datetime.datetime(year = 2010, month = 3, day = 3)
print(march3)
pretty_march3 = march3.strftime("%b %d, %Y")
print(pretty_march3)

mystery_date = datetime.datetime(2015, 12, 31, 0, 0)
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)

# strptime: string to a datetime instance
mystery_date = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(mystery_date)


# convert posts dataset to contain datetime instances
import datetime
for i in posts:
	datetime_object = datetime.datetime.fromtimestamp(float(i[2]))   
	i[2] = datetime_object
  
# count how many of top 1000 posts user submitted in March
march_count = 0
for row in posts:
    if row[2].month == 3:
	march_count += 1

# function form
def function(n):
	count = 0
	for row in posts:
		if row[2].month == n:
			count += 1
	return count

feb_count = function(2)
aug_count = function(8)









