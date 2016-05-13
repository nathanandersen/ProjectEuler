# Problem 24

#real	0m18.330s
#user	0m17.017s
#sys	0m0.628s

import itertools

nums = [0,1,2,3,4,5,6,7,8,9]

perms = list(itertools.permutations(nums))
strs = []
for value_list in perms:
    strs.append(str(''.join(str(v) for v in value_list)))
print(strs[999999])


