# Problem 107
import networkx as nx

#real	0m0.342s
#user	0m0.265s
#sys	0m0.060s

edges = []
for line in open("p107_network.txt"):
    line = line.replace("-","None")
    l = eval("[" + line + "]")
    edges.append(l)

G = nx.Graph()

G.add_nodes_from(range(40))

total_cost = 0
for u in range(40):
    for v in range(40):
        e = edges[u][v]
        if e is not None:
            total_cost += e
            G.add_weighted_edges_from([(u,v,e)])


# Taken from CMU, modified slightly.
#=======================================================================
# Union-Find
#=======================================================================

class ArrayUnionFind:
    """Holds the three "arrays" for union find"""
    def __init__(self, S):
        self.group = dict((s,s) for s in S) # group[s] = id of its set
        self.size = dict((s,1) for s in S) # size[s] = size of set s
        self.items = dict((s,[s]) for s in S) # item[s] = list of items in set s
        
def make_union_find(S):
    """Create a union-find data structure"""
    return ArrayUnionFind(S)
    
def find(UF, s):
    """Return the id for the group containing s"""
    return UF.group[s]

def union(UF, a,b):
    """Union the two sets a and b"""
    assert a in UF.items and b in UF.items
    # make a be the smaller set
    if UF.size[a] > UF.size[b]:
        a,b = b,a
    # put the items in a into the larger set b
    for s in UF.items[a]:
        UF.group[s] = b
        UF.items[b].append(s)
    # the new size of b is increased by the size of a
    UF.size[b] += UF.size[a]
    # remove the set a (to save memory)
    del UF.size[a]
    del UF.items[a]

#=======================================================================
# Kruskal MST
#=======================================================================

def kruskal_mst(G):
    """Return a minimum spanning tree using kruskal's algorithm"""
    # sort the list of edges in G by their length
    Edges = []
    for u,v in G.edges_iter():
        Edges.append((u,v,G[u][v]['weight']))
    Edges.sort(key=lambda x: x[2])

    UF = make_union_find(G.nodes())  # union-find data structure

    # for edges in increasing weight
    mst = [] # list of edges in the mst
    for u,v,d in Edges:
        setu = find(UF, u)
        setv = find(UF, v)
        # if u,v are in different components
        if setu != setv:
            mst.append((u,v))
            union(UF, setu, setv)
    return mst

mst = kruskal_mst(G)
total = 0
for e in mst:
    total += G[e[0]][e[1]]['weight']

print(total_cost,total,total_cost-total)

