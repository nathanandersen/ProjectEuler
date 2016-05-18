# Problem 79
# passcode derivation
#from itertools import *
import itertools
import functools

# TODO:
# Implement a shortest common subsequence algorithm.


def shortestCommonSeq(s1,s2):
    pass

seq = []

with open("p079_keylog.txt","r") as f:
    seq = [str(f.readline().strip())]
#    sequence = str(f.readline().strip())
    for segment in f:
        seq.append(str(segment.strip()))
#        sequence = shortestCommonSeq(str(segment.strip()),sequence)
print(seq)
