from itertools import zip_longest

# def numberOfCarry(num1, num2):
#     carry_count = 0
#     carry = 0
#     num1,num2 = str(num1),str(num2)
#     num1,num2 = list(num1)[::-1],list(num2)[::-1]
#     for i,j in zip_longest(num1,num2,fillvalue=0):
#         sum = int(i) + int(j) + carry
#         if sum>9:
#             carry_count += 1
#             carry = sum//10
#     return carry_count

def numberOfCarry(num1, num2):
    # making both the numbers of equal length
    num1,num2 = list(str(num1)),list(str(num2))
    if len(num1) > len(num2):
        num2 = [0]*(len(num1)-len(num2)) + num2
    else:
        num1 = [0]*(len(num2)-len(num1)) + num1
    # return num1,num2

    # reverse the numbers , Addition is took place from right to left
    num1,num2 = num1[::-1],num2[::-1]
    carry_count = 0
    carry = 0
    digit_sum = 0
    for i in range(len(num1)):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        if digit_sum > 9:
            carry_count += 1
            carry = digit_sum//10
    return carry_count

num1 = int(input())
num2 = int(input())

print(numberOfCarry(num1,num2))
