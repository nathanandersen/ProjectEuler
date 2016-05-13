# Problem 39
# a + b + c = p (perimeter)
# a^2 + b^2 = c^2
# Find p with maximum number of solutions (a,b,c)

# a + b + c = perimeter
# c = p-b-a
# Some math. Probably could have used Euclid....

# a^2 + b^2 - (p-b-a)^2 = 0
# a^2 + b^2 - (p-b-a)(p-b-a) = 0
# a^2 + b^2 - (p^2 - pb - pa - pb + b^2 + ba - ap + ba + a^2) = 0
# a^2 + b^2 + (-p^2 + pb + pa + pb - b^2 - ba + ap - ba - a^2) = 0
# a^2 + b^2 + -p^2 + pb + pa + pb - b^2 - ba + ap - ba - a^2 = 0
# -p^2 + pb + pa + pb - ba + ap - ba = 0
# -p^2 + 2*p*b + 2*p*a - 2*ba = 0
# -p^2 + 2*p*b + a(2*p - 2*b) = 0
# a = (p^2 - 2*p*b) / (2*p - 2*b)
# a = p*(p - 2*b) / (2*p - 2*b)
# a = p*(p + p - p -2*b) / (2*p - 2*b)
# a = p*(2*p - p -2*b) / (2*p - 2*b)
# a = p*(2*p -2*b) / (2*p - 2*b) - p^2 / (2*p - 2*b)
# a = p - p^2 / (2*p - 2*b)
# Maximum # of solutions
from utils import is_right_triangle

def find_triangles(p):
    """Find all the right triangles for a given perimeter, p"""
    tris = []
    for b in range(p):
        a = p - int((p**2)/(2*p - 2*b))
        if a > 0 and b and is_right_triangle(a,b,(p-a-b)):
            tris.append([a,b,(p-a-b)])
    return(int(len(tris)))



max_triangles = 0
max_index = 0
for p in range(1,1000):
    n = find_triangles(p)
    if n > max_triangles:
        max_index = p
        max_triangles = n

print(max_index)
