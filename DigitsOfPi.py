'''
The constant Pi is defined as the ratio of a circle's circumference to its diameter.
Pi is an irrational number, meaning that it's digits never end or repeat in any known way. 

Task:
Given an integer N as input, find and output the Nth decimal digit of Pi.

Input Format:
An integer: 0<N<1000

Output Format: 
An integer, representing the Nth decimal digit of Pi.

Sample Input:
12

Sample Output:
9
'''

from mpmath import mp

decimal = int(input())
mp.dps = decimal + 2

pi_str = str(mp.pi)
nth_digit = pi_str[decimal + 1]

print(nth_digit)
