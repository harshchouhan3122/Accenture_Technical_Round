def productsSmallPair(sum,arr):
    if len(arr) < 2:
        return -1
    
    arr.sort()
    sum1 = arr[0] + arr[1]
    if sum1<sum:
        return arr[0]*arr[1]
    else:
        return sum
    



sum = int(input())
arr = list(map(int,input().split(" ")))

print(productsSmallPair(sum,arr))