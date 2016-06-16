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
def setValue(x,y,solution,gridSet):
    if isinstance(solution[y][x],int): return
    solution[y][x] = solution[y][x][0]
    gridSet.add((x,y))
    eliminatePossibilities(x,y,solution,gridSet)
def removeValFromSquarePossibilities(x,y,v,solution,gridSet):
    if isinstance(solution[y][x],int): return
    try:
        solution[y][x].remove(v)
        if len(solution[y][x]) == 1:
            setValue(x,y,solution,gridSet)
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
            print("error in row")
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
            print("error in col")
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
            print("error in section")
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
    xMin = (x//3)*3
    yMin = (y//3)*3
    for dx in range(3):
        for dy in range(3):
            removeValFromSquarePossibilities(xMin+dx,yMin+dy,solution[y][x],solution,gridSet)
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
def findOccurrencesInRow(digit,puzzle,row):
    occurrences = []
    for col in range(sudokuLen):
        if isinstance(puzzle[row][col],int):
            if puzzle[row][col] == digit:
                return None
        elif digit in puzzle[row][col]:
            occurrences.append((col,row))
    return occurrences
def occurrencesInSameSection(occ):
    if len(occ) > 3:
        return False
    if len(occ) == 3:
        return (occ[0][0]//3 == occ[1][0]//3 and occ[1][0]//3 == occ[2][0]//3 and occ[0][1]//3 == occ[1][1]//3 and occ[1][1]//3 == occ[2][1]//3)
    elif len(occ) == 2:
        return occ[0][0]//3 == occ[1][0]//3 and occ[0][1]//3 == occ[1][1]//3
    else:
        return True
def smartCheckSectionsByRow(puzzle,gridSet):
    # For each row, if say, 2 is only available in the
    # pieces of the row in that section, remove it everywhere
    # else in that section.
    for row in range(sudokuLen):
        sectY = row//3 * 3
        for digit in digits:
            occurrences = findOccurrencesInRow(digit,puzzle,row)
            if occurrences is not None and occurrencesInSameSection(occurrences):
                sectX = occurrences[0][0] // 3 * 3
                for dx in range(3):
                    for dy in range(3):
                        if (sectX+dx,row) not in occurrences:
                            removeValFromSquarePossibilities(sectX+dx,sectY+dy,digit,puzzle,gridSet)
def findOccurrencesInColumn(digit,puzzle,col):
    occurrences = []
    for row in range(sudokuLen):
        if isinstance(puzzle[row][col],int):
            if puzzle[row][col] == digit:
                return None
        elif digit in puzzle[row][col]:
            occurrences.append((col,row))
    return occurrences
def smartCheckSectionsByColumn(puzzle,gridSet):
    for col in range(sudokuLen):
        sectX = col//3 * 3
        for digit in digits:
            occurrences = findOccurrencesInColumn(digit,puzzle,col)
            if occurrences is not None and occurrencesInSameSection(occurrences):
                sectY = occurrences[0][1] // 3 * 3
                for dx in range(3):
                    for dy in range(3):
                        if (col,sectY+dy) not in occurrences:
                            removeValFromSquarePossibilities(sectX+dx,sectY+dy,digit,puzzle,gridSet)
def occurrencesInSameRow(occ):
    if len(occ) > 3:
        return False
    if len(occ) == 3:
        return occ[0][1] == occ[1][1] and occ[1][1] == occ[2][1]
    elif len(occ) == 2:
        return occ[0][1] == occ[1][1]
    else:
        return True
def occurrencesInSameColumn(occ):
    if len(occ) > 3:
        return False
    if len(occ) == 3:
        return occ[0][0] == occ[1][0] and occ[1][0] == occ[2][0]
    elif len(occ) == 2:
        return occ[0][0] == occ[1][0]
    else:
        return True
def findOccurrencesInSection(digit,puzzle,xMin,yMin):
    o = []
    for dx in range(3):
        for dy in range(3):
            if isinstance(puzzle[yMin+dy][xMin+dx],int):
                if puzzle[yMin+dy][xMin+dx] == digit:
                    return None
            elif digit in puzzle[yMin+dy][xMin+dx]:
                o.append((xMin+dx,yMin+dy))
    return o
def smartCheckRowsBySection(puzzle,gridSet):
    for xMin in range(0,sudokuLen,3):
        for yMin in range(0,sudokuLen,3):
            for digit in digits:
                occurrences = findOccurrencesInSection(digit,puzzle,xMin,yMin)
                if occurrences is not None and occurrencesInSameRow(occurrences):
                    # iterate over the row and remove everything not in occurrences
                    row = occurrences[0][1]
                    for col in range(sudokuLen):
                        if (col,row) not in occurrences:
                            removeValFromSquarePossibilities(col,row,digit,puzzle,gridSet)
def smartCheckColumnsBySection(puzzle,gridSet):
    for xMin in range(0,sudokuLen,3):
        for yMin in range(0,sudokuLen,3):
            for digit in digits:
                occurrences = findOccurrencesInSection(digit,puzzle,xMin,yMin)
                if occurrences is not None and occurrencesInSameColumn(occurrences):
                    # iterate over the row and remove everything not in occurrences
                    col = occurrences[0][0]
                    for row in range(sudokuLen):
                        if (col,row) not in occurrences:
                            removeValFromSquarePossibilities(col,row,digit,puzzle,gridSet)

def smartCheck(p,gridSet):
    # If a section is lacking value v, and v is only possible
    # in a row or a column, than we can remove v from that
    # row and column in other sections

    # Similarly, if a row or column is lacking value v, and v is only
    # possible in a given section, then we can remove v from other entries
    # in that section.

    simpleSmartCheck(p,gridSet)

    smartCheckRowsBySection(p,gridSet)
    smartCheckColumnsBySection(p,gridSet)
    smartCheckSectionsByRow(p,gridSet)
    smartCheckSectionsByColumn(p,gridSet)


def simpleSmartCheck(p,gridSet):
    for num in range(sudokuLen):
        checkForUniqueValuesInRow(num,p,gridSet)
        checkForUniqueValuesInColumn(num,p,gridSet)
    for x in range(0,sudokuLen,3):
        for y in range(0,sudokuLen,3):
            checkForUniqueValuesInSection(x,y,p,gridSet)

def solveSudoku(p):
    solution = createSolutionMatrix(p)
    gridSet = prepareSet(solution)

    iterCount = 1
    while True:
        try:
            (x,y) = gridSet.pop()
            eliminatePossibilities(x,y,solution,gridSet)
        except KeyError:

            if isSolved(solution):
                print("solved in",iterCount,"attempts")
                return solution[0][0]*100 + solution[0][1]*10 + solution[0][2]
            else:
                iterCount += 1
                smartCheck(solution,gridSet)
#                if iterCount > 10:
#                    superSmartCheck(solution,gridSet)
                if iterCount % 100 == 0:
                    prettyPrint(solution)



if __name__ == "__main__":
    puzzles = []
    curPuzzle = []
    topLeftSum = 0
    f = open("p096_sudoku.txt")
    f.readline()
    for line in f:
        if line.startswith("Grid"):
#            print("solving a puzzle.")
            puzzles.append(curPuzzle)
            topLeftSum += solveSudoku(curPuzzle)
            curPuzzle = []
        else:
            curPuzzle.append(list(line.strip()))

    print(topLeftSum)
