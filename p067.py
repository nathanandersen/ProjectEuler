# Problem 67

triangle = []
with open("p067_triangle.txt","r") as f:
    while(1):
        tri_line = []
        line = f.readline()
        if line == '': break
        for num in line.split():
            tri_line.append(int(num))
        triangle.append(tri_line)

for i in range(98,-1,-1):
    for j in range(i+1):
        triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])

print(triangle[0][0])
