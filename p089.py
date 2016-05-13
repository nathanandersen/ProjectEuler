# Problem 89
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
