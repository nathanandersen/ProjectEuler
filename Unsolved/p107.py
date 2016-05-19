# Problem 107


edges = []
for line in open("p107_network.txt"):
#    line = line.replace("-","-1")
    line = line.replace("-","None")
    l = eval("[" + line + "]")
    edges.append(l)

#print(edges)
# Now, we have "edges", an adjacency matrix graph representation.

# Now we just build an MST

