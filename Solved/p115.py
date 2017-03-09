4# Problem 115

#real	0m0.046s
#user	0m0.028s
#sys	0m0.009s

n = {0:1}
m = 50
def tile_count(x):
    return n[x-1] + sum(1 if i == x else n[x-i-1] for i in range(m,x+1))

counter,tc = 0,0
while tc < 1000000:
    counter += 1
    tc = tile_count(counter)
    n[counter] = tc

print(counter,tc)
