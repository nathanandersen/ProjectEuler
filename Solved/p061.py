# Problem 61

# real 0m0.092s
# user 0m0.071s
# sys  0m0.012s

from utils import is_triangular_num
from utils import is_square_num
from utils import is_pent_num
from utils import is_hex_num
from utils import is_hept_num
from utils import is_oct_num
from itertools import permutations

tri_nums = set()
sq_nums = set()
pent_nums = set()
hex_nums = set()
hept_nums = set()
oct_nums = set()

prefixes = dict()
# dictionary of xx-- to xxxx

# semi-suffix-tree
def add_to_structure(n):
    prefix = str(n)[:2]
    if prefixes.get(prefix) is None:
        prefixes[prefix] = set([n])
    else:
        prefixes[prefix].add(n)


def add_to_tri_nums(n):
    tri_nums.add(n)
    add_to_structure(n)
def add_to_sq_nums(n):
    sq_nums.add(n)
    add_to_structure(n)
def add_to_pent_nums(n):
    pent_nums.add(n)
    add_to_structure(n)
def add_to_hex_nums(n):
    hex_nums.add(n)
    add_to_structure(n)
def add_to_hept_nums(n):
    hept_nums.add(n)
    add_to_structure(n)
def add_to_oct_nums(n):
    oct_nums.add(n)
    add_to_structure(n)


# construct sets of all nums
for n in range(1000,10000):
    if is_triangular_num(n): add_to_tri_nums(n)
    if is_square_num(n): add_to_sq_nums(n)
    if is_pent_num(n): add_to_pent_nums(n)
    if is_hex_num(n): add_to_hex_nums(n)
    if is_hept_num(n): add_to_hept_nums(n)
    if is_oct_num(n): add_to_oct_nums(n)

# Want to: write a recursive function that
# returns all possible prefix-suffix completions
# for a given number.

def buildSeq(original,n,remaining):
    if remaining is 1:
        if str(n)[2:] == str(original)[:2]:
            return [[n]]
        else: return None
    else:
        comps = []
        nexts = prefixes.get(str(n)[2:])
        if nexts is None:
            return None
        else:
            for item in nexts:
                following = buildSeq(original,item,remaining-1)
                if following is not None:
                    for follower in following:
                        follower[:0] = [n]
                        comps.append(follower)
        return comps
    
def isValidSeq(seq):
    for (a,b,c,d,e,f) in permutations(seq):
        if (a in tri_nums
            and b in sq_nums
            and c in pent_nums
            and d in hex_nums
            and e in hept_nums
            and f in oct_nums):
            print(a,b,c,d,e,f)
            return True
    return False


for t in oct_nums:
    seqs = buildSeq(t,t,6)
    if seqs is None:
        continue
    else:
        for seq in seqs:
            if isValidSeq(seq):
                print(seq)
                print(sum(seq))
                exit()
