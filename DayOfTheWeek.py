'''
You receive a date and need to know what day of the week it is. 
 
Task: 
Create a program that takes in a string containing a date, and outputs the day of the week.

Input Format: 
A string containing a date in either "MM/DD/YYYY" format or "Month Day, Year" format.

Output Format: 
A string containing the day of the week from the provided date.

Sample Input: 
11/19/2019

Sample Output: 
Tuesday
'''

import datetime 
import calendar

date = input()
months = []

if "/" in date:
    date = date.split("/")
else:
    date = date.replace(",", "").split(" ")
 
for i in range(1, 13):
    months.append(calendar.month_name[i])

for i in range(12):
    if date[0] == months[i]:
        date[0] = i + 1
    if date[1] == months[i]:
        date[1] = i + 1

def findDay(date):
    month, day, year = (int(i) for i in date)
    dateInfo = datetime.date(year, month, day)    
    dayNumber = dateInfo.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[dayNumber]

print(findDay(date))
