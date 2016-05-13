# Problem 67
# Digit factorial chains
from math import factorial

def digit_fact_sum(n):
    return sum(factorial(int(d)) for d in str(n))

def digit_fact_chain_len(n):
    chain_eles = {n}
    chain_ele_len = len(chain_eles)
    while(1):
        n = digit_fact_sum(n)
        chain_eles.add(n)
        if chain_ele_len == len(chain_eles):
            return len(chain_eles)
        else: chain_ele_len = len(chain_eles)


#print(digit_fact_sum(145))
#print(digit_fact_chain_len(169))
count = 0
for i in range(1000000):
    print(i)
    if digit_fact_chain_len(i) == 60:
        count += 1
print(count)
