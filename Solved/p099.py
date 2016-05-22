# Problem 99

#real	0m0.050s
#user	0m0.029s
#sys	0m0.011s

import math
# I have the sense that this requires intelligent handling
# from discrete math.

# a^b , c^d
# log(a^b) , log(c^d)
# b log(a) , d log(c)

max_val = 0
max_index = 0
counter = 1
with open("p099_base_exp.txt") as f:
    for line in f:
        (a,b) = line.split(",")
        v = int(b) * math.log(int(a))
        if v > max_val:
            max_val = v
            max_index = counter
        counter += 1
print(max_index)
