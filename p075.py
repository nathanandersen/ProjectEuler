# Problem 75
from utils import is_right_triangle

# Not efficient enough
def has_one_triangle(p):
    """Return whether there is only one triangle for a given perimeter."""
    tris = []
    for b in range(p):
        a = p - int((p**2)/(2*p - 2*b))
        if a > 0 and b and is_right_triangle(a,b,(p-a-b)):
            tris.append([a,b,(p-a-b)])
            if len(tris) > 1: return 0
    return 1

count = 0
for l in range(1500000):
    print(l)
    if has_one_triangle(l):
        count += 1


print(count)
