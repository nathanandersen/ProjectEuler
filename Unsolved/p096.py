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
digits = {d for d in range(1,10)}
sudoku_len = 9


def print_puzzle(p):
    for line in p:
        for sq in line:
            if len(sq) is not 1: print("-",end=" ")
            else: print(sq[0],end= " ")
        print()
    print()
def print_puzzle_pair(orig,solved):
    for row in range(sudoku_len):
        for sq in orig[row]:
            print(sq,end=" ")
        print("  ",end=" ")
        for sq in solved[row]:
            if len(sq) is not 1: print("-",end=" ")
            else: print(sq[0],end=" ")
        print()
    print()
def is_solved(m):
    # Given a solution matrix, m, return if it is a valid solution.
    row_vals = [{d:0 for d in digits} for n in range(sudoku_len)]
    col_vals = [{d:0 for d in digits} for n in range(sudoku_len)]
    sec_vals = [{d:0 for d in digits} for n in range(sudoku_len)]

    for y in range(sudoku_len):
        for x in range(sudoku_len):
            if len(m[y][x]) is not 1: return False
            v = m[y][x][0]
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
def increment_existing_value(d,key):
    try: d[key] += 1
    except KeyError: return
def update_existing_value(d,key,value):
    try: d[key]
    except KeyError: return
    d[key] = value
def check_for_uniqueness(vals,indexes,m,s,u):
    for (k,v) in vals.items():
        if v is 1:
            (x,y) = indexes[k]
            m[y][x] = [k]
            s[y][x] = True
            u.add((x,y))

def check_in_section(x,y,m,s,q):
    row_vals = {d:0 for d in digits}
    row_indexes = {d:(0,0) for d in digits}
    for row in range(sudoku_len):
        if s[row][x]:
            # If we've seen it, remove it and don't track it\
            try:
                row_vals.pop(m[row][x][0])
            except KeyError:
                print_puzzle(m)
                print(x,row,m[row][x])
            row_indexes.pop(m[row][x][0])
        else:
            for v in m[row][x]:
                increment_existing_value(row_vals,v)
                update_existing_value(row_indexes,v,(x,row))

    col_vals = {d:0 for d in digits}
    col_indexes = {d:(0,0) for d in digits}
    for col in range(sudoku_len):
        if s[y][col]:
            # If we've seen it, remove it and don't track it
            try:
                col_vals.pop(m[y][col][0])
            except KeyError:
                print_puzzle(m)
                print(col,y,m[y][col])
            col_indexes.pop(m[y][col][0])
        else:
            for v in m[y][col]:
                increment_existing_value(col_vals,v)
                update_existing_value(col_indexes,v,(col,y))


    sec_vals = {d:0 for d in digits}
    sec_indexes = {d:(0,0) for d in digits}
    y_base = (y//3)*3
    x_base = (x//3)*3
    for x_inc in range(3):
        for y_inc in range(3):
            x_nu = x_base + x_inc
            y_nu = y_base + y_inc
            if s[y_nu][x_nu]:
                try:
                    sec_vals.pop(m[y_nu][x_nu][0])
                except KeyError:
                    print_puzzle(m)
                    print(x_nu,y_nu,m[y_nu][x_nu])
                sec_indexes.pop(m[y_nu][x_nu][0])
            else:
                for v in m[y_nu][x_nu]:
                    increment_existing_value(sec_vals,v)
                    update_existing_value(sec_indexes,v,(x_nu,y_nu))


    u = set()
    check_for_uniqueness(row_vals,row_indexes,m,s,u)
    check_for_uniqueness(col_vals,col_indexes,m,s,u)
    check_for_uniqueness(sec_vals,sec_indexes,m,s,u)

    for tup in u:
        q.put(tup)

def remove_sudoku_value(v,x,y,m,s,q):
    # Remove value v from m[y][x]
    if s[y][x]: return
    try: m[y][x].remove(v)
    except ValueError: pass

    check_in_section(x,y,m,s,q)

def sudoku_process(x,y,m,s,q):
    # Update all values in the region to not have any of the same
    # digit that is in this value


    # Pseudocode:
    # Remove all of the same value from the row, and column
    # then check the whole row and the column.
    # if anything in the row and column is UNIQUE, ie, there is
    # only one 1, then mark that as finished and push to the
    # queue.

    v = m[y][x][0]
    for col in range(sudoku_len):
        remove_sudoku_value(v,col,y,m,s,q)

    for row in range(sudoku_len):
        remove_sudoku_value(v,x,row,m,s,q)

    y_bd = (y//3)*3
    x_bd = (x//3)*3
    for row in range(3):
        for col in range(3):
            remove_sudoku_value(v,x_bd+col,y_bd+row,m,s,q)


def sudoku_loop(m,s,q):
    while not q.empty():
        (x,y) = q.get()
        print(x,y)
        sudoku_process(x,y,m,s,q)

    # Once we've touched everything.. try again, just once.

    unsolved = []

    for x in range(sudoku_len):
        for y in range(sudoku_len):
            if len(m[y][x]) != 1:
#                print(s[y][x],m[y][x])
                unsolved.append((x,y))


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
    m[y][x] = [random.choice(m[y][x])]
    s[y][x] = True
    print("random choice: ",x,y)

    q.put((x,y))

    sudoku_loop(m,s,q)

    return m


def solve_sudoku(puzzle,i):

    # Returns numbers (1,1), (1,2), (1,3) as 3 digit number.
    m = [ [ [d for d in digits] for m in range(sudoku_len)]
        for n in range(sudoku_len)]
    # m is a matrix of all possible values

    # s is a "seen" matrix
    s = [ [False for m in range(sudoku_len)]
        for n in range(sudoku_len)]
    q = queue.Queue() # use a queue to maintain the ordering

    for y in range(sudoku_len):
        for x in range(sudoku_len):
            if int(puzzle[y][x]) != 0:
                m[y][x] = [int(puzzle[y][x])]
                s[y][x] = True
                q.put((x,y))


    sudoku_loop(m,s,q)

    t = m
    print_puzzle_pair(puzzle,t)
    while not is_solved(t):
        print("conditionally solving...")
#        # do some randomness
        t = conditional_solve(m,s)
        print_puzzle_pair(puzzle,t)


    print_puzzle_pair(puzzle,t)
    if is_solved(t):
        print("is solved")

    string = ""
    for x in range(3):
        string += str(t[0][x][0])
#    print(int(string))

    return int(string)


if __name__ == "__main__":
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
#    solve_sudoku(puzzles[2],2)
    for i in range(len(puzzles)):
        top_left_sum += solve_sudoku(puzzles[i],i)
    print(top_left_sum)
