# Problem 116

#real	0m0.045s
#user	0m0.027s
#ys	0m0.010s

r = []
g = []
b = []

def calc_tiles(arr,length,x):
    total = 0
    for tile in [1,length]:
        if x - tile < 0: continue
        if x is tile: total += 1
        else: total += arr[x-tile]
    return total

for x in range(51):
    r.append(calc_tiles(r,2,x))
    g.append(calc_tiles(g,3,x))
    b.append(calc_tiles(b,4,x))

print(r[50] + g[50] + b[50] - 3)
# there is 1 all-black per type
