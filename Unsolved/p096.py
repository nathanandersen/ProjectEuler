# Problem 96

# Pseudocode algorithm
# 1) Matrix, 9x9, of possibilities (list 0-9)
# 2) Matrix, 9x9, of bool "seen" values (bool T/F, all init False)

# Maintain a Queue of (x,y) coordinates
# Pop the next value:
# Update all values in its REGION, ROW, and COLUMN
# If a value is of length 1 (unique), and not SEEN
# add it to the queue

# while queue has values, iterate

# once queue has no values, we are finished


# BUT HOW DO WE HANDLE THE CONDITIONAL, FUNNY VALUES?
# like when a section needs an 9, it's only available in two places
# then we have to block off the rest of the row...


import queue
digits = [0,1,2,3,4,5,6,7,8,9]
sudoku_len = 9

def try_to_remove_sudoku_value(x,y,v,m,s,q):
    if s[y][x]: return
    try:
        m[y][x].remove(v)
    except ValueError:
        pass

    if len(m[y][x]) == 1:
        add_to_queue(x,y,s,q)
        return

    return
    # or if is the only one in its block or row or col

def add_to_queue(x,y,s,q):
    s[y][x] = True
    q.put((x,y))

def sudoku_process(x,y,m,s,q):
    # Update all values in the region to not have any of the same
    # digit that is in this value

    # for (x,y) in row:
    for x_row in range(sudoku_len):
        try_to_remove_sudoku_value(x_row,y,m[y][x][0],m,s,q)

    for y_col in range(sudoku_len):
        try_to_remove_sudoku_value(x,y_col,m[y][x][0],m,s,q)


    x_bd = (x // 3) * 3
    y_bd = (y // 3) * 3
    for x_row in range(3):
        for y_col in range(3):
            try_to_remove_sudoku_value(x_bd+x_row,
                                       y_bd+y_col,
                                       m[y][x][0],m,s,q)



def solve_sudoku(puzzle):
    for line in puzzle:
        for sq in line:
            if len(sq) == 1:
                print(sq[0],end=" ")
            else:
                print("-",end=" ")
        print()


    
    # Returns numbers (1,1), (1,2), (1,3) as 3 digit number.
    m = [ [ [d for d in digits] for m in range(sudoku_len)]
        for n in range(sudoku_len)]
    # m is a matrix of all possible values
    s = [ [False for m in range(sudoku_len)]
        for n in range(sudoku_len)]
    # s maintains whether a node has been seen or not
    q = queue.Queue() # use a queue to maintain the ordering

    for y in range(sudoku_len):
        for x in range(sudoku_len):
            if int(puzzle[y][x]):
                m[y][x] = [int(puzzle[y][x])]
                add_to_queue(x,y,s,q)

    while not q.empty():
        (x,y) = q.get()
        sudoku_process(x,y,m,s,q)

    print()

    for line in m:
        for sq in line:
            if len(sq) == 1:
                print(sq[0],end=" ")
            else:
                print("-",end=" ")
        print()

#    return sum(m[0][:3])
    return 0

    

puzzles = []
cur_puzzle = []
f = open("p096_sudoku.txt")
f.readline()
for line in f:
    if line.startswith("Grid"):
        puzzles.append(cur_puzzle)
        cur_puzzle = []
    else:
        cur_puzzle.append(list(line.strip()))


top_left_sum = 0
print(solve_sudoku(puzzles[0]))
#print(puzzles[0])
#for puzzle in puzzles:
#    top_left_sum += solve_sudoku(puzzle)

print(top_left_sum)
#Ok, now I have all the puzzles
