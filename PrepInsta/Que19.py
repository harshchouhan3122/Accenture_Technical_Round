'''
Question: 19 
Find the maximum value and its index in the array 
Problem Statement : 
You are given a function, void MaxInArray(int arr], int length); The function accepts an integer array 
‘arr’ of size ‘length’ as its argument. Implement the function to find the maximum element of the 
array and print the maximum element and its index to the standard output 
(STDOUT). The maximum element and its index should be printed in separate lines.
Get It or Regret It Sale is Live!! To get 80% discount use coupon code PRIME Checkout Prime 
¢ Array index starts with 0 
« Maximum element and its index should be separated by a line in the output 
¢ Assume there is only 1 maximum element in the array 
¢ Print exactly what is asked, do not print any additional greeting messages 
Example: 
Input: 
234582276612781371 86 
Qutput: 
86 
Explanation: 
86 is the maximum element of the array at index 9. 

'''

def maxPosition(arr):
    maxIndex = 0
    maxNum = arr[maxIndex]
    for i in range(1, len(arr)):
        if arr[i] > maxNum:
            maxIndex = i
    return maxIndex


arr = [23,45,82,27,66,12,78,13,71,86]

print(maxPosition(arr))