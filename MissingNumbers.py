'''
You are given a list of whole numbers in ascending order. You need to find which numbers are missing in the sequence.

Task: 
Create a program that takes in a list of numbers and outputs the missing numbers in the sequence separated by spaces.

Input Format: 
The first input denotes the length of the list (N). The next N lines contain the list elements as integers. 

Output Format: 
A string containing a space-separated list of the missing numbers.

Sample Input: 
5
2
4
5
7
8

Sample Output: 
3 6
'''

lenght = int(input())
numbList= []
# creating inputs list
for i in range(lenght):
 numbList.append(int(input()))

result = ""
#loop between real len list
for i in range(numbList[(lenght-1)]- numbList[0]):
#checking if values are not in the list
 if (i + numbList[0]) not in numbList:
  result += str(i + numbList[0]) + " "

print(result)
