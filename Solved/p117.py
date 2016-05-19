# Problem 117

#real	0m0.101s
#user	0m0.031s
#sys	0m0.024s

# Dynamic programming, again

# We will define a table, N
# where N(x) is the number
# of ways to tile a length.

n = [0]
tile_lens = [1,2,3,4]

def tile_patterns(x):
    total = 0
    for tile in tile_lens:
        if x - tile < 0: continue
        if x is tile: total += 1
        else: total += n[x-tile]
    return total


for x in range(1,51):
    n.append(tile_patterns(x))

print(n[50])
