# Problem 206

# real 0m27.558s
# user 0m27.160s
# sys  0m0.176s

import math
import sys

# a bottom-up brute-force algorithm
def solve_bottom_up():
    bottom = int(math.sqrt(1020304050607080900))
    top = math.ceil(math.sqrt(1929394959697989900))
    sqr = bottom ** 2
    for i in range(bottom+10,top,10):
        # clever math for (i-10)**2 -> i**2
        sqr += 5 * (i << 2) - 100
        if str(sqr)[::2] == "1234567890":
            print(i,sqr)
            sys.exit()

solve_bottom_up()

#(i-10)**2 -> i **2
#i **2 - 20i + 100 -> i ** 2
