





def f(nums, n):
    sum_items = sum(nums)
    nums_digits = []
    for i in nums:
        for j in str(i):
            nums_digits.append(int(j))
    sum_digits = sum(nums_digits)
    
    return sum_digits % n - sum_items % n



nums1, n1 = [11,14,16,10,9,8,24,5,4,3], 10
nums2, n2 = [16,18,20], 3

print(f(nums1, n1))
print(f(nums2, n2))