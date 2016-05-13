# Problem 89

# real 0m0.066s
# user 0m0.046s
# sys  0m0.012s

from utils import roman_numeral
from utils import roman_to_int

numerals = []
with open("p089_roman.txt","r") as f:
    for r_num in f:
        numerals.append(r_num.strip())

total = 0
for n in numerals:
    total += len(n) - len(roman_numeral(roman_to_int(n)))
print(total)
