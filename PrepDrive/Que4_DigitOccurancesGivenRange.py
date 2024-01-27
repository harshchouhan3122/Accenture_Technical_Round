'''
Question 4 : Count Digit Occurrences


You are required to implement the following function:

int CountDigitOccurrences(int l, int u, int x);

The function accepts 3 positive integers 'l', 'u' and 'x' as its argument. you are required to calculate the number of occurrences of a digit 'x' in the digit of number lying in the range between 'l' and 'u' both inclusive, and return the same.

Note:

l < = u
0 < = x < = 9

Test Case 1

Input :
l : 2
u : 13
x : 3

Output :
2

Explanation

The number of occurrences of digit 3 in the digits of the number lying in the range [2,13] both inclusive is 2, i.e{3,13}, hence 2 is returned.

Test Case 2

Input :
l: 1
u: 30
x: 2

Output :
13
'''

def CountDigitOccurrences(l, u, x):
    result = []
    for i in range(l, u+1):
        if str(x) in str(i):
            result.append(i)
    # return result
    return len(result)

l, u, x = 1, 30, 2
l, u, x = 2, 13, 3
print(CountDigitOccurrences(l, u, x))