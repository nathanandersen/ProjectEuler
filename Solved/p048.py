# Problem 48

# real 0m0.054s
# user 0m0.034s
# sys  0m0.009s

total = sum(i ** i for i in range(1,1000))
total = str(total)
print(total[len(total)-10:len(total)])
