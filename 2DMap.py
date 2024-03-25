'''
You're given a representation of a 5x5 2D map, and if you can only move left, right, up, or down, determine how many moves you would have to make to get between two points on the map.

Task:
 Determine the total number of moves that are needed between two points on a map.  The points that you move between are marked with a P and the spaces in between are marked with X.

Input Format: 
A string that represents the 2D space starting at the top left.  Each level from top to bottom is separated by a comma.

Output Format: 
An integer that represents the total number of moves that you had to make.

Sample Input: 
XPXXX,XXXXX,XXXXX,XXXPX,XXXXX

Sample Output: 
5
'''

myMap = input().split(",")

columnS = 0
rowS = 0
columnE = 0
rowE = 0
status = False

for i in range(5):
    for index in range(5):
        if myMap[i][index] == "P" and not status:
            columnS = index
            rowS = i
            status = True

        if myMap[i][index] == "P" and status:
            columnE = index
            rowE = i

# Calculate the absolute difference between column and row positions
column_diff = abs(columnE - columnS)
row_diff = abs(rowE - rowS)

# Total number of moves is the sum of column and row differences
result = column_diff + row_diff

print(result)
