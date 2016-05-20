# Problem 78

# Given that the group on the end is of size n,
# every group to its left must be at least of size n.

# N = a 2-D matrix.
N = []
# N[x] = the entries for row length x
# N[x][i] = the number of ways to order a row of length x with last
# group of size i

# Correct, but not quite fast enough.
# Can I use math to optimize.

def calc_coin_table_entry(n,l):
    """ N is the row length, l is the last-group size."""
    total = 0
    for k in range(l,n-l+1):
        total += N[n-l][k]
    return total

def calc_coin_table_row(n):
    """N is the row length"""
    row = [0]
    for l in range(1,n):
        row.append(calc_coin_table_entry(n,l))
    row.append(1)
    return row

x = 0
while True:
    row = calc_coin_table_row(x)
    s = sum(row)
    if not s % 1000000:
        print(x)
        exit()
    N.append(row)
    print(x,s)
    x += 1

