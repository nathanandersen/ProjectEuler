# Problem 2
# Consider the Fibonacci numbers below four million
# Find the sum of the even valued terms.

prev = 1
cur = 2
total = 0

def next_fibo(p,c):
    return (c,p+c)

while cur < 4000000:
    total += (cur if not cur%2 else 0)
    (prev,cur) = next_fibo(prev,cur)

print(total)
#print (sum)
