# Problem 26
from decimal import *
import math
from utils import repeating_cycle_len

cycle_max_index = 1000
cycle_max = 1
for d in range(1,1000):
    cycle = repeating_cycle_len(Decimal(1)/Decimal(d))
    if (cycle > cycle_max):
        cycle_max_index = d
        cycle_max = cycle

print(cycle_max_index,cycle_max)
