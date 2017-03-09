# Problem 114
# Yet another DP

#real	0m0.046s
#user	0m0.026s
#sys	0m0.010s

# We will define a 1-D DP table, N
# where N(x) is the number of ways we can
# distinctly place tiles on it.

# To calculate arbitrary entry N(i), we have to consider
# red blocks of length 3....i at the end, as well as a regular
# single black block at the end.
# Looks like O(n^2).

n = {0:1}
def tile_count(x):
    return n[x-1] + sum(1 if i == x else n[x-i-1] for i in range(3,x+1))

for x in range(1,51):
    n[x] = tile_count(x)

print(n[50])
