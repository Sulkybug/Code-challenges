'''
You are given a list of names for a fundraiser, but you need to keep the names relatively anonymous. You are tasked with getting the initials for each name provided.

Task: 
Given a list of first and last names, take the first letter from each name to create initials and output them as a space-separated string.

Input Format: 
The first input denotes the number of names in the list (N). The next N lines contain the list elements as strings. 

Output Format: 
A string containing the initials of each name in the original list, separated by spaces.

Sample Input: 
3 
Nick Dunburry
Tommy Newborne
David James

Sample Output: 
ND TN DJ
'''

names = int(input())
namesList= []

for i in range(names):
 namesList.append(input())

initials = ""
for i in namesList:
 name = i.split(" ")
 initials += f"{name[0][0]}{name[1][0]} "

print(initials)
