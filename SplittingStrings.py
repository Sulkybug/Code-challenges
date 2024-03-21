'''
You are given a word and want to split it into even parts based on a number that is provided, each half being the size of the number.

Task: 
Write a program that takes in a string, and a number as input. 
Split the string into even parts sized by the number, and output the parts separated by hyphens. 
The last part of the output will be any leftover, as the input string might not split into the provided parts evenly.

Input Format: 
Two inputs: a string and an integer.

Output Format: 
A string, representing the hyphen-separated parts.

Sample Input: 
hello
2

Sample Output: 
he-ll-o
'''

word = input()
splitNum = int(input())

count = 0
result =""
for i in word:
 count += 1
 if count == splitNum+1:
  result += f"-{i}"
  count = 1
 else:
  result += i
 
print(result)
