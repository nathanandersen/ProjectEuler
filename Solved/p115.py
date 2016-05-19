# Problem 115

#real	0m0.046s
#user	0m0.028s
#sys	0m0.009s

n = [1]
m = 50
def tile_count(x):
    total = n[x-1]
    for i in range(m,x+1):
        if i is x: total += 1
        else: total += n[x-i-1]
    return total

x = 1
while True:
    tc = tile_count(x)
    if tc > 1000000:
        print(x,tc)
        exit()
    else:
        n.append(tc)
        x += 1
