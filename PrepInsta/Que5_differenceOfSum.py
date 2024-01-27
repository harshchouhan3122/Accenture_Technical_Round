'''
Question 5 :
(Asked in Accenture OnCampus 11 Aug 2021, Slot 2)

Implement the following Function 

def differenceofSum(n. m)

The function accepts two integers n, m as arguments Find the sum of all numbers in 
range from 1 to m(both inclusive) that are not divisible by n. Return difference 
between sum of integers not divisible by n with sum of numbers divisible by n.

Assumption:

n>0 and m>0
Sum lies between integral range
Example

Input
n:4
m:20
Output
90

Explanation

Sum of numbers divisible by 4 are 4 + 8 + 12 + 16 + 20 = 60
Sum of numbers not divisible by 4 are 1 +2 + 3 + 5 + 6 + 7 + 9 + 10 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150
Difference 150 – 60 = 90
Sample Input
n:3
m:10
Sample Output
19
'''

def differenceOfSum(n,m):
    sum1, sum2 = 0,0
    for i in range(1,m+1):
        if i%n==0:
            sum1 += i
        else:
            sum2 += i
    return abs(sum1-sum2)


# Input
n,m = 4,20
# Output
# 90
print(differenceOfSum(n,m))