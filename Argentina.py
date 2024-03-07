'''
You are in a hat store in Argentina! The prices are listed in US Dollars and Argentinian Pesos. You have both, but you want to make sure you pay the lower price! Do you pay in Dollars or Pesos? The exchange rate is 2 cents for every Peso.

Task 
Create a program that takes two prices and tells you which one is lower after conversion.

Input Format 
Two integer values, the first one is the price in Pesos and the second one is the price in Dollars.

Output Format 
A string that says which currency you should make the purchase in ('Dollars' or 'Pesos').

Sample Input 
4000
100

Sample Output 
Pesos
'''
pesos = int(input())
dollars = int(input())
exchange = pesos * 0.02

if exchange < dollars:
 print('Pesos')
else:
 print('Dollars')
