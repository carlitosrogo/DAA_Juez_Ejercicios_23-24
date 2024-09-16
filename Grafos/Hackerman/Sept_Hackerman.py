from collections import deque


def visit_bfs(g, visited, node, costes):
    q = deque()
    visited[node] = True
    total = 0
    q.append(node)
    while q:
        nodeAux = q.popleft()
        for nodes in range(len(g)):
            print(g[nodes], g[nodeAux], (set(g[nodes]) & set(g[nodeAux])))
            if nodeAux in g[nodes] and not (set(g[nodes]) & set(g[nodeAux])):
                total += costes[nodeAux]
                break
        for nodeAdj in g[nodeAux]:
            if not visited[nodeAdj]:
                visited[nodeAdj] = True
                q.append(nodeAdj)
    return total



def ord_bfs(g, costes):
    visited = [False] * len(g)
    for node in range(len(g)):
        if not visited[node]:
            total = visit_bfs(g,visited,0, costes)
            print(total)


nNodos, nConexiones = map(int, input().strip().split())
costesNodos = []
for _ in range(nNodos):
    costesNodos.append(int(input().strip()))
print(costesNodos)
listaNodos = [[] for i in range(nNodos)]
for i in range(nConexiones):
    nodo1, nodo2 = map(int, input().strip().split())
    listaNodos[nodo1].append(nodo2)
    listaNodos[nodo2].append(nodo1)
ord_bfs(listaNodos, costesNodos)