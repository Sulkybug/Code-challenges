'''
You are trying to determine which of two apartments has a larger balcony. Both balconies are rectangles, and you have the length and width, but you need the area.

Task 
Evaluate the area of two different balconies and determine which one is bigger.

Input Format 
Your inputs are two strings where the measurements for height and width are separated by a comma. The first one represents apartment A, the second represents apartment B.

Output Format: 
A string that says whether apartment A or apartment B has a larger balcony.

Sample Input 
'5,5'
'2,10'

Sample Output 
Apartment A
'''

apartmentA = input().split(",")
apartmentB = input().split(",")

areaA = int(apartmentA[0])* int(apartmentA[1])

areaB = int(apartmentB[0])* int(apartmentB[1])

if areaA > areaB:
 print("Apartment A")

elif areaA == areaB:
 print("Same Area")
 
else:
 print("Apartment B")
