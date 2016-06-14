# Problem 66
# Diophantine equations



# Take the euclidean algorithm
# From the Knuth text.

def euclid_gcd(a,b):
    a = a.copy()
    b = b.copy()
    while True:
        r = a % b
        if r == 0:
            return b
        else:
            t1 = a
            t2 = b
            t3 = r
            a = t2
            b = t3

# Once we have the GCD, we have to build back up.



exit()
