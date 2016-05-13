# Problem 6

# real 0m0.043s
# user 0m0.025s
# sys  0m0.010s

def find_squared_sum(a):
    return (sum(i for i in range(0,a))**2)

def find_sum_of_squares(a):
    return (sum(i**2 for i in range(0,a)))

print( find_squared_sum(101) - find_sum_of_squares(101))

