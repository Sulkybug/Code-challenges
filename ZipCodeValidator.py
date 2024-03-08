'''
As headmaster of the post office, sometimes people write zip codes that don't exist or zip codes that are not valid.  
You are tasked with making a system to check if the inputted zip code is a valid zip code. 

Task:
Write a program that takes in a string representing a zip code. Output true or false if it is a valid zip code or not. 
A valid zip code is only numbers, must be 5 characters in length, and contain no spaces.

Input Format: 
A string containing a zip code.

Output Format: 
A string: true is the input is a valid zip code, or false, if it is not. 

Sample Input: 
752f78

Sample Output: 
false
'''

zipcode = input()

if zipcode.isdigit() and len(zipcode) == 5:
 print("true")
else:
 print("false")
