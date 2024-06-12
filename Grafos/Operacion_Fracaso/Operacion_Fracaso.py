from collections import deque

def bfsVisit(v, g, visited, nota):
    fans = 0
    q = deque()
    visited[v] = True
    q.append((v, 1))  # Añadir el nodo y su nivel (1 para el nodo inicial)
    while q:
        aux, level = q.popleft()
        fans += 1
        if level < nota:
            for adj in g[aux]:
                if not visited[adj]:
                    visited[adj] = True
                    q.append((adj, level + 1))  # Añadir nodo con el siguiente nivel
    return fans

def bfs(g, nota):
    visited = [False] * len(g)
    totalFans = bfsVisit(0, g, visited, nota)
    print(totalFans)

numConcursantes = int(input())
for _ in range(numConcursantes):
    nota, numFans, numConexiones = map(int, input().strip().split())
    adjList = [[] for _ in range(numFans)]
    for _ in range(numConexiones):
        a, b = map(int, input().strip().split())
        adjList[a].append(b)
        adjList[b].append(a)
    bfs(adjList, nota)
