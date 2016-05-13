
# Problem 1 from Project Euler.
# Find the sum of the multiples of 3 and 5 below 1000.

print(sum(i if (not i%3 or not i%5) else 0 for i in range(1000)))
