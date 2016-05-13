# Problem 206
import math
import sys
from utils import is_square_num
from itertools import product
from utils import digital_root

def make_num(d):
    # must end in 0
    return int( '1' + d[0] + '2' + d[1] + '3' + d[2] +
                '4' + d[3] + '5' + d[4] + '6' + d[5] +
                '7' + d[6] + '8' + d[7] + '900')

print(digital_root(65536))

#digits = ['0','1','2','3','4','5','6','7','8','9']
#digit_prod = product(digits,repeat=8)
#for d in digit_prod:
#    num = make_num(d)
#    print(num)
#    if is_square_num(num):
#        print(num,math.sqrt(num))
#        sys.exit()


# 1 4 9 6 5 6 9 4 1 0 (9's digit pattern)

# 6 7 1 6 4 4 5 9 4 2 2 3 7 2 0 0 1 5 0 8 8 9 3 8 6 (8's digit pattern)
# uh oh did i miss half the 9's?
nine = [0,1,4]
bottom = int(math.sqrt(1020304050607080900)) + 20 + 100*19
top =  int(math.sqrt(1929394959697989990))
for i in range(bottom,top,100*25):
    # has to end in 900
    for n in nine:
        sqr = (i + 100*n) ** 2
        print(i,str(sqr)[len(str(sqr))-5:len(str(sqr))-4])
        if str(sqr)[::2] == "1234567890":
            print(i,sqr)
            sys.exit()
