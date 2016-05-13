#Problem 43
from itertools import permutations

def is_valid_solution(p):
    p = str(p)
    return (len(p) == 10
            and not int(p[1:4])%2
            and not int(p[2:5])%3
            and not int(p[3:6])%5
            and not int(p[4:7])%7
            and not int(p[5:8])%11
            and not int(p[6:9])%13
            and not int(p[7:10])%17)

digits = [0,1,2,3,4,5,6,7,8,9]
pan_ints = {''.join(map(str,tup)) for tup in permutations(digits)}
print(sum(int(p) for p in pan_ints if is_valid_solution(p)))
