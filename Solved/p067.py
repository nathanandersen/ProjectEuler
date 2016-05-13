# Problem 67

# real 0m0.051s
# user 0m0.032s
# sys  0m0.010s

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
