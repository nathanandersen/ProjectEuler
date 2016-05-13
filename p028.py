# Problem 28

# Each time we move to the next level of spiral, we add 2 to the
# spin of the previous one and then do that four times.

# For example, in 5x5,
# [1x1]: 1
# [3x3]: (1 + 1*2) + (1 + 2*2) + (1 + 3*2) + (1 + 4*2)
# [5x5]: (1+4*2 + 1*4) + (.. + 2*4)



iter_start = 1
width = 1001
#width = 5
total = 1
for x in range(2,width,2):
    for i in range(1,5):
        total += iter_start + i*x
    iter_start = iter_start+x*i

print(total)
