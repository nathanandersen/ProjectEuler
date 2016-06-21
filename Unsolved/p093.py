# Problem 93

def formIntegerTargets(a,b,c,d):
    ints = set()


for d in range(1,10):
    for c in range(1,d):
        for b in range(1,c):
            for a in range(1,b):
                formIntegerTargets(a,b,c,d)
