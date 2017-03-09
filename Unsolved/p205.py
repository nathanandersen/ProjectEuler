import itertools as it
peter = [1,2,3,4]
colin = [1,2,3,4,5,6]

peter_prob = (1/4) ** 9
colin_prob = (1/6) ** 6
single_prob = peter_prob * colin_prob

peter_rolls = it.product(peter,peter,peter,peter,peter,peter,peter,peter,peter)
colin_rolls = it.product(colin,colin,colin,colin,colin,colin)

total_pr = 0
for p,c in it.product(peter_rolls,colin_rolls):
    print(p,c)
    if sum(p) > sum(c):
        total_pr += single_prob

print(total_pr)
