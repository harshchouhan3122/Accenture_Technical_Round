'''
Question: 16 
Instructions: You are required to write the code. You can click on compile and run anytime to check 
compilation/execution status. The code should be logically/syntactically correct. 
Problem: Write a program in C to display the table of a number and print the sum of all the multiples 
init. 
Test Cases: 
Test Case 1: 
Input: 
5 
Expected Result Value: 
5,10, 15, 20, 25, 30, 35, 40, 45, 50 
275 
Test Case 2: 
Input: 
12 
Expected Result Value: 
12,24, 36, 48, 60, 72, 84, 96, 108, 120 
660 
'''


def tableSum(num):
    sum = 0
    for i in range(1,11):
        print(num*i, end=" ")
        sum += num*i
    print()
    return sum

# Input
num1 = 5
num2 = 12

print(tableSum(num1))
print(tableSum(num2))