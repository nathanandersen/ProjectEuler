# Problem 76

# perhaps try and find a pattern or speed this up..?
# it works, but *** 
def find_sums(n):
    return take_steps(n,n)

def take_steps(n,largest):
    total = 1
    if n < 0:
        return 0
    if n==0 or n == 1:
        return 1
    for i in range(2,largest):
        total += take_steps(n-i,i+1)
    return total

print(find_sums(100))

# 2: 1
# 3: 2 (+1)
# 4: 4 (+2)
# 5: 6 (+2)
# 6: 10 (+4)
# 7: 14 (+4)
# 8: 21 (+7)
# 9: 29 (+8)
# 10: 41 (+12)
# 11: 55 (+14)
# 12: 76 (+21)
# 13: 100 (+24)
# 14: 134 (+34)
# 15: 175 (+41)
