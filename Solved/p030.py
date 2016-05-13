# Problem 30

# real 0m1.769s
# user 0m1.734s
# sys  0m0.016s

total = 0
for n in range(10,354294):
    total += n if n == sum(int(digit) ** 5 for digit in str(n)) else 0
print(total)
