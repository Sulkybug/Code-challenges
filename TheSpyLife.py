'''
You are a secret agent, and you receive an encrypted message that needs to be decoded. The code that is being used flips the message backwards and inserts non-alphabetic characters in the message to make it hard to decipher.

Task: 
Create a program that will take the encoded message, flip it around, remove any characters that are not a letter or a space, and output the hidden message.

Input Format:  
A string of characters that represent the encoded message.

Output Format: 
A string of character that represent the intended secret message.

Sample Input: 
d89%l++5r19o7W *o=l645le9H

Sample Output: 
Hello World
'''

import re
cryptedMessage = input()

message= ""
for i in cryptedMessage:
 message = i+message
 
result = re.sub('[^a-zA-Z\s]', '', message )
print(result)
