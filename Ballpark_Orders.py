'''
You and three friends go to a baseball game and you offer to go to the concession stand for everyone. They each order one thing, and you do as well. Nachos and Pizza both cost $6.00. A Cheeseburger meal costs $10. Water is $4.00 and Coke is $5.00. Tax is 7%.

Task 
Determine the total cost of ordering four items from the concession stand. If one of your friend’s orders something that isn't on the menu, you will order a Coke for them instead.

Input Format
You are given a string of the four items that you've been asked to order that are separated by spaces.

Output Format 
You will output a number of the total cost of the food and drinks.

Sample Input 
'Pizza Cheeseburger Water Popcorn'

Sample Output 
26.75
'''

order = input()
orderList = order.split(" ")

total = 0
#billing orderList 
for i in orderList: 
 if i == "Water":
  total += 4
 elif i == "Pizza" or i == "Nachos":
  total += 6 
 elif i == "Cheeseburger":
  total += 10
 elif i == "Coke":
  total += 5
  #if item is not available order coke
 else:
  total += 5

#adding 7% tax
total = ((7* total)/100)+ total
#display order total  
print(total)
