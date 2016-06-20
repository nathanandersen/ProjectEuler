# Problem 85

# given a rectangle that is x by y,

# there are 1 <= a <= x, where a is the side
# length
# there are (x-a)+1 possible positions for this
# rectangle on each bit

# equations:
# x^2*y^2 + x^2*y + x*y^2 + xy > 8,000,000
# x*y * (x*y + x + y + 1)

# min x*y

def rect_count(x,y):
    x2 = x**2
    y2 = y**2
    return int(((x2*y2) + (x*y2) + (x2*y) + (x*y))/4)

print(rect_count(3,2))
print(rect_count(4,2))
