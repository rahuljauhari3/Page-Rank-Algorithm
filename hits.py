import networkx as nx
import numpy as np

web_graph=nx.read_gpickle("web_graph.gpickle")
print(web_graph)

#read all the queries
query = input('Enter your query:')
query = query.split()

arr = np.zeros(100)

for i in range(0,100) :
    document = web_graph.nodes[i]['page_content']
    temp=document.split()

    for q in query:
        if q in temp:
            arr[i]=1
            break

#create adjacency matrix arr1
adj=nx.to_numpy_array(web_graph)

arr=np.array(arr)

#Getting Hub score
hub=np.dot(arr,adj)

#Getting authority score
authority=np.dot(arr,adj.T)

#Finding which all pages involved in hub-authority relationship for the given query and are to be a part of the sub-graph
arr=arr+hub+authority

#create the baseset
connection=[]

for i in range (0,100):
    if(arr[i]!=0):
        #add i to a vector arr5
        connection.append(i)

#create a subgraph using arr5
subgraph=nx.subgraph(web_graph, connection)
result=nx.to_numpy_array(subgraph)

length = len(connection)
hubvector=np.ones(length)
authvector=np.ones(length)
hubvector=hubvector/length
authvector=authvector/length

count=0
# Setting no. of iterations
while(count<=1000):
    hubvector=np.dot(result,authvector)
    authvector=np.dot(result.T,hubvector)
    hubvector=hubvector/sum(hubvector)
    authvector=authvector/sum(authvector)
    count=count+1

result=list(subgraph.nodes)

print("\nNode\tHub Values:")
step=0
for value in hubvector:
    print(result[step],end="\t")
    print(value,end="\n")
    step=step+1

print("\nNode\tAuthority Values:")
step=0
for value in authvector:
    print(result[step],end="\t")
    print(value,end="\n")
    step=step+1
