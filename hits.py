import networkx as nx
import numpy as np

G = nx.read_gpickle('web_graph.gpickle')

print(G)

# read all the queries
query = input('Enter your query:')
query = query.split()

authority_matrix = np.zeros(100)

for i in range(0, 100):
    node_index = i
    doc = G.nodes[node_index]['page_content']
    arr0 = doc.split()

# create an array arr0 for storing all values
    for q in query:
        if q in arr0:
            authority_matrix[i] = 1
            break

# create adjacency_matrix adjacency_matrix
adjacency_matrix = nx.to_numpy_array(G)
authority_matrix = np.array(authority_matrix)
# hub_matrix=authority_matrix*adjacency_matrix
hub_matrix = np.dot(authority_matrix, adjacency_matrix)
# hub_transpose=authority_matrix * (adjacency_matrix)T
hub_transpose = np.dot(authority_matrix, adjacency_matrix.T)
# arr4=authority_matrix+hub_matrix+hub_transpose
arr4 = np.add(authority_matrix, np.add(hub_matrix, hub_transpose))
# create the baseset
arr5 = []

for i in range(0, 99):
    if(arr4[i] != 0):
        # add i to a vector arr5
        arr5.append(i)

# create a subgraph using arr5
subgraph = nx.subgraph(G, arr5)
arr8 = nx.to_numpy_array(subgraph)

hubvector = np.ones(len(arr5))
authvector = np.ones(len(arr5))
hubvector = hubvector/sum(hubvector)
authvector = authvector/sum(authvector)


count = 0
while(count <= 1000):
    hubvector = np.dot(arr8, authvector)
    authvector = np.dot(arr8.T, hubvector)
    hubvector = hubvector/sum(hubvector)
    authvector = authvector/sum(authvector)
    count = count+1

arr5 = list(subgraph.nodes)

print("\nNode\tHub Values:")
index = 0
for x in hubvector:
    print(arr5[index], end="\t")
    print(x, end="\n")
    index = index+1

print("\nNode\tAuthority Values:")
index = 0
for x in authvector:
    print(arr5[index], end="\t")
    print(x, end="\n")
    index = index+1
