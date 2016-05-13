# Problem 19
# How many Sundays were there in the first month (January)
# between 1 Jan 1901 and 31 Dec 2000?

# 1 Jan 1900 = Monday

import datetime


sum = 0
for year in range(1901,2001):
    for month in range(1,13):
        if datetime.date(year,month,1).strftime("%A") == "Sunday":
            sum += 1
print(sum)


