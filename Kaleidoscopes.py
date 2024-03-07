'''
You sell souvenir kaleidoscopes at a gift shop, and if a customer buys more than one, they get a 10% discount on all of them!
Given the total number of kaleidoscopes that a customer buys, let them know what their total will be. Tax is 7%. All of your kaleidoscopes cost the same amount, 5.00.

Task: 
Take the number of kaleidoscopes that a customer buys and output their total cost including tax and any discounts.

Input Format: 
An integer value that represents the number of kaleidoscopes that a customer orders.

Output Format: 
A number that represents the total purchase price to two decimal places.

Sample Input: 
4

Sample Output: 
19.26
'''

NumbKaleido = int(input())
total= NumbKaleido * 5
discount = (total)*10/100

if NumbKaleido > 1:
 tax = (total-discount)*7/100
 total = round(total + tax - discount, 2)
 print(total)
else:
 tax = (total*7)/100
 total = total + tax
 print(total)
