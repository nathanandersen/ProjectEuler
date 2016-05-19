# Problem 112

#real	0m9.021s
#user	0m8.967s
#sys	0m0.025s

def is_in_order(s,key):
    for n in range(1,len(s)):
        if key(s[n]) < key(s[n-1]): return False
    return True

def is_bouncy(n):
    return not(is_in_order(str(n),key= lambda c : int(c) ) or
               is_in_order(str(n),key= lambda c : -1*int(c)))


b = 1 # bouncy nums
n = 101 # nums
while True:
    n += 1
    if is_bouncy(n):
        b += 1
    if b/n == 0.99:
        print(n)
        exit()
