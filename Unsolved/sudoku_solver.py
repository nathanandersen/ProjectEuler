# Problem 96
# Solving Sudoku

# We will implement this with a queue
from queue import Queue

digits = {d for d in range(1,10)}
sudokuLen = 9


# Elementary algorithm:

# Add all squares in grid to the queue.
# While queue is not empty:
    # If the square is unsolved:
        #add it to the back of the queue
    # Else:
        #then apply the Sudoku Rules
        # to eliminate its number from row/column/section.
        # Do not re-add to queue.

# A Sudoku puzzle is a 9x9 list.

def createSolutionMatrix(p):
    # Pre-process
    s = p.copy()
    for x in range(sudokuLen):
        for y in range(sudokuLen):
            if p[y][x] == '0':
                s[y][x] = [d for d in digits]
            else:
                s[y][x] = int(p[y][x])

    return s
def prepareQueue():
    # Return a queue with all squares in the sudoku matrix
    q = Queue()
    for x in range(sudokuLen):
        for y in range(sudokuLen):
            q.put((x,y))

    return q
def prepareSet(p):
    # Return a set with all the solved squares in the
    # sudoku matrix
    s = set()
    for x in range(sudokuLen):
        for y in range(sudokuLen):
            if isinstance(p[y][x],int):
                s.add((x,y))

    return s

def removeValFromSquarePossibilities(x,y,v,solution,gridSet):
    if isinstance(solution[y][x],int): return

    try:
        solution[y][x].remove(v)
        if len(solution[y][x]) == 1:
            solution[y][x] = solution[y][x][0]
            gridSet.add((x,y))
    except ValueError:
        pass


def eliminateInRow(x,y,solution,gridSet):
    for col in range(sudokuLen):
        removeValFromSquarePossibilities(col,y,solution[y][x],solution,gridSet)
def eliminateInColumn(x,y,solution,gridSet):
    for row in range(sudokuLen):
        removeValFromSquarePossibilities(x,row,solution[y][x],solution,gridSet)
def eliminateInSection(x,y,solution,gridSet):
    x_min = (x//3)*3
    y_min = (y//3)*3
    for dx in range(3):
        for dy in range(3):
            removeValFromSquarePossibilities(x_min+dx,y_min+dy,solution[y][x],solution,gridSet)
def eliminatePossibilities(x,y,solution,gridSet):
    eliminateInRow(x,y,solution,gridSet)
    eliminateInColumn(x,y,solution,gridSet)
    eliminateInSection(x,y,solution,gridSet)

def prettyPrint(puzzle):
    for col in range(sudokuLen):
        for row in range(sudokuLen):
            if isinstance(puzzle[col][row],int):
                print(puzzle[col][row],end=" ")
            else:
                print("?",end=" ")
        print()
    print()

def solveSudoku(p):
    solution = createSolutionMatrix(p)
    gridSet = prepareSet(solution)

    while True:
        try:
            (x,y) = gridSet.pop()
            eliminatePossibilities(x,y,solution,gridSet)
        except KeyError:
            prettyPrint(solution)
            return



if __name__ == "__main__":
    puzzles = []
    curPuzzle = []
    f = open("p096_sudoku.txt")
    f.readline()
    for line in f:
        if line.startswith("Grid"):
            puzzles.append(curPuzzle)
            curPuzzle = []
        else:
            curPuzzle.append(list(line.strip()))

    for p in puzzles:
        solveSudoku(p)
#    solveSudoku(puzzles[0])
