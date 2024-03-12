'''
A coyote is chasing a roadrunner and they start out 50 feet apart. If you know how fast they are both traveling, and how far the roadrunner is from safety, determine whether or not the coyote is able to catch the roadrunner. 
Both animals and the roadrunner's safe place are on a straight line.

Task: 
Determine whether or not the roadrunner made it to safety.

Input Format: 
Three integer values, the first value represents the distance the roadrunner is from safety, then the roadrunner's speed (feet/second) and then the coyote's speed (feet/second).

Output Format: 
A string that says 'Meep Meep' if the roadrunner made it, or 'Yum' if the coyote caught up to the roadrunner.

Sample Input: 
10 
5 
20

Sample Output: 
Meep Meep
'''

distanceToSafe = int(input())
roadRunnerSpeed = int(input())
coyoteSpeed = int(input())

timeRunner =(distanceToSafe)/ roadRunnerSpeed 
# 50 feet initial distance apart
timeCoyote =(distanceToSafe + 50)/ coyoteSpeed 

if timeRunner > timeCoyote:
 print('Yum')
else:
 print("Meep Meep")
