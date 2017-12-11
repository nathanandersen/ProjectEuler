# Problem 64
from math import sqrt
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html

# I think this is going to involve symbolic manipulation.
# I'm not entirely sure how I want to process that.

class ContinuedSqrt:
    def __init__(self,n):
        self.n = n
        self.irrational_num = 0
        self.rational_num = 0
        self.denom = 0
        self.nums = []
        self.expand()

    def expand(self):
        pass

    def get_period(self):
        pass




def findContinuedFraction(rt):
    m = int(sqrt(rt)) # Largest square less than m
    # rt(n) = m + 1/x, we are looking for 1/x
    # x = 1 / ( rt(n) - m)
