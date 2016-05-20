# Problem 78
# Partitions. Number Theory.

#real	0m18.383s
#user	0m18.160s
#sys	0m0.098s

p = [1,1,2]

def calc_term(k):
    return k*(3*k-1)/2

while (p[len(p)-1] % 1000000 != 0):
    # recurrence relation from Pentagonal Number Theorem
    # calculate the next value
    v = 0
    k = 1
    n = len(p)
    t = calc_term(k)
    while n >= t:
        v = v + ((-1)**(k-1))*p[int(n-t)]
        k = k+1
        t = calc_term(k)
    k = -1
    t = calc_term(k)
    while n >= t:
        v = v + ((-1)**(k-1))*p[int(n-t)]
        k = k-1
        t = calc_term(k)

    p.append(v % 1000000)

final = len(p)-1
print(final,p[final])    
