# Problem 15

# real 0m0.046s
# user 0m0.026s
# sys  0m0.010s


def calc_steps(n):
    return 2 if n==1 else int((4*n-2) * calc_steps(n-1)/n)

# This is the blunt force approach (with recursion)
# Obviously works well in small cases.
def takesteps(x,y,xlim,ylim):
    routes = 0
    if x < xlim:
        routes += takesteps(x+1,y,xlim,ylim)
    if y < ylim:
        routes += takesteps(x,y+1,xlim,ylim)
    return routes if routes else 1

print(calc_steps(20))

