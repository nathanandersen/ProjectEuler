# Problem 78

def partitions(n):
    # There are 2 ** n-1 possible arrangements of the partitions
    # between coins. The question is, how do we determine how
    # many of them are unique?


# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1

# 2 coins: 2 groups ==> 2
# 1 group no partitions
# 1 group partitions

# oo
# o|o
# 2^(2-1) - 0 = 2

# 3 coins: 3 groups ==> 4 - 1
# 1 group no partitions
# 1 group 1 partition -> 1 repeat
# What is the relationship between 3 coins and 1 partition?
# 1 group all partitions

# ooo
# oo|o (o|oo)
# o|o|o
# 2 ^ (3-1) - 1 = 3

# 4 coins: 5 groups ==> 8 - 3
# 1 none, 1 all
# 2 groups 1 partition -> 1 repeat
# What is the relationship between 4 coins and 1 partition
# 1 group 2 partitions -> 2 repeats
# Relationship between 4 coins and 2 partitions

# oooo
# ooo|o (o|ooo) <- repeated once
# oo|oo
# oo|o|o (o|oo|o o|o|oo) <- repeated twice
# o|o|o|o


# 5 coins: 7 groups ==> 16 - 9
# 1 none, 1 all
# 2 groups 1 -> 2 repeats
# 2 groups 2 -> 4 repeats
# 1 group 3 -> 3 repeats


# 6 coins: 12 groups ==> 32 - 20


# oooooo
# ** 1 partition
# ooooo|o (o|ooooo)
# oooo|oo (oo|oooo)
# ooo|ooo
# ** 2 partitions
# oooo|o|o (o|oooo|o o|o|oooo)
# ooo|oo|o (ooo|o|oo o|oo|ooo o|ooo|oo oo|ooo|o oo|o|ooo)
# oo|oo|oo
# ** 3 partitions
# ooo|o|o|o (o|ooo|o|o o|o|ooo|o o|o|o|ooo)
# oo|oo|o|o (oo|o|oo|o oo|o|o|oo o|oo|o|oo o|o|oo|oo)
# ** 4 partitions
# oo|o|o|o|o (o|oo|o|o|o o|o|oo|o|o o|o|o|oo|o o|o|o|o|oo)
# ** 5 partitions
# o|o|o|o|o|o


# n-1 partitions: 1
# n-2 partitions: 1
# 1 partition: n/2
# 0 partitions: 1
