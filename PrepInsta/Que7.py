'''
Question:7 
(Asked in Accenture OnCampus 12 Aug 2021, Slot 1) 
Implement the following Function
Get et It It or or R Regre t It Sale ale is is Live!l Liv To get 80% 6 discount discount u use coupon u code PRIME Checkout Prime . 
The function accepts an integers sum and an integer array arr of size n. Implement the function to 
find the pair, (arrfj], arr[k]) where jl=k, Such that arr[j] and arr[k] are the least two elements of array 
(arr[j] + arr[k] <= sum) and return the product of element of this pair 

* Return -1 if array is empty or if n<2 
* Return 0, if no such pairs found 
¢ All computed values lie within integer range 
Example 
Input 
sum:9 
size of Arr=7 
Armr:5243971 
Output 
2 
Explanation 
Pair of least two element is (2,1) 2+ 1 = 3 < 9, Product of (2, 1) 2*1 = 2. Thus, output is 2 
Sample Input 
sum:4 
size of Arr=6 
Armr983-739 
Sample Output 
-21 
'''

def productSum(arr,sum,size):
    n = size
    if n < 2:
        return -1
    arr = sorted(arr)
    for i in range(n-1):
        if arr[i] + arr[i+1] < sum1:
            return (arr[i] * arr[i+1])
    else:
        return 0


# Inputs
sum1, size1, arr1 = 9, 7, [5,2, 4, 3, 9, 7, 1]
# Output : 2
sum2, size2, arr2 = 4, 6, [9,8,3,-7,3,9]
# Output : -21

# Output
print(productSum(arr1,sum1,size1))
print(productSum(arr2,sum2,size2))