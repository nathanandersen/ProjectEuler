# Problem 97
#m = (28433 * (2 ** 7830457)) + 1

#real	0m0.052s
#user	0m0.035s
#sys	0m0.010s

# Let's use some discrete math.
# 28433 * (2 ** 7830457) + 1, mod 10 ** 10
# Want to: split up 2 ** 7830457
# into smaller modulo powers (and recurse).
a = 28433 # leading coef
b = 2 # base
p = 7830457
t = 10 ** 10

def find_min_modulo(base,mod):
    # Given a mod b,
    # we want to find (x,y), such that a ** x == y mod b
    # such that y is a minimum
    p = 0 #power
    cur = 1
    while cur < mod:
        cur *= base
        p += 1

    cur %= mod
    min_index = p
    min_val = cur
    for n in range(10000):
        cur = (cur * base) % mod
        p += 1
        if (cur < min_val):
            (min_val,min_index) = (cur,p)
    return(min_val,min_index)


while p > 1:
    (new_base,new_pow) = find_min_modulo(b,t)
    # given b ** p, we then split
    # b**p => (new_base ** new_pow) * (b ** (p % new_pow))
    # and recurse on (new_base ** new_pow)
    rem = p % new_pow
    a = (a*(b ** rem)) % t
    b = new_base
    p //= new_pow

print(a+1)
