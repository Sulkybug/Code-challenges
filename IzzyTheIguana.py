'''
Your pet Iguana has run away, and you found it up in a tree! It will come down right away if you brought the right snacks, but if you don't have enough, you will have to wait. You need 10 total snack points to bring it down. Lettuce is worth 5, Carrot is worth 4, Mango is worth 9, and Cheeseburger is worth 0.

Task: 
Evaluate whether or not you have enough snack points to convince your iguana to come down.

Input Format: 
Your input is a string that represents the snacks that you have. Snacks are separated by spaces, you can have any number of snacks, and they can repeat.

Output Format: 
A string that says 'Come on Down!' if you have enough points, or 'Time to wait' if you do not. 

Sample Input: 
Mango Cheeseburger Carrot

Sample Output:
Come on Down!
[6:28 p. m., 7/3/2024] Andrés A: snaksList = input().split(" ")

'''

snaksList = input().split(" ")
points = 0

for i in snaksList:
 if i == "Lettuce":
  points += 5
 elif i == "Carrot":
  points += 4
 elif i == "Mango":
  points += 9
  
if points < 10:
 print("Time to wait")
else:
 print("Come on Down!")
