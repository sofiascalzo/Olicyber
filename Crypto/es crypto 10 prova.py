from math import gcd

def chinese_remainder_theorem(equations):
    n = len(equations)
    prod = 1
    for i in range(n):
        prod *= equations[i][1]
    
    sol = 0
    for i in range(n):
        pi = prod // equations[i][1]
        sol += equations[i][0] * pi * (pi**(-1))
    
    return sol % prod

equations = [(73, 25), (51, 66), (68, 91), (16, 29), (43, 53)]

x = chinese_remainder_theorem(equations)
flag = x % 673879206
print(flag)

