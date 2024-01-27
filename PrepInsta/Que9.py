'''
Question:9 
(Asked in Accenture Offcampus 1 Aug 2021, Slot 1) 
Implement the following functions.a
Get It or Regret It Sale is Live!l To get 80% discount use coupon code 
PRIME . 9 9 ? up Checkout Prime 
The function accepts a string “str” of length 'n’, that 
contains alphabets and hyphens (-). Implement 
the function to move all hyphens(-) in the string to the 
front of the given string. 
NOTE:- Return null if str is null. 
Example :- 
+ Input: 
o str.Move-Hyphens-to-Front 
* Qutput: 
o —MoveHyphenstoFront 
Explanation:- 
The string “Move-Hyphens -to-front” has 3 hyphens (-), which are moved to the front of the string, this 
output is “— MoveHyphen” 
Sample Input 
s Str: String-Compare 
Sample Output- 
¢ -StringCompare 
'''

def removeHyphens(str):
    hyphens = []
    string = []
    for i in str:
        if i == "-":
            hyphens.append(i)
        else:
            string.append(i)
    result = "".join(hyphens) + "".join(string)
    return result


# Inputs 
str1 = "Move-Hyphens-to-Front"
# Output : ---MoveHyphenstoFront
str2 = "String-Compare"


# Output
print(removeHyphens(str1))
print(removeHyphens(str2))
