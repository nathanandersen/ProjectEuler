# Problem 346
#real	0m2.251s
#user	0m2.157s
#sys	0m0.071s

upperLim = 40 # 40 1's, for base 2

def evalBase(length,b):
    # Evaluate string n in base b
    t = 0
    for i in range(length):
        t += b ** i
    return t

def calcRepunits(length):
    base = 2
    while True:
        t = evalBase(length,base)
        if t > target: return
        repunits.add(t)
        base += 1

repunits = set([1])
target = 10 ** 12

for length in range(3,upperLim):
    # n = 11 in base n-1
    calcRepunits(length)

print(sum(repunits))
