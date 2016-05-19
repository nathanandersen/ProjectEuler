# Problem 345

matrix = []
line_len = 0
for line in open("p345_matrix.txt"):
    line = line.strip()
    line = line.replace("   ",",")
    line = line.replace("  ",",")
    line = line.replace(" ",",")
    row = eval("[" + line + "]")
    line_len = len(row)
    matrix.append(row)

# We will define a dynamic programming, 2D table, M
# M(i,j) will contain the max matrix sum if we include
# element (i,j) in the matrix.

# matrix [y] [x] is how it is used

# to construct element M(i,j)

# we have to iterate over everything in the previous...


# this looks like a multi-dimensional DP. I don't know how to do this problem yet.
