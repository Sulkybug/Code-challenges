'''
You're interviewing to join a security team. They want to see you build a password evaluator for your technical interview to validate the input.

Task: 
Write a program that takes in a string as input and evaluates it as a valid password. The password is valid if it has at a minimum 2 numbers, 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*'), and a length of at least 7 characters.
If the password passes the check, output 'Strong', else output 'Weak'.

Input Format:
A string representing the password to evaluate.

Output Format:
A string that says 'Strong' if the input meets the requirements, or 'Weak', if not.

Sample Input: 
Hello@$World19

Sample Output: 
Strong
'''

password = input()
symbols = "!@#$%&*"

symbol_count = sum(1 for char in password if char in symbols)
number_count = sum(1 for char in password if char.isdigit())  
# Use isdigit() for numeric check

if len(password) >= 7 and symbol_count >= 2 and number_count >= 2:
    print("Strong")
else: 
    print("Weak")
