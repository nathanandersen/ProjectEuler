# Problem 78

# This smells like dynamic programming.

# For every possible group, from 2 -> 3

# we can either add a coin to extend the back group ( o )
# or we can add it as its own group ( |o)

# how can we detemine whether the o is unique? the |o is always unique.

# if we extend with a (o), and the relationship between all the groups
# is no longer in order (the last one is not the smallest), then we don't
# count it.
# how to check this?


# Maybe I could implement this with sets of tuples.
# for each tuple in the prev layer
# last number += 1, and append 1.
# then sort the tuple
# and add it to the set.
# (then, dispose of the previous set).

def make_coin_extensions(tup):
    if isinstance(tup,int):
        single = (1,) + (tup,)
        extended = (tup+1,)
    else:
        single = (1,) + tup
        

        
prev = set((1,))
cur = set()
x = 1
while True:
#if True:
    for coins in prev:
        if isinstance(coins,int):
            single = (1,) + (coins,)
            extended = (coins+1,)
        else:
            single = (1,) + coins
            extended = coins[:len(coins)-2]
            if isinstance(extended,int):
                extended = (extended,) + (coins[len(coins-1):]+1,)
            else:
                extended = extended + (coins[len(coins-1):]+1,)
            print(extended)

        cur.add(single)
        cur.add(extended)
    if not len(cur) % 1000000:
        print(x)
        exit()
    else:
        x += 1
        prev = cur
        cur = set()


#OR.. THIS IS NO GOOD


# for each layer....x
# we determine the # of coins in the LAST group, l
# then look up n(x-l), and sum that in.
# n(0) = 1, 1 way to order no coins
#n = [1]

#def coin_partitions(x):
#    total = 0
#    for l in range(1,x+1): # number of coins in last group
#        total += n(x-l) # number of ways to pre-order that
        # no... this is not unique


