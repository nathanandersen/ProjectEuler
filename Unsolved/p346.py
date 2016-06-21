# Problem 346
upperLim = 40 # 40 1's, for base 2

def evalBase(length,b):
    # Evaluate string n in base b
    t = 0
    for i in range(length):
        t += b ** i
    return t

repunits = set()
repunitMultiples = set()
total = 1
target = 10 ** 12

for length in range(2,upperLim):
    n = 2
    while True:
        t = evalBase(length,n)
        print(t)
        if t > target:
            break
        if t in repunits:
            repunitMultiples.add(t)
        else:
            repunits.add(t)
        n += 1
    print(length)

print(sum(repunitMultiples))

    # put together strings of 1's
    # calculate the base...
