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

n = [1]
def tile_count(x):
    total = n[x-1]
    for i in range(3,x+1):
        if i is x: total += 1
        else: total += n[x-i-1]
    return total

for x in range(1,51):
    n.append(tile_count(x))

print(n[50])
