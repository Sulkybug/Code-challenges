'''
If a sentence flows, the first letter of each word will be the same to the last letter of the previous word. 

Task:
Write a program that takes in a string that contains a sentence, checks if the first letter of each word is the same as the last letter of the previous word. If the condition is met, output true, if not, output false. 
Casing does not matter.

Input Format: 
A string containing a sentence of words.

Output Format: 
A string: true or false.

Sample Input:
this string gets stuck

Sample Output: 
true
'''

sentence = input().split(" ")

index = 0
result=""

for i in sentence:
#to avoid first word
 if index > 0:
#comparing first and last letter with previus word
  if sentence[index-1][len(sentence[index-1])-1] == i[0]:
   result= "true"
  else:
   result= "false"
   break
 index += 1 
 
print(result)
