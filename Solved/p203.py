# Problem 203

#real	0m0.048s
#user	0m0.029s
#sys	0m0.012s

pascal = [[0 for n in range(k+1)] for k in range(51)]

primeSquares = [x*x for x in [2,3,5,7,11,13,15,17,19,23]]

def isSquarefree(n):
    for p in primeSquares:
        if n % p == 0:
            return False
    return True

nums = set([1])
for n in range(51):
    pascal[n][0] = 1
    pascal[n][n] = 1
    for k in range(1,n):
        v = pascal[n-1][k-1] + pascal[n-1][k]
        pascal[n][k] = v
        nums.add(v)

total = 0
for n in nums:
    if isSquarefree(n):
        total += n
print(total)
