# Problem 92
global nums89
nums89 = {89}
global nums1
nums1 = {1}

# This is ok and correct, but slow.

def next_sq_digit_num(n):
    return sum(int(d)**2 for d in str(n))

def add_to_c89(chain):
    for c in chain:
        nums89.add(c)

def add_to_c1(chain):
    for c in chain:
        nums1.add(c)

def find_chain(i):
    chain = []
    while(1):
        if i in nums89:
            add_to_c89(chain)
            return 1
        elif i in nums1:
            add_to_c1(chain)
            return 0
        else:
            chain.append(i)
            i = next_sq_digit_num(i)

for i in range(1,10000000):
    print(i)
    find_chain(i)
print(len(nums89))
