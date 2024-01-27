'''
Question 15 
Problem Statement 
You are required to input the size of the matrix then the elements of 
matrix, then you have to divide 
the main matrix in two sub matrices (even and odd) in such a way that 
element at 0 index will be 
considered as even and element at 1st index will be considered as odd 
and so on. then you have sort 
the even and odd matrices in ascending order then print the sum of 
second largest number from 
both the matrices 
Example 
¢ enter the size of array : 5 
* enter element at 0 index : 
+ enter element at 1 index : 
+ enter element at 2 index : 
+ enter element at 3 index: 
« enter element at 4 index : OO N= hh Ww 
Sorted even array: 139 
Sorted odd array : 4 7 
7

'''

def SortedSum(arr):
    even = []
    odd = []
    for i in range(len(arr)):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    even = list(set(even))
    odd = list(set(odd))
    return even[-2] + odd[-2]


size = 5
# arr = list(map(int,input().split(" ")))
arr = [3,4,1,7,9]

print(SortedSum(arr))