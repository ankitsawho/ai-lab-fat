from BN import *

nnode = int(input("No. of nodes : "))
nedge = int(input("No. of edges : "))
nquery = int(input("No. of queries : "))

edges = []
for line in range(nedge):
    edge = input().rstrip().split(" ")
    edges += [edge]

print("Queries")
queries = []
for line in range(nquery):
    query = input().rstrip().split(" ")
    (start, end, observed) = (query[0], query[1], query[3:])
    queries += [(start, end, observed)]

myBN = BN()
for edge in edges:
    myBN.add_edge(edge)
for (start, end, observed) in queries:
    print(myBN.is_dsep(start, end, observed))
