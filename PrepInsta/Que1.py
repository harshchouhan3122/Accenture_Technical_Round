'''
Problem Description :
The function accepts two positive integers ‘r’ and ‘unit’ and a 
positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the 
number of rats present in an area, ‘unit’ is the amount of food each 
rat consumes and each ith element of array ‘arr’ represents 
the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for 
all the rats.Computed values lie within the integer range.
Example:

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2

Output 
4
'''


def isFoodSufficient(r,unit,n,arr):
    if arr == []:
        return -1
    
    consume = r*unit
    count = 0
    food = 0

    for i in arr:
        count += 1
        food += i
        if food >= consume:
            return count

    return 0



r = 7
unit = 2
n = 8
arr = [2, 8, 3, 5, 7, 4, 1, 2]
# arr = [1]*5
# arr = []
print(isFoodSufficient(r,unit,n,arr))

