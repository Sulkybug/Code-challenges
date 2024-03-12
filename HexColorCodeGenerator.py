'''
You are starting a new company and unfortunately that means you can no longer rely on the free hex-color code software you used to rely on. It’s time to put your skills to the test and create one from the ground up!

Task: 
Create a function that accepts three integers that represent the RGB (red, green, blue) values and outputs the hex-code representation.

Input Format: 
Three integers that represent RGB values.

Output Format: 
The hexadecimal color code string that corresponds with the entered RGB values.

Sample Input: 
100 
200 
233

Sample Output: 
#64c8e9
'''

r = int(input())
g = int(input())
b = int(input())

hex= '#'

codes = {10:"a", 11:"b", 12:"c", 13:"d",14:"e", 15:"f"}
 
def hexTransform (color):
 colorHex = str(round((color/16),2)).split(".")
 colorHex[1] = str(int((((color/16)- int(colorHex[0]))*16)))
 
 hex=""

 for i in colorHex: 
  if int(i)<=9:
   hex += i
  elif int(i)>9:
   for key, value in codes.items():
    if int(i) == key:
     hex += value
 return hex
  
rHex = hexTransform(r)
gHex = hexTransform(g)
bHex = hexTransform(b)

print(hex + rHex + gHex + bHex)
