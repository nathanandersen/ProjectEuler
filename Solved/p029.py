# Problem 29

# real 0m0.056s
# user 0m0.036s
# sys  0m0.010s

powers = []

for a in range(2,101):
    for b in range(2,101):
        powers.append(a ** b)

print(len(set(powers)))
