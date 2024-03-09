'''
An isogram is a word that has no repeating letters, whether they are consecutive or non-consecutive.  
Your job is to find a way to detect if a word is an isogram.

Task: Write a program that takes in a string as input, detects if the string is an isogram and outputs true or false based on the result.
 
Input Format: 
A string containing one word.

Output Format: 
A string: true or false.

Sample Input: 
turbulence

Sample Output: 
false
'''

word = input()
isogram = ""

for i in word:
 if word.count(i) > 1:
  isogram = "false"
  break
 else:
  isogram= "true"

print(isogram)
