# Problem 64
from math import sqrt
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html

# I think this is going to involve symbolic manipulation.
# I'm not entirely sure how I want to process that.

def findContinuedFraction(rt):
    m = int(sqrt(rt)) # Largest square less than m
    # rt(n) = m + 1/x, we are looking for 1/x
    # x = 1 / ( rt(n) - m)
