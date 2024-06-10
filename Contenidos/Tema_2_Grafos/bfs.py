from collections import deque
def bfs_aux(v, g, visited):
    q = deque()
    visited[v] = True
    q.append(v)
    print(v, end = " ")
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)
                print(adj, end = " ")

def bfs(g):
    n = len(g) - 1
    visited = [False] * (n + 1)
    for v in range(1, n + 1):
        if not visited[v]:
            bfs_aux(v, g, visited)

graph_AdjList = [
    [],
    [2,4,8],
    [1,3,4],
    [2,4,5],
    [1,2,3,7],
    [3,6],
    [5,7],
    [4,6,9],
    [1,9],
    [7,8]
]

#breath first search
bfs(graph_AdjList)