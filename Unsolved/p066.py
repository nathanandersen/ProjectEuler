# Problem 66
# Diophantine equations
import sys

# euclidean algorithm for gcd
# A = b*(A//b) + A%b
# b = (A%b)*(b//A%b).....

# Number theory, Euclidean algorithm.
# Taken from Discrete textbook (p. 29)
def solve_Dioph(a,b,c):
    # ax + by = c
    # return (x,y)
    m1=1
    m2=0
    n1=0
    n2=1
    r1=a
    r2=b
    while r1%r2!=0:
        q=r1//r2
        aux=r1%r2
        r1=r2
        r2=aux
        aux3=n1-(n2*q)
        aux2=m1-(m2*q)
        m1=m2
        n1=n2
        m2=aux2
        n2=aux3

    if m2*c*a + n2*c*b == c:
        return m2*c,n2*c
    else:
        return None,None
#    print(m2*c*a + n2*c*b,c)
#    return m2*c,n2*c;

#def find_min_solution(d):
#    for
#a,b,c = 12,17,4
#a,b,c = 6,7,1
a,b,c = 2,-4,1
x,y = solve_Dioph(a,b,c)
print(x,y)


min_value = sys.maxsize
min_index = 0

#for d in range(2,1001):
#    x = solve_Dioph(1,1,1)
