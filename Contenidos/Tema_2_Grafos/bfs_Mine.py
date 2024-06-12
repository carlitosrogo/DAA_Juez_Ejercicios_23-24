from collections import deque


def bfsPath(n,g,visited):
    q = deque()
    visited[n] = True
    q.append(n)
    while q:
        aux = q.popleft()
        for ady in g[aux]:
            if not visited[ady]:
                visited[ady] = True
                q.append(ady)




def bfs (g):
    n = len(g)
    visited = [False] * n
    for v in range(1, n):
        if not visited[v]:
            bfsPath(v,g,visited)
