# Problem 79
# passcode derivation

# TODO:
# Implement a shortest common subsequence algorithm.


def shortestCommonSeq(s1,s2):
    pass

sequence = ""

with open("p079_keylog.txt","r") as f:
    sequence = str(f.readline().strip())
    for segment in f:
        sequence = shortestCommonSeq(str(segment.strip()),sequence)
print(sequence)
