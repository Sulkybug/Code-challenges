'''
Given a list of numbers, you want to take out all of the odd ones and leave just the even ones.

Task: 
Evaluate each number in your list to see if it is even or odd. Then, output a new list that only contains the even numbers from your original list.

Input Format: 
A string that includes all of the integer values in your list separated by spaces.

Output Format: 
A string that includes all of the even integer values from your first list separated by spaces.

Sample Input: 
8 10 19 25 5 16 12

Sample Output: 
8 10 16 12
'''

numbList = input().split(" ")
result = ""

for i in numbList:
 if int(i)%2 == 0:
  result += f"{i} "

print(result)
