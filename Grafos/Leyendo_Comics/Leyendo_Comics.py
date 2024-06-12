from collections import deque


def bfsVisit(v, g, visited, finalList):
    q = deque()
    visited[v] = True
    finalList.append(v)
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                dependency = False
                for i in range(len(g)):
                    if adj in g[i] and not visited[i]:
                        dependency = True
                        break
                if not dependency:
                    finalList.append(adj)
                    visited[adj] = True
                    q.append(adj)


def bfs(g):
    visited = [False] * len(g)
    finalList = []
    for v in range(len(g)):
        if not visited[v]:
            dependency = False
            for i in range(len(g)):
                if v in g[i] and not visited[i]:
                    dependency = True
                    break
            if not dependency:
                bfsVisit(v, g, visited, finalList)
    return finalList


numComics, numConexiones = map(int, input().strip().split())
adjList = [[] for _ in range(numComics)]
for i in range(numConexiones):
    a, b = map(int, input().strip().split())
    adjList[a].append(b)

finalList = bfs(adjList)
print(finalList)
