# Problem 100

#real	0m0.065s
#user	0m0.042s
#sys	0m0.012s


# some blue discs
# some red discs
from math import sqrt
from utils import gcd

#equation: ( b / (b+r) ) * ( (b-1) / (b+r-1)) = 1/2
# quadratic equation to solve...:

#b = ((1+2r) + rt(1+8r^2)) / 2
#r + ((1+2r) + rt(1+8r^2)) / 2 > 10**12
#2r + (1+2r) + rt(1+8r^2) > (10**12) * 2
#1 + 4r + rt(1+8*(r**2)) > (10**12) * 2

# whoa. there's a pattern..

# 1 3 1 (0)
#2 5 3 (1)
#7 17 5 (2)
#12 29 17 (3)
#41 99 29 (4)
#70 169 99 (5)
#239 577 169 (6)
#408 985 577 (7)

l = 2 # reds
r = 5 # blues
g = 3

iteration = 1

#for x in range(10):
while True:
    iteration += 1
    if iteration % 2:
        l_new = l + g
    else:
        l_new = l + r
    g_new = r

    l_term = l_new * g_new
    r_term = (2*l_term + 1 + sqrt(1 + 8*(l_term ** 2)))/2 # from the formula above
    r_new = int(r_term/g_new)

    (l,r,g) = (l_new,r_new,g_new)
#    print(l,r,g)
    if (l+r)*g > 10**12:
        print(r*g)
        exit()

exit()
