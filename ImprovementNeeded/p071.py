# Problem 71

def findClosestFraction(n):
    base = 3*n//7 - 1
    while True:
        if base/n >= 3/7: return base-1
        base += 1
if __name__ == "__main__":
    target = 10**6
    max_n = 1
    max_d = 1000
    for d in range(2,target):
        print(d)
        n = findClosestFraction(d)
        if (n/d) > (max_n/max_d):
            max_n = n
            max_d = d

    print(max_n,max_d)
