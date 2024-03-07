'''
You run a hovercraft factory. Your factory makes ten hovercrafts in a month. Given the number of customers you got that month, did you make a profit? It costs you 2,000,000 to build a hovercraft, and you are selling them for 3,000,000. You also pay 1,000,000 each month for insurance.

Task: 
Determine whether or not you made a profit based on how many of the ten hovercrafts you were able to sell that month.
 
Input Format: 
An integer that represents the sales that you made that month.

Output Format: 
A string that says 'Profit', 'Loss', or 'Broke Even'.

Sample Input: 
5

Sample Output: 
Loss
'''

sales = int(input())

price_production_unit = 2000000
cost_sale_unit = 3000000
insurance = 1000000

production = 10 * price_production_unit 
profit = sales * cost_sale_unit 
balance = profit - insurance - production 

if balance > 0:
 print('Profit')
 
elif balance < 0:
 print('Loss') 
 
else:
 print('Broke Even')
