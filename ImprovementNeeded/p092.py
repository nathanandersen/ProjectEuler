# Problem 92


# Slow.

#real	1m8.287s
#user	1m6.965s
#sys	0m0.787s


nums89 = set([89])
nums1 = set([1])


def next_sq_digit_num(n):
    return sum(int(d)**2 for d in str(n))

def find_chain(i):
    chain = set()
    while True:
        if i in nums89:
            nums89.update(chain)
            return True
        elif i in nums1:
            nums1.update(chain)
            return False
        else:
            chain.add(i)
            i = next_sq_digit_num(i)

for i in range(1,10000000):
    print(i)
    find_chain(i)

print(len(nums89))
