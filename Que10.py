'''
10. Execute the function for the given purpose. 
Create a matrix and mention the elements in it. Now, divide the main matrix into two halves 
in such a way that the elements in index O are even, the elements in index 1 are odd, and so 
on. 
Then arrange the values in ascending order for even and odd. After this, calculate the sum 
of the second largest numbers from both even and odd matrices. 
Example 
The size of the array is 5. 
Element at 0 index: 3 
Element at 1 index: 4 
Element at 2 index: 1 
Element at 3 index: 7 
Element at 4 index: 9 
Even array: 1,3,9 
Odd array: 4,7 

'''
    
def oddEvenArray(arr):
    Odd = []
    Even = []
    for i in range(len(arr)):
        if i%2==0:
            Even.append(str(arr[i]))
        else:
            Odd.append(str(arr[i]))

    Even = ','.join(Even)
    Odd = ','.join(Odd)
    
    return (f"Even array : {Even} \nOdd array : {Odd}")


# Input 
# arr = list(map(int,input().split(" ")))
arr = [3,4,1,7,9]

# Output
print(oddEvenArray(arr))