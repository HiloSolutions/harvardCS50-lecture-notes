# importing the module
import csv
 
# open the file in read mode
filename = open('nyc_weather.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
date = []
temp = []

 
# iterating over each row and append
# values to empty list
for col in file:
    date.append(col['date'])
    temp.append(col['temperature(F)'])
 
# printing lists
print('Key:', date)
print('Value:', temp)

# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
