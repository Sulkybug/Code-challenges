'''
You want to take a list of numbers and find the sum of all of the even numbers in the list. Ignore any odd numbers.

Task:
Find the sum of all even integers in a list of numbers.

Input Format: 
The first input denotes the length of the list (N). The next N lines contain the list elements as integers.

Output Format: 
An integer that represents the sum of only the even numbers in the list.

Sample Input: 
9
1
2
3
4
5
6
7
8
9

Sample Output: 
20
'''

listLength = int(input())

list=[] 

for i in range(listLength):
 a=input()
 list.append(int(a))
 
#when number or inputs is unknown
"""
while(True): 
 try: 
  a=input() 
 except Exception as e: 
  break 
 list.append(int(a))
"""

result= 0
for i in list:
 if i % 2 == 0:
  result += i
  
print(result)
