# Problem 66
# Diophantine equations



# Take the euclidean algorithm
# From the Knuth text.

def euclid_gcd(a,b):
    while True:
        r = a % b
        if r == 0:
            return b
        else:
            m1 = a // b
            t1 = a
            t2 = b
            t3 = r
            a = t2
            b = t3
            print(t1,"=",a,"*",m1,"+",b)

# Once we have the GCD, we have to build back up.


print(euclid_gcd(17,5))
