# Problem 85
#real	0m0.071s
#user	0m0.048s
#sys	0m0.009s

# given a rectangle that is x by y,

# there are 1 <= a <= x, where a is the side
# length
# there are (x-a)+1 possible positions for this
# rectangle on each bit

# equations:
# x^2*y^2 + x^2*y + x*y^2 + xy > 2,000,000
# x*y * (x*y + x + y + 1)

# min x*y

def rect_count(x,y):
    x2 = x**2
    y2 = y**2
    return int(((x2*y2) + (x*y2) + (x2*y) + (x*y))/4)

closest = 0
_x,_y = 0,0
for x in range(1,100):
    for y in range(1,100):
        c = rect_count(x,y)
        if abs(2000000-c) < abs(2000000-closest):
            _x,_y,closest = x,y,c

print(_x,_y,closest)


def alt_rect_count(x,y):
    total = 0
    for x_len in range(1,x+1):
        for y_len in range(1,y+1):
            total += (x-x_len+1) * (y-y_len+1)
    return total
