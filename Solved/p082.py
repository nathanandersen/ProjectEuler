# Problem 82

# real 0m0.122s
# user 0m0.101s
# sys  0m0.012s

# Abstract idea:
# Given the minimum cost path on the board to the right side,
# fill in all its neighbors, because they will necessarily take
# that path.

# We will implement this minimum cost tracking with a priority
# queue, that maps costs to (x,y) points.

import queue

matrix = []
with open("p082_matrix.txt","r") as f:
    for text in f:
        text = eval("[" + text + "]")
        matrix.append(text)

# TAKE CARE THAT THE MATRIX IS USED
# MATRIX [ Y ] [ X ]

# we don't actually need a min_costs array, it's just simple
# for book-keeping and back-tracking.
# it's useful to mark what cells we have already seen.
min_costs = [[None for x in range(len(matrix))] for y in range(len(matrix))]
# use a PQ to track minimum values
min_vals = queue.PriorityQueue()
# store: (cost, (x,y) )
x = len(matrix)-1
for y in range(len(matrix)):
    v = matrix[y][x]
    min_costs[y][x] = v
    min_vals.put((v,(x,y)))

def update_table_value(x,y,cost):
    if -1 < x < len(matrix) and -1 < y < len(matrix):
        if min_costs[y][x] is None:
            # calculate the total cost
            total_cost = matrix[y][x] + cost
            # update its min_cost table entry
            min_costs[y][x] = total_cost
            # put it in the priority queue
            min_vals.put((total_cost,(x,y)))

while True:
    # get the min value
    (cost,(x,y)) = min_vals.get()
    # update all 3 of its neighbors
    update_table_value(x-1,y,cost)
    update_table_value(x,y-1,cost)
    update_table_value(x,y+1,cost)
    # if we are in col 1, then we know that we
    # updated a value in col 0 (target column)
    if x == 1:
        break

print((x-1,y),min_costs[y][0])
