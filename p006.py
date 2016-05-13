# Problem 6
# Find the difference between the sum of the first 100 numbers,
# squared, and the sum of their squares


def find_squared_sum(a):
    return (sum(i for i in range(0,a))**2)

def find_sum_of_squares(a):
    return (sum(i**2 for i in range(0,a)))

print( find_squared_sum(101) - find_sum_of_squares(101))

