'''
It is almost Hanukkah and the store in your town is completely out of candles! You decide to place an order online, and you talk to your friends to see who else needs candles. How many candles should you order in total for the holiday? 

Task 
Determine how many candles you need to order based on how many friends ask to join your order (each friend will need 9 candles).

Input Format 
An integer that represents the number of friends that ask to order candles with you.

Output Format 
An integer that represents the total number of candles that you need to order.

Sample Input 
4

Sample Output 
45
'''

friends = int(input())
#myself + friends * number of candles
order = (1+ friends)*9
print(order)
