'''
Question 2 : Balance Fruits


Implement the following function: int BalanceFruits(int a, int m, int rs);

You have a basket full of apples and mangoes, your job is to make the numer of apples and given a 
function that accepts three integers 'a', 'm' and 'rs' as its argument where 'a' and a basket 
respectively and 'rs' is the rupees that you have. Implement the function to balance the basket. 
If 'a' > 'm', then buy (a - m) mangoes at the rate of Rs 1 per mango. If 'a' < 'm', then sell (m - a) 
mangoes at the rate of Rs 1 per mango. Return the total rupees left with you after balancing the fruits.

Assumption:

a > = 0, m > = 0 and rs > = 0
rs > = (a - m)

Note: If a = m, return rs unchanged

Test Case :

Input :

a : 8
m : 4
rs : 6

Output :
2


Explanation:

Since a > m, (a - m) mangoes are bought at Rs 1 per mango, so rs = 6 - 4 = 2. Thus, output is 2.
'''

def BalanceFruits( a, m, rs):
    if a > m:
        rs -= m
    else:
        rs += a
    return rs


a, m ,rs = 8, 4, 6
print(BalanceFruits(a,m,rs))