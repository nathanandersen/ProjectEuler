# Problem 78

# This smells like dynamic programming.

# For every possible group, from 2 -> 3

# we can either add a coin to extend the back group ( o )
# or we can add it as its own group ( |o)

# how can we detemine whether the o is unique? the |o is always unique.

# but if we extend, I think, then it's possibly double-counted.
# some scratch work..

# 2:
# oo
# o|o

# 3:
# ooo
# oo|o
# o|o|o

# 4:
# oooo
# ooo|o
# oo|oo
# oo|o|o
# o|o|o|o

# 5:
# oooo | o
# ooooo
# ooo |oo
# ooo|o|o
# oo|oo|o
# oo|ooo XXX
# oo|o|o|o
# oo|o|oo XXX
# o|o|o|oo XXX
# o|o|o|o|o

