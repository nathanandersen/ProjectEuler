# Problem 57
# NUMERATOR(n) = 2*NUMERATOR(n-1) + NUMERATOR(n-2)
# DENOMINATOR(n) = 2*DENOMINATOR(n-1) + DENOMINATOR(n-2)
def next_num(p,c):
    return (c,p+2*c)

prev_num = 1
num = 1
prev_denom = 0
denom = 1
total = 0
for n in range(1000):
    (prev_num,num) = next_num(prev_num,num)
    (prev_denom,denom) = next_num(prev_denom,denom)
    if (len(str(num)) >
        len(str(denom))):
        total += 1
print(total)
