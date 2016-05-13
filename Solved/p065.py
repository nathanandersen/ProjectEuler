# Problem 65

# real 0m0.061s
# user 0m0.041s
# sys  0m0.012s

from fractions import Fraction
from utils import digit_sum

# a helper for the lookup values of e
# n > 1
def get_convergent_value(n):
    if n % 3:
        return 1
    else:
        return (n//3) * 2

def make_convergent_frac(n,rest_num,rest_denom):
    if n == 1:
        return (rest_num,rest_denom)
    else:
        v = get_convergent_value(n)
        if rest_num and rest_denom:
            # then factor in v
            frac = Fraction(v*rest_denom + rest_num,rest_denom)
            return make_convergent_frac(n-1,frac.denominator,frac.numerator)
        else:
            return make_convergent_frac(n-1,1,v)

def get_convergent_num(n):
    (num,den) = make_convergent_frac(n,0,0)
    frac = Fraction(2*den + num, den)
    return(frac.numerator,frac.denominator,get_convergent_value(n))

for n in [100]:
    (num,den,v) = get_convergent_num(n)
    print(digit_sum(num))
