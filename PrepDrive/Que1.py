'''
Question 1 : Count Specific Numbers


You are required to implement the following function: int CountSpecificNumbers(int m, int n)

The function accepts two arguments m and n which are integers. You are required to calculate the count of numbers having only 1, 4 and 9 as their digits between the numbers lying in the range m and n both inclusive, and return the same. Return -1 if m>n.


Test Case :

Input :

100
200

Output :
9


Explanation:

The numbers between 100 and 200, both inclusive having only 1,4 and 9 as their digits are 
111, 114, 119, 141, 144, 149, 191, 194, 199.
The count is 9 hence 9 is returned.
'''

def CountSpecificNumber(a,b, num):
    result = []
    for i in range(a, b):
        count = 0
        for j in str(i):
            if int(j) not in num:
                break
            count += 1
        if count == 3:
            result.append(i)
    return len(result)

a, b = 100, 200
num = [1,4,9]

print(CountSpecificNumber(a,b,num))
