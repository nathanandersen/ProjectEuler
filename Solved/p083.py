# Problem 83

# real 0m0.135s
# user 0m0.113s
# sys  0m0.012s

import queue

matrix = []
with open("p083_matrix.txt","r") as f:
    for text in f:
        text = eval("[" + text + "]")
        matrix.append(text)

min_costs = [[None for x in range(len(matrix))] for y in range(len(matrix))]
min_vals = queue.PriorityQueue()

v = matrix[len(matrix)-1][len(matrix)-1]
min_costs[len(matrix)-1][len(matrix)-1] = v
min_vals.put((v,(len(matrix)-1,len(matrix)-1)))

def update_table_value(x,y,cost):
    if -1 < x < len(matrix) and -1 < y < len(matrix):
        if min_costs[y][x] is None:
            total_cost = matrix[y][x] + cost
            min_costs[y][x] = total_cost
            min_vals.put((total_cost,(x,y)))

while min_costs[0][0] == None:
    (cost,(x,y)) = min_vals.get()
    update_table_value(x-1,y,cost)
    update_table_value(x+1,y,cost)
    update_table_value(x,y-1,cost)
    update_table_value(x,y+1,cost)

print(min_costs[0][0])
