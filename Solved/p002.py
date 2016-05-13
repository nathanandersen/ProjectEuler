# Problem 2

# real 0m0.061s
# user 0m0.038s
# sys  0m0.014s

prev = 1
cur = 2
total = 0

def next_fibo(p,c):
    return (c,p+c)

while cur < 4000000:
    total += (cur if not cur%2 else 0)
    (prev,cur) = next_fibo(prev,cur)

print(total)
