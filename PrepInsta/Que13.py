


def maxExponential(a,b,c):
    start = int(a**(1/2))
    end = int(b**(1/2))
    ans = 0
    # print(start, end)
    for i in range(start, end+1):
        # print(i)
        temp = c**i
        if temp > b:
            break
        ans = temp
    return ans

a,b = 7,1200
c = 2

print(maxExponential(a,b,c))
