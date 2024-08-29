import defaultdict
from collections import defaultdict
def dfs(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited, path)
    
    return path
graph=defaultdict(list)
n,e=map(int,input().split())from collections import defaultdict

def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph, neighbour,
                visited, path)
    return path

graph = defaultdict(list)
n, e = map(int, input("Enter the number of nodes and edges: ").split())

for i in range(e):
    u, v = input(f"Enter edge {i+1} (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)  # If the graph is undirected; remove this line for a directed graph

if '0' in graph:
    start = '0'
else:
    start = 'A'
# Starting node
visited = defaultdict(bool)
path = []

traversed_path = dfs(graph, start, visited, path)
print("DFS Traversal Path:", traversed_path)
for i in range(e):
   #type ur code here
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)
#print(graph)
start='A'
visited=defaultdict(bool)
path=[]

traversedpath=dfs(graph,start,visited,path)
print(traversedpath)
