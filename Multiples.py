'''
You need to calculate the sum of all the multiples of 3 or 5 below a given number.

Task: 
Given an integer number, output the sum of all the multiples of 3 and 5 below that number. 
If a number is a multiple of both, 3 and 5, it should appear in the sum only once.

Input Format: 
An integer.

Output Format: 
An integer, representing the sum of all the multiples of 3 and 5 below the given input.

Sample Input: 
10

Sample Output:
23
'''

number = int(input())
#getting multiples in a list
multiples_3 = [n for n in range(number) if n % 3 == 0]
multiples_5 = [n for n in range(number) if n % 5 == 0]
#removing duplicated values in 5 List
multiples_5 = set(multiples_5 ) - set(multiples_3)
mixedList = multiples_3 + list(multiples_5)
print(sum(mixedList))
