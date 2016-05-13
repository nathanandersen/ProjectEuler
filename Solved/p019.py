# Problem 19

# real 0m0.119s
# user 0m0.037s
# sys  0m0.012s

import datetime


sum = 0
for year in range(1901,2001):
    for month in range(1,13):
        if datetime.date(year,month,1).strftime("%A") == "Sunday":
            sum += 1
print(sum)


