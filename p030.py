# Problem 30

total = 0
for n in range(10,354294):
    total += n if n == sum(int(digit) ** 5 for digit in str(n)) else 0
print(total)
