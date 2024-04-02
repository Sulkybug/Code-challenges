'''
Task:
Given multiple words, you need to find the longest string that is a substring of all words. 

Input Format:
A string of words, separated by spaces. The string can also contain numbers.

Output Format:
A string, representing the longest common substring. 
If there are multiple longest common substrings, output the smallest one in alphabetical order.

Sample Input:
SoloLearn Learning LearningIsFun Learnable

Sample Output:
Learn
'''

input_list = input().split()

longest_substring = ""

for i in range(len(input_list[0])):
    for j in range(i + len(longest_substring) + 1, len(input_list[0]) + 1):
        substring = input_list[0][i:j]
        if all(substring in word for word in input_list):
            longest_substring = max(longest_substring, substring, key=lambda x: (len(x), x))

print(longest_substring)
