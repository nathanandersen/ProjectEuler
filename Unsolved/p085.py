# Problem 85

# given a rectangle that is x by y,

# there are 1 <= a <= x, where a is the side
# length
# there are (x-a)+1 possible positions for this
# rectangle on each bit




# 1 * (1 + 2 + 3 + ... + y) +
# 2 * (1 + 2 + .... + y) +
# ...
# + x * (1 + 2 + ... + y)
# = 1 * ( y*(y+1)/2) + 2*....
# = y*(y+1)/2 * x*(x+1)/2

# y*(y+1)*x*(x+1) / 4 -> close to 2 million
# (y^2+y)(x^2+x) / 4
# x^2 y^2 + x y^2 + x^2 y + xy > 8,000,000
# and are integers...
# how do i solve this?

def rect_count(x,y):
    total = 0
    for a in range(1,x+1):
        for b in range(1,y+1):
            total += a*b
    return total

print(rect_count(3,2))
