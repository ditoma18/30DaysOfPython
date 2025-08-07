# Exercises: Day 16
# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
import datetime
now = datetime.datetime.now()
print("current date and time:",now)
print("Current day:", now.day)
print("Current month:", now.month)
print("current year:", now.year)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current timestamp:", now.timestamp())

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)

# 3. Today is 5 December, 2019. Change this time string to time.
time_string = "5 December, 2019"
time_object = datetime.datetime.strptime(time_string, "%d %B, %Y")
print("Time object from string:", time_object)

# 4. Calculate the time difference between now and new year.
new_year = datetime.datetime(now.year + 1, 1, 1)
time_difference_to_new_year = new_year - now    
print("Time difference to New Year:", time_difference_to_new_year)

# 5. Calculate the time difference between 1 January 1970 and now.
epoch = datetime.datetime(1970, 1, 1)
time_difference_from_epoch = now - epoch
print("Time difference from Epoch:", time_difference_from_epoch)

#6. I can use the datetime module for:
# Time series analysis
