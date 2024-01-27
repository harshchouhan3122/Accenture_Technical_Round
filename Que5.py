# IMPORTANT


import string 
def decTonBase(d,num):
    num_out = ""
    k = list(range(10,37))
    v = list(string.ascii_uppercase)
    hexValue = dict(zip(k,v))
    # print(dic)

    q = 1
    while(q>0):
        q = num//n
        rem = num%n
        if rem > 36:
            return -1
        if rem>9:
            rem = hexValue[rem]
        num_out = str(rem) + num_out
        num = q

    return num_out

# def DectoNBase(n, num):
#     hex = []
#     val = 'A'
#     for i in range(10,n+1):
#         hex.append(val)
#         val = chr(ord(val)+1)
    
#     result = ""
#     while(num!=0):
#         que =  num//n
#         rem = num%n
#         num = que
#         if rem > 9 :
#             result = str(hex[rem-10]) + result
#         else:
#             result = str(rem) + result

#     return result


n = int(input())
num = int(input())

print(decTonBase(n,num))
