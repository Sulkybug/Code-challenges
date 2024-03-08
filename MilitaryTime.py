'''
You want to convert the time from a 12 hour clock to a 24 hour clock. If you are given the time on a 12 hour clock, you should output the time as it would appear on a 24 hour clock.  

Task:  
Determine if the time you are given is AM or PM, then convert that value to the way that it would appear on a 24 hour clock.

Input Format: 
A string that includes the time, then a space and the indicator for AM or PM.

Output Format: 
A string that includes the time in a 24 hour format (XX:XX)

Sample Input: 
1:15 PM

Sample Output: 
13:15
'''

time = input()
arr = time.split()

if arr[1] == "AM":
 print(arr[0])
else:
 militar= arr[0].split(":")
 militar = str(int(militar[0])+12) + ":" + militar[1]
 print(militar)
