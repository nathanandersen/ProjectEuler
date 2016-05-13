# Problem 14

# This could probably still be improved
# even more with a better DP.

#real	0m3.296s
#user	0m3.177s
#sys	0m0.088s

# n -> n/2 (even)
# n -> 3n + 1 (odd)

step_counts = {}

def collatz_steps(n):
    i = 1
    while(n-1):
        if n in step_counts:
            return i + step_counts[n]
        else:
            n = 3*n+1 if n%2 else n/2
            i += 1
    return i

def max_collatz():
    (max_steps,n) = (0,0)
    for i in range(1,1000000):
        steps = collatz_steps(i)
        step_counts[i] = steps
        if (steps > max_steps):
            max_steps = steps
            n = i
    return n
print(max_collatz())
