# Problem 96
# Solving Sudoku

digits = {d for d in range(1,10)}
sudokuLen = 9
# A Sudoku puzzle is a 9x9 list.
def prettyPrint(puzzle):
    for col in range(sudokuLen):
        for row in range(sudokuLen):
            if isinstance(puzzle[col][row],int):
                print(puzzle[col][row],end=" ")
            else:
                print(".",end=" ")
        print()
    print()
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
    except ValueError: pass
def checkForUniqueValuesInRow(y,solution,gridSet):
    for d in digits:
        numOccurrences = 0
        c = -1
        for col in range(sudokuLen):
            if isinstance(solution[y][col],int):
                if solution[y][col] == d:
                    numOccurrences = -1
                    break
            else:
                if d in solution[y][col]:
                    numOccurrences += 1
                    c = col
        if numOccurrences == 0:
            exit() # Error
        elif numOccurrences == 1:
            solution[y][c] = d
            gridSet.add((c,y))
def checkForUniqueValuesInColumn(x,solution,gridSet):
    for d in digits:
        numOccurrences = 0
        r = -1
        for row in range(sudokuLen):
            if isinstance(solution[row][x],int):
                if solution[row][x] == d:
                    numOccurrences = -1
                    break
            else:
                if d in solution[row][x]:
                    numOccurrences += 1
                    r = row
        if numOccurrences == 0:
            exit() # Error
        elif numOccurrences == 1:
            solution[r][x] = d
            gridSet.add((x,r))
def numOccurrencesInSection(d,xMin,yMin,solution):
    numOccurrences = 0
    (posX,posY) = (-1,-1)
    for dx in range(3):
        for dy in range(3):
            if isinstance(solution[yMin+dy][xMin+dx],int):
                if solution[yMin+dy][xMin+dx] == d:
                    numOccurrences = -1
                    return(-1,None,None)
            else:
                if d in solution[yMin+dy][xMin+dx]:
                    numOccurrences += 1
                    (posX,posY) = (xMin+dx,yMin+dy)
    return(numOccurrences,posX,posY)
def checkForUniqueValuesInSection(x,y,solution,gridSet):
    xMin = (x//3)*3
    yMin = (y//3)*3
    for d in digits:
        (numOccurrences,posX,posY) = numOccurrencesInSection(d,xMin,yMin,solution)
        if numOccurrences == -1:
            continue
        elif numOccurrences == 0:
            print(d,xMin,yMin)
            prettyPrint(solution)
            exit() # Error
        elif numOccurrences == 1:
            solution[posY][posX] = d
            gridSet.add((posX,posY))
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
    checkForUniqueValuesInRow(y,solution,gridSet)
    checkForUniqueValuesInColumn(x,solution,gridSet)
    checkForUniqueValuesInSection(x,y,solution,gridSet)
def isSolved(p):
    for x in range(sudokuLen):
        for y in range(sudokuLen):
            if not isinstance(p[y][x],int):
                return False
    return True

def smartCheckSectionsByRow(p,gridSet):
    # If a digit is missing in a section, and is only
    # available in a certain row, then remove it from
    # the rest of the section
    for d in digits:
        pass
def smartCheckSectionsByColumn(p,gridSet):
    pass


def findOccurrencesInRow(d,p,row):
    occurrences = []
    for col in range(sudokuLen):
        if isinstance(p[row][col],int):
            if p[row][col] == d:
                return None
        elif d in p[row][col]:
            occurrences.append((col,row))
    return occurrences
def smartCheckRowsBySection(p,gridSet):
        # If a digit is missing in a row,
        # and is only available in a certain section
        #, then remove it from the rest of the row

    for d in digits:
        for sect in range(sudokuLen):
            rowOccurrences = findOccurrencesInRow(d,p,sect)
            sectOccurrences = findOccurrencesInSection(d,p,sect)
            # If those occurrences
            # are the only ones in the section


    pass
def smartCheckColumnsBySection(p,gridSet):
    pass

def smartCheck(p,gridSet):
    # If a section is lacking value v, and v is only possible
    # in a row or a column, than we can remove v from that
    # row and column in other sections

    # Similarly, if a row or column is lacking value v, and v is only
    # possible in a given section, then we can remove v from other entries
    # in that section.
    smartCheckSectionsByRow(p,gridSet)
    smartCheckSectionsByColumn(p,gridSet)
    smartCheckRowsBySection(p,gridSet)
    smartCheckColumnsBySection(p,gridSet)

def solveSudoku(p):
    solution = createSolutionMatrix(p)
    gridSet = prepareSet(solution)

    while True:
        try:
            (x,y) = gridSet.pop()
            eliminatePossibilities(x,y,solution,gridSet)
        except KeyError:

            if isSolved(solution):
                prettyPrint(solution)
                return solution[0][0]*100 + solution[0][1]*10 + solution[0][2]
            else:
                smartCheck(solution,gridSet)
                # Do some harder cross-checking here.

                prettyPrint(solution)
                return 0



if __name__ == "__main__":
    puzzles = []
    curPuzzle = []
    topLeftSum = 0
    f = open("p096_sudoku.txt")
    f.readline()
    for line in f:
        if line.startswith("Grid"):
            puzzles.append(curPuzzle)
            topLeftSum += solveSudoku(curPuzzle)
            curPuzzle = []
        else:
            curPuzzle.append(list(line.strip()))

    print(topLeftSum)
#    for p in puzzles:
#        topLeftSum += solveSudoku(p)
#        print(solveSudoku(p))
#    solveSudoku(puzzles[3])
