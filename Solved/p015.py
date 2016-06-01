# Problem 15

# real 0m0.046s
# user 0m0.026s
# sys  0m0.010s


def calc_steps(n):
    return 2 if n==1 else int((4*n-2) * calc_steps(n-1)/n)

print(calc_steps(20))

