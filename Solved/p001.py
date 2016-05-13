# Problem 1 from Project Euler.

# real 0m0.044s
# user 0m0.026s
# sys  0m0.010s

print(sum(i if (not i%3 or not i%5) else 0 for i in range(1000)))
