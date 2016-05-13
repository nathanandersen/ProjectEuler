# Problem 79
# passcode derivation

def shortestCommonSeq(s1,s2):
    scs = [[0 for i in range(len(s1))] for j in range(len(s2))]
    for i in range(len(s1)):
        scs[0][i] = s1
    for j in range(len(s2)):
        scs[j][0] = s2

    for k in range(1,len(s1)+len(s2)):
        for i in range(1,k):
            j = k-i
            pass
        
    return scs[len(s2)-1][len(s1)-1]

logins = []
with open("p079_keylog.txt","r") as f:
    for segment in f:
        logins.append(segment.strip())

#print(logins)
# endgame, can probably do this insertion and processing
# as I read the file directly.
passcode = []
sequence = ""
for login in logins:
    pass
print(shortestCommonSeq("hello","hi"))
