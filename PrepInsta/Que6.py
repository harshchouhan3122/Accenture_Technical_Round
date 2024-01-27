'''
Question:6 
(Asked in Accenture OnCampus 11 Aug 2021, Slot 3) 
You are required to implement the following Function
Get It or Regret It Sale is Live!! To get 80% discount use coupon code PRIME .
 9 ia d o discount u up Checkout Prime 
The function accepts an integers arr of size ‘length’ as its arguments 
you are required to return the 
sum of second largest element from the even positions and second 
smallest from the odd position 
of given ‘arr’ 
Assumption: 
* All array elements are unique 
+ Treat the Oth position as even 
NOTE 
¢ Return 0 if array is empty 
¢ Return 0, if array length is 3 or less than 3 
Example 
Input 
arr321754 
Output 
7 
Explanation 
* Second largest among even position elements(1 3 5) is 3 
* Second smallest among odd position element is 4 
¢ Thus output is 3+4 =7 
Sample Input 
arr1802356 
Sample Output
8
'''

def sumLargestSmallest(arr):
    if len(arr) <= 3:
        return 0

    even_elements = []
    odd_elements = []

    for i in range(len(arr)):
        if i%2==0:
            even_elements.append(arr[i])
        else:
            odd_elements.append(arr[i])
    
    even_elements = list(set(even_elements))
    odd_elements = list(set(odd_elements))
    even_elements.sort()
    odd_elements.sort()

    # print(even_elements, odd_elements)

    result  = even_elements[-2] + odd_elements[1]
    return result



# Inputs
arr1 = [3,2,1,7,5,4 ]
# Output  7 

arr2 = [1,8,0,2,3,5,6] 
# Output 8

# Outputs
print(sumLargestSmallest(arr1))
print(sumLargestSmallest(arr2))