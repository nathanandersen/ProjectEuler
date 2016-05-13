# Problem 24
import itertools

nums = [0,1,2,3,4,5,6,7,8,9]

perms = list(itertools.permutations(nums))
strs = []
for value_list in perms:
    strs.append(str(''.join(str(v) for v in value_list)))
print(strs[999999])


