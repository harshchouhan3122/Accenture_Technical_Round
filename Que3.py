'''
3. Write a function to validate if the provided two strings are anagrams or not. If the two strings are anagrams, then return ‘yes’. Otherwise, return ‘no’.
Input:

Input 1: 1st string
Input 2: 2nd string

Output:
(If they are anagrams, the function will return ‘yes’. Otherwise, it will return ‘no’.)

Example

Input 1: Listen
Input 2: Silent

Output:
Yes

Explanation

Listen and Silent are anagrams (an anagram is a word formed by rearranging the letters of the other word).
'''

# Check two strings are anagrams or not
# def anagram(str1,str2):
#     list(str1.lower()).sort()
#     list(str2.lower()).sort()
#     str1 = "".join(str1)
#     str1 = "".join(str2)

#     if str1:
#         return "YES"
#     else:
#         return "NO"

def anagram(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if (sorted(str1)==sorted(str2)):
        return "YES"
    else:
        return "NO"

# Input
str1 = input()
str2 = input()

# Output
print(anagram(str1,str2))