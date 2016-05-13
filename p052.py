#Problem 52
import sys

def is_solution(x):
    digit_set = [digit for digit in str(x)]
    for i in range(2,7):
        for d in [digit for digit in str(x*i)]:
            if d not in digit_set:
                return 0
    return 1

for x in range(1,1000000):
    if is_solution(x):
        print(x)
        sys.exit()
