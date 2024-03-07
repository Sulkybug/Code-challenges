'''
You want to completely cover a flat door on both sides with duct tape. You need to know how many rolls of duct tape to buy when you go to the store.

Task: 
Given the height and width of the door, determine how many rolls of duct tape you will need (a roll of duct tape is 60 feet long and 2 inches wide and there are 12 inches in each foot). Don't forget both sides of the door!

Input Format: 
Two integers that represent the height and width of the door.

Output Format: 
An integer that represents the total rolls of duct tape that you need to buy.

Sample Input: 
7
4

Sample Output: 
6
'''

import math
len = int(input())
width = int(input())
areaDoor = (len* width)*2

rollTapeArea = (2/12)*60
numberRolls = math.ceil(areaDoor/ rollTapeArea)

print(numberRolls
