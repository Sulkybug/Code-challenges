'''
You are trying to send a secret message, and you've decided to encode it by replacing every letter in your message with its corresponding letter in a backwards version of the alphabet. 
What do your messages look like?

Task: 
Create a program that replaces each letter in a message with its corresponding letter in a backwards version of the English alphabet.

Input Format: 
A string of your message in its normal form.

Output Format: 
A string of your message once you have encoded it (all lower case).

Sample Input: 
Hello World

Sample Output: 
svool dliow
'''

import string

inputMessage = input()
alphabet = list(string.ascii_lowercase)

resultMessage = ""

for i in inputMessage:
 if i == " ":
  resultMessage += " "
 else:
  indexNum = (alphabet.index(i.lower()))*-1
 
  resultMessage += alphabet[indexNum+25]

print(resultMessage)
