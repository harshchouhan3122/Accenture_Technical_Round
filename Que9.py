'''
9. Perform the function Int calculate(int m, int n). This function n 
two positive integers. Calculate the sum of numbers between th 
two numbers that are divisible by 3 and 5. 
Assumption
m>n>=0 

Example 

Input: 
m:12 
n: 50 

Output: 
90 

Explanation 
The numbers between 12 and 50 that are divisible by 3 and 5 are 15, 30, and 45. The sum 
of these numbers is 90. 

Sample input: 
m: 100 
n: 160 

Sample output: 
510 
'''

def sum3and5(m,n):
    sum = 0
    for i in range(m,n+1):
        if i%3==0 and i%5==0:
            # print(i,end=" ")
            sum+=i
    # print()
    return sum

# Input
# m, n = input().split(" ")
# m, n = int(m), int(n)
m1, n1 = 12, 50
m2, n2 = 100, 160

# Output
print(sum3and5(m1,n1))
print(sum3and5(m2,n2))