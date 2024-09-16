from collections import deque

def visit_bfs(g, nodo, visited):
    q = deque()
    visited[nodo] = True
    q.append(nodo)

    while q:
        nodoAux = q.popleft()
        for nodoAdj in g[nodoAux]:
            if not visited[nodoAdj]:
                visited[nodoAdj] = True
                q.append(nodoAdj)
def ord_bfs(g):
    visited = [False] * len(g)
    for nodo in range(len(g)):
        if not visited[nodo]:
            visit_bfs(g, nodo, visited)