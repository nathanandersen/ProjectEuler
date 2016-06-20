# Problem 173
squares = {n**2 for n in range(1,10**3+1)}

total = 0
upperLim = 100 + 1
for n in range(8,upperLim):
    for s in squares:
        if n + s in squares:
            print(n,s,n+s)
            total += 1
    print(n)

print(total)
