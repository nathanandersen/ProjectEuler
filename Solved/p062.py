# Problem 62

#real	0m0.120s
#user	0m0.096s
#sys	0m0.014s

# We will have a dictionary (or structure) of tuples -> cube numbers
cubeStruct = {}

n = 1
while True:
    c = n ** 3
    t = tuple(sorted([int(d) for d in str(c)]))
    d = cubeStruct.get(t)
    if d is None:
        cubeStruct[t] = [c]
    else:
        l = cubeStruct[t]
        if len(l) == 4:
            print(min(l))
            exit()
        l.append(c)
        cubeStruct[t] = l
    n += 1
