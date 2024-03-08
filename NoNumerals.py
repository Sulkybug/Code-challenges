'''
You write a phrase and include a lot of number characters (0-9), but you decide that for numbers 10 and under you would rather write the word out instead. Can you go in and edit your phrase to write out the name of each number instead of using the numeral? 

Task: 
Take a phrase and replace any instances of an integer from 0-10 and replace it with the English word that corresponds to that integer.

Input Format: 
A string of the phrase in its original form (lowercase).

Output Format: 
A string of the updated phrase that has changed the numerals to words.

Sample Input: 
i need 2 pumpkins and 3 apples

Sample Output: 
i need two pumpkins and three apples
'''

input = input()
arr= input.split(" ")

result = ""
for i in arr:
 if i == "1":
  result += "one "
 elif i == "2":
  result += "two "
 elif i == "3":
  result += "three "
 elif i == "4":
  result += "four "
 elif i == "5":
  result += "five "
 elif i == "6":
  result += "six "
 elif i == "7":
  result += "seven "
 elif i == "8":
  result += "eight "
 elif i == "9":
  result += "nine "
 elif i == "0":
  result += "zero "
 elif i == "10":
  result += "ten "
 else:
  result += i + " "
print(result)
