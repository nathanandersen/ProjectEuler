# Problem 77
primes = sieve(1000)

# we will define a table, N
# where N(x) is the number
# of ways x can be written as
# the sum of prev. primes

# to calculate arbitrary N(i),
# we must take a prime p, and then
# look up the value N(i-p)

# this is cool, and all, but how do
# we guarantee uniqueness?

# 2+5 looks a lot like 5+2...

# 27+2 could look a lot like 24+5

# we will define a helper table, where
# V(x) is the set of tuples of coin collections

# so we will iterate over everything in everything up
# to x, make a new set of tuples,

