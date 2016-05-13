
#Problem 31
coins = [1,2,5,10,20,50,100,200]
global solutions
solutions = []

#Put tuples of the coin values in solutions

# When we look to add a 100, we assume that a set that has added
# smaller coins will already have tried all possibilities below
# 100, ie that 2 shouldn't add a 1 because 1 will already add 2.
def solve():
    add_1(0,0,0,0,0,0,0,0,200)
    add_2(0,0,0,0,0,0,0,0,200)
    add_5(0,0,0,0,0,0,0,0,200)
    add_10(0,0,0,0,0,0,0,0,200)
    add_20(0,0,0,0,0,0,0,0,200)
    add_50(0,0,0,0,0,0,0,0,200)
    add_100(0,0,0,0,0,0,0,0,200)
    add_200(0,0,0,0,0,0,0,0,200)


def add_1(n1,n2,n5,n10,n20,n50,n100,n200,target):
    if not target:
        solutions.append([n1,n2,n5,n10,n20,n50,n100,n200])
    elif target < 0:
        return
    else:
        add_1(n1+1,n2,n5,n10,n20,n50,n100,n200,target-1)
        add_2(n1+1,n2,n5,n10,n20,n50,n100,n200,target-1)
        add_5(n1+1,n2,n5,n10,n20,n50,n100,n200,target-1)
        add_10(n1+1,n2,n5,n10,n20,n50,n100,n200,target-1)
        add_20(n1+1,n2,n5,n10,n20,n50,n100,n200,target-1)
        add_50(n1+1,n2,n5,n10,n20,n50,n100,n200,target-1)
        add_100(n1+1,n2,n5,n10,n20,n50,n100,n200,target-1)

def add_2(n1,n2,n5,n10,n20,n50,n100,n200,target):
    if not target:
        solutions.append([n1,n2,n5,n10,n20,n50,n100,n200])
    elif target < 2:
        return
    else:
        add_2(n1,n2+1,n5,n10,n20,n50,n100,n200,target-2)
        add_5(n1,n2+1,n5,n10,n20,n50,n100,n200,target-2)
        add_10(n1,n2+1,n5,n10,n20,n50,n100,n200,target-2)
        add_20(n1,n2+1,n5,n10,n20,n50,n100,n200,target-2)
        add_50(n1,n2+1,n5,n10,n20,n50,n100,n200,target-2)
        add_100(n1,n2+1,n5,n10,n20,n50,n100,n200,target-2)

def add_5(n1,n2,n5,n10,n20,n50,n100,n200,target):
    if not target:
        solutions.append([n1,n2,n5,n10,n20,n50,n100,n200])
    elif target < 5:
        return
    else:
        add_5(n1,n2,n5+1,n10,n20,n50,n100,n200,target-5)
        add_10(n1,n2,n5+1,n10,n20,n50,n100,n200,target-5)
        add_20(n1,n2,n5+1,n10,n20,n50,n100,n200,target-5)
        add_50(n1,n2,n5+1,n10,n20,n50,n100,n200,target-5)
        add_100(n1,n2,n5+1,n10,n20,n50,n100,n200,target-5)

def add_10(n1,n2,n5,n10,n20,n50,n100,n200,target):
    if not target:
        solutions.append([n1,n2,n5,n10,n20,n50,n100,n200])
    elif target < 10:
        return
    else:
        add_10(n1,n2,n5,n10+1,n20,n50,n100,n200,target-10)
        add_20(n1,n2,n5,n10+1,n20,n50,n100,n200,target-10)
        add_50(n1,n2,n5,n10+1,n20,n50,n100,n200,target-10)
        add_100(n1,n2,n5,n10+1,n20,n50,n100,n200,target-10)

def add_20(n1,n2,n5,n10,n20,n50,n100,n200,target):
    if not target:
        solutions.append([n1,n2,n5,n10,n20,n50,n100,n200])
    elif target < 20:
        return
    else:
        add_20(n1,n2,n5,n10,n20+1,n50,n100,n200,target-20)
        add_50(n1,n2,n5,n10,n20+1,n50,n100,n200,target-20)
        add_100(n1,n2,n5,n10,n20+1,n50,n100,n200,target-20)

def add_50(n1,n2,n5,n10,n20,n50,n100,n200,target):
    if not target:
        solutions.append([n1,n2,n5,n10,n20,n50,n100,n200])
    elif target < 50:
        return
    else:
        add_50(n1,n2,n5,n10,n20,n50+1,n100,n200,target-50)
        add_100(n1,n2,n5,n10,n20,n50+1,n100,n200,target-50)

def add_100(n1,n2,n5,n10,n20,n50,n100,n200,target):
    if not target:
        solutions.append([n1,n2,n5,n10,n20,n50,n100,n200])
    elif target < 100:
        return
    else:
        add_100(n1,n2,n5,n10,n20,n50,n100+1,n200,target-100)

def add_200(n1,n2,n5,n10,n20,n50,n100,n200,target):
    if target == 200:
        solutions.append([n1,n2,n5,n10,n20,n50,n100,n200+1])


solve()
solutions = set(tuple(x) for x in solutions)
print(len(solutions))
