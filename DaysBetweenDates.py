'''
You need to calculate exactly how many days have passed between two dates.

Task:  
Calculate how many days have passed between two input dates, and output the result. 

Input Format: 
Two strings that represent the dates, first date should be the older date. 
Date format: Month DD, YYYY

Output Format: 
A number representing the number of days between the two dates.

Sample Input: 
August 15, 1979
June 15, 2018

Sample Output: 
14184
'''
from datetime import date
import calendar
months = []

for i in range(1, 13):
 months.append(calendar.month_name[i])

dateOne= input().replace(",","").split(" ")
dateTwo= input().replace(",","").split(" ")

for i in range(12):
 if dateOne[0] == months[i]:
  dateOne[0] = i + 1
 if dateTwo[0] == months[i]:
  dateTwo[0] = i + 1

dateOne[1]= int(dateOne[1])
dateOne[2]= int(dateOne[2])
dateTwo[1]= int(dateTwo[1])
dateTwo[2]= int(dateTwo[2])

f_date = date(dateOne[2], dateOne[0], dateOne[1])
l_date = date(dateTwo[2], dateTwo[0], dateTwo[1])
difference = l_date - f_date

print(difference.days)
