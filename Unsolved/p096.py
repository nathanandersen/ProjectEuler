# Problem 96
import copy
import random

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
digits = [1,2,3,4,5,6,7,8,9]
sudoku_len = 9

def is_solved(m):
    row_vals = [{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} for n in range(sudoku_len)]
    col_vals = [{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} for n in range(sudoku_len)]
    sec_vals = [{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} for n in range(sudoku_len)]
    # 1 2 3
    # 4 5 6
    # 7 8 9

    for y in range(sudoku_len):
        for x in range(sudoku_len):
            if not m[y][x]: return
            v = m[y][x]
            row_vals[y][v] += 1
            col_vals[x][v] += 1
            sec = (y//3)*3+(x//3)
            sec_vals[sec][v] += 1

    for rv in row_vals:
        for (key,val) in rv.items():
            if val is not 1: return False

    for cv in col_vals:
        for (key,val) in cv.items():
            if val is not 1: return False

    for sv in sec_vals:
        for (key,val) in sv.items():
            if val is not 1: return False
    return True

def try_to_remove_sudoku_value(x,y,v,m,s):
    if s[y][x]:
        return
    try:
        m[y][x].remove(v)
    except ValueError:
        pass

def increment_dict(d,key):
    try:
        d[key] += 1
    except KeyError:
        pass


def sudoku_process(x,y,m,s,q):
    # Update all values in the region to not have any of the same
    # digit that is in this value


    # Pseudocode:
    # Remove all of the same value from the row, and column
    # then check the whole row and the column.
    # if anything in the row and column is UNIQUE, ie, there is
    # only one 1, then mark that as finished and push to the
    # queue.

    row_vals = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for x_row in range(sudoku_len):
        if s[y][x_row]:
#            print(x_row,y)
            row_vals.pop(s[y][x_row])
        else:
            for v in m[y][x_row]:
                increment_dict(row_vals,v)

        try_to_remove_sudoku_value(x_row,y,s[y][x],m,s)

    for (key,val) in row_vals.items():
        if val is 1:
            for x_row in range(sudoku_len):
                if not s[y][x_row] and key in m[y][x_row]:
                    s[y][x_row] = key
                    q.put((x_row,y))

    # maintain a dictionary of nums -> occurrences
    col_vals = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for y_col in range(sudoku_len):
        if s[y_col][x]:
            col_vals.pop(s[y_col][x])
        else:
            for v in m[y_col][x]:
                increment_dict(col_vals,v)
        try_to_remove_sudoku_value(x,y_col,s[y][x],m,s)

    # if any of them are 1, ie, unique
    for (key,val) in col_vals.items():
        if val is 1:
            for y_col in range(sudoku_len):
                # mark it, add it to the queue
                if not s[y_col][x] and key in m[y_col][x]:
                    s[y_col][x] = key
                    q.put((x,y_col))


    x_bd = (x // 3) * 3
    y_bd = (y // 3) * 3
    sec_vals = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for x_row in range(3):
        for y_col in range(3):
            local_y = y_bd + y_col
            local_x = x_bd + x_row
            if s[local_y][local_x]:
                try:
                    sec_vals.pop(s[local_y][local_x])
                except KeyError:
                    print_puzzle(s)
                    print(local_x,local_y,s[local_y][local_x])
                    print(sec_vals)
                    # Aha! SOmetimes, there are two of the
                    # same number in a section! That means
                    # I have made a mistake somewhere!
                    exit()

            else:
                for v in m[local_y][local_x]:
                    increment_dict(sec_vals,v)
            try_to_remove_sudoku_value(local_x,local_y,
                                       s[y][x],m,s)


    for (key,val) in sec_vals.items():
        if val is 1:
            for x_row in range(3):
                for y_col in range(3):
                    if not s[y_bd+y_col][x_bd+x_row] and key in m[y_bd+y_col][x_bd+x_row]:
                        s[y_bd+y_col][x_bd+x_row] = key
                        q.put((x_bd+x_row,y_bd+y_col))


def print_puzzle(p):
    for line in p:
        for sq in line:
            if sq is 0: print("-",end=" ")
            else: print(sq,end=" ")
        print()

    print()

def conditional_solve(local_m,local_s):
    # have to build randomness into this
    m = copy.deepcopy(local_m)
    s = copy.deepcopy(local_s)
    q = queue.Queue()
    unsolved = []
    for x in range(sudoku_len):
        for y in range(sudoku_len):
            if not s[y][x]:
                unsolved.append((x,y))

    selection = random.randint(0,len(unsolved)-1)
    (x,y) = unsolved[selection]
    cur_list = m[y][x]

    s[y][x] = cur_list[random.randint(0,len(cur_list)-1)]

    q.put((x,y))

    while not q.empty():
        (x,y) = q.get()
        sudoku_process(x,y,m,s,q)

    return s


def solve_sudoku(puzzle,i):

    # Returns numbers (1,1), (1,2), (1,3) as 3 digit number.
    m = [ [ [d for d in digits] for m in range(sudoku_len)]
        for n in range(sudoku_len)]
    # m is a matrix of all possible values

    #s maintains final values
    s = [ [0 for m in range(sudoku_len)]
        for n in range(sudoku_len)]
    q = queue.Queue() # use a queue to maintain the ordering

    for y in range(sudoku_len):
        for x in range(sudoku_len):
            if int(puzzle[y][x]):
                s[y][x] = int(puzzle[y][x])
                q.put((x,y))

    while not q.empty():
        (x,y) = q.get()
        sudoku_process(x,y,m,s,q)
        # solves as much as we know for certain, up to here

#    t = m
    t = s
    while not is_solved(t):
#        # do some randomness
        t = conditional_solve(m,s)
        print_puzzle(t)
        print(i)



    print_puzzle(puzzle)
    print_puzzle(t)

    string = ""
    for x in range(3):
        string += str(t[0][x])
    print(int(string))

    return int(string)



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
#solve_sudoku(puzzles[0],0)
for i in range(len(puzzles)):
    top_left_sum += solve_sudoku(puzzles[i],i)
print(top_left_sum)
