# Problem 79
# passcode derivation

#real	0m0.045s
#user	0m0.027s
#sys	0m0.010s

sequences = []
with open("p079_keylog.txt","r") as f:
    for segment in f:
        sequences.append(str(segment.strip()))

digits = set()
for s in sequences:
    for c in s:
        digits.add(int(c))

# Put all the digits in every position
seq = [[d for d in digits] for n in range(11)]

def try_to_remove(ele,seq):
    # catch ValueErrors in Remove
    try:
        seq.remove(ele)
    except ValueError:
        pass

def add_rules_for_first_value(a,b,c):
    # Remove all b and c before
    # first value of a
    should_remove = True
    num_occurrences = 0
    index = 0
    for i in range(len(seq)):
        if should_remove:
            try_to_remove(b,seq[i])
            try_to_remove(c,seq[i])
        if a in seq[i]:
            should_remove = False
            num_occurrences += 1
            index = i

    # If a is only present in 1 spot,
    # remove everything else at that spot.
    if num_occurrences is 1:
        seq[index] = [a]

def add_rules_for_second_value(a,b,c):
    num_occurrences = 0
    index = 0

    for i in range(len(seq)):
        try_to_remove(c,seq[i])
        if b in seq[i]:
            break
    # Remove all a after LAST b
    for k in reversed(range(len(seq))):
        try_to_remove(a,seq[i])
        if b in seq[i]:
            break

    for i in range(len(seq)):
        if b in seq[i]:
            num_occurrences += 1
            index = i

    if num_occurrences is 1:
        seq[index] = [b]


def add_rules_for_third_value(a,b,c):
    # Remove all a and b after last
    # value of c
    should_remove = True
    num_occurrences = 0
    index = 0
    for i in reversed(range(len(seq))):
        if should_remove:
            try_to_remove(a,seq[i])
            try_to_remove(b,seq[i])
        if c in seq[i]:
            should_remove = False
            num_occurrences += 1
            index = i
    if num_occurrences is 1:
        seq[index] = [c]



def add_rules_for_seq(a,b,c):
    add_rules_for_first_value(a,b,c)
    add_rules_for_second_value(a,b,c)
    add_rules_for_third_value(a,b,c)


for (a,b,c) in sequences:
    add_rules_for_seq(int(a),int(b),int(c))

code_str = ""
for s in seq:
    if s != []:
        code_str += str(s[0])

print(code_str)
