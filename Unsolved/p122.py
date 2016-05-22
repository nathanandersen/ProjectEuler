# Problem 122

# Also looks like DP!

# We will define a 1-D table, m, which will contain the number of
# multiplications for a given power needed

# ie, m[2] = the number of multiplications needed to calculate
# n^2.

# to build arbitrary m[i], we must look at all previous values

# hmmm but in the example case

# 1 , 1 = 2
# 2 , 1 = 3
# 3 , 3 = 9
# 6 , 6 = 12
# 12 , 3 = 15
# we have to hold on to 3.
# so somehow we have to keep track of the values we look at, along
# the way.]

# we will define supplementary 1D table, a, which will contain a set
# at each entry, of the previous values visited along the way, ie, that
# we can use again for no additional cost.

# to build a[i], where the final values are k,j
# we will insert into this set:
# a[k] + a[j] + j + k.
