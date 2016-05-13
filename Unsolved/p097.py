# Problem 97

#m = (28433 * (2 ** 7830457)) + 1
def find_pattern_start_len(seq):
    l = len(seq)
    for i in range(2,int(l/2)):
        if (seq[0:i] == seq[i:2*i]):
            return (seq[0:i],i)
    return ([0],0)

lastd = []
secd = []
threed = []
fourd = []
fived = []
sixd = []
sevend = []
eightd = []
nined = []
tend = []
for i in range(20,50000):
    print(i)
    m = str(28433 * (2 ** i) + 1)
    l = len(m)
    lastd.append(m[l-1:l])
    secd.append(m[l-2:l-1])
    threed.append(m[l-3:l-2])
    fourd.append(m[l-4:l-3])
    fived.append(m[l-5:l-4])
    sixd.append(m[l-6:l-5])
    sevend.append(m[l-7:l-6])
    eightd.append(m[l-8:l-7])
    nined.append(m[l-9:l-8])
    tend.append(m[l-10:l-9])
#    print(l,m[l-10:l])


one = find_pattern_start_len(lastd)[1]
#print(one)
two = find_pattern_start_len(secd)[1]
three = find_pattern_start_len(threed)[1]
four = find_pattern_start_len(fourd)[1]
five = find_pattern_start_len(fived)[1]
six = find_pattern_start_len(sixd)[1]
seven = find_pattern_start_len(sevend)[1]
eight = find_pattern_start_len(eightd)[1]
nine = find_pattern_start_len(nined)[1]
ten = find_pattern_start_len(tend)[1]
print(one,two,three,four,five,six,seven,eight,nine,ten)
#print(lastd)
#print(m)
#print(str(m)[2357196])
