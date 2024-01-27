'''
2. Execute the given function.
def LargeSmallSum(arr)

The function takes an integral arr which is of the size or length of its arguments. Return the sum of the second smallest element at odd position ‘arr’ and the second largest element at the even position.

Assumption

Every array element is unique.
Array is 0 indexed.
Note:

If the array is empty, return 0.
If array length is 3 or <3, return 0.
 
Example

Input:
Arr: 3 2 1 7 5 4

Output:
7
 

Explanation

The second largest element at the even position is 3.
The second smallest element at the odd position is 4.
The output is 7 (3 + 4).

'''

arr = list(map(int,input().split(" ")))
list_odd = []
list_even = []

for i in range(len(arr)):
    if i%2==0:
        list_even.append(arr[i])
    else:
        list_odd.append(arr[i])

# print(list_odd)
# print(list_even)

list_even.sort()
list_odd.sort()

list_even = list(set(list_even))
list_odd = list(set(list_odd))

print(list_odd[-2]+list_even[-2])

