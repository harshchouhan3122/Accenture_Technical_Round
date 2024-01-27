'''
Question : 17 
Instructions: You are required to write the code. You can click on compile and run anytime to check 
compilation/execution status. The code should be logically/syntactically correct. 
Question: Write a program in C such that it takes a lower limit and upper limit as inputs and print all 
the intermediate palindrome numbers. 
Test Cases: 
TestCase 1: 
Input : 
10,80 
Expected Result: 
11,22,33,44,55,66,77. 
Test Case 2: 
Input: 
100,200 
Expected Result: 
101,111,121,131,141,151,161,171,181,191. 

'''

def checkPalindrome(num):
    orgNum = num
    revNum = 0
    while(num!=0):
        revNum =revNum*10 + num%10
        num = num//10
    if orgNum == revNum:
        return True
    return False


def printPalindrome(a,b):
    result = []
    for i in range(a,b+1):
        if checkPalindrome(i):
            result.append(i)
    return result



# a,b = 10, 80
a,b = 100, 200

print(printPalindrome(a,b))