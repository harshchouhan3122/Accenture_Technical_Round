'''
8. Perform the function: Int operationchoices(int ¢c, int n, int a, int b). 
This function considers three positive inputs of a, b and c. 
Execute the function to get: 
(a+b) if c=1 
(a/b), if c=4 
(a-b),if c=2 
(axb) if c=3 

Example: 
Input: 
a: 12 
a: 16 
c: 1 
Output : 
28

Explanation 
C = 1, hence the function is {a + b). Hence, the output is 28. 

Sample input: 
a: 16 
b: 20
c: 2
Sample output: 
-4 
'''

def operations(a,b,c):
    if c == 1:
        return a+b
    elif c == 2:
        return a-b
    elif c == 3:
        return a*b
    elif c == 4:
        return a/b

# Input
# a = int(input())
# b = int(input())
# c = int(input())
a1, b1, c1 = 12, 16, 1
a2, b2, c2 = 16, 20, 2

# Output
# print(operations(a,b,c))
print(operations(a1,b1,c1))
print(operations(a2,b2,c2))
