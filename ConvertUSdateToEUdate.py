'''
You and your friends are going to Europe! You have made plans to travel around Europe with your friends, but one thing you need to take into account so that everything goes according to play, is that the format of their date is different than from what is used in the United States. Your job is to convert all your dates from MM/DD/YYYY to DD/MM/YYYY.

Task: 
Create a function that takes in a string containing a date that is in US format, and return a string of the same date converted to EU.

Input Format: 
A string that contains a date formatting 11/19/2019 or November 19, 2019.

Output Format: 
A string of the same date but in a different format: 19/11/2019.

Sample Input: 
7/26/2019

Sample Output: 
26/7/2019
'''

dateUS = input()
dateUS = dateUS.replace(",", "")

if "/" in dateUS:
 dateUS = dateUS.split("/")
 dateEU = dateUS[1] + "/" + dateUS[0] +       "/" + dateUS[2]
 print(dateEU)
 
else:
 dateUS = dateUS.split(" ")
 if dateUS[0] == "January":
  dateUS[0] = "1"
 elif dateUS[0] == "February":
  dateUS[0] = "2"
 elif dateUS[0] == "March":
  dateUS[0] = "3" 
 elif dateUS[0] == "April":
  dateUS[0] = "4"
 elif dateUS[0] == "May":
  dateUS[0] = "5"
 elif dateUS[0] == "June":
  dateUS[0] = "6"
 elif dateUS[0] == "July":
  dateUS[0] = "7"
 elif dateUS[0] == "August":
  dateUS[0] = "8"
 elif dateUS[0] == "September":
  dateUS[0] = "9"
 elif dateUS[0] == "October":
  dateUS[0] = "10"
 elif dateUS[0] == "November":
  dateUS[0] = "11"
 elif dateUS[0] == "December":
  dateUS[0] = "12"
  
 dateEU = dateUS[1] + "/" + dateUS[0] +       "/" + dateUS[2]
 print(dateEU)
