# Problem 81

fives = []
fives.append([131,673,234,103,18])
fives.append([201,96,342,965,150])
fives.append([630,803,746,422,111])
fives.append([537,699,497,121,956])
fives.append([805,732,524,37,331])

matrix = []
#parse the file
with open("p081_matrix.txt","r") as f:
    for text in f:
        text = eval("[" + text + "]")
        matrix.append(text)
# matrix is a 80x80 list..

def replace_element(m,x,y):
    max_x = len(m) -1
    max_y = len(m[0])-1
    if x == max_x and y == max_y:
        1
    elif x == max_x:
        m[x][y] += m[x][y+1]
    elif y == max_y:
        m[x][y] += m[x+1][y]
    else:
        m[x][y] += min(m[x+1][y],m[x][y+1])
    return m

def solve(m):
    max_x = len(m)-1
    max_y = len(m[0])-1
    for total in range(max_x+max_y,-1,-1):
        for x in range(max_x,-1,-1):
            if not (max_y >= total-x >= 0):
                continue
            else:
                m = replace_element(m,x,total-x)
    return(m[0][0])
print(solve(matrix))
#print(solve(fives))
