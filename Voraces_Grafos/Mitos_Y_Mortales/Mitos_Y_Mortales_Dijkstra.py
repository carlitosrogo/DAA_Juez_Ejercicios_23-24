import math


def bestNodeSort(distances, visited):
    minDist = float('inf')
    minNode = None
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            minNode = i
    return minNode, minDist


def dijkstra(g, origin):
    distances = [float('inf')] * len(g)
    visited = [False] * len(g)

    visited[origin] = True
    distances[origin] = 0

    for adjNode, dist in g[origin]:
        distances[adjNode] = dist
    for _ in range(len(g) -1):
        nextNode, nextMetros = bestNodeSort(distances, visited)
        if nextMetros < float('inf'):
            visited[nextNode] = True
        for adjNode, dist in g[nextNode]:
            if not visited[adjNode]:
                distances[adjNode] = min(distances[adjNode], dist)
    print(math.ceil((sum(distances)/5)))


numEnemigos, numConexiones = map(int, input().strip().split())
adjList = [[] for i in range(numEnemigos)]
for _ in range(numConexiones):
    n1, n2, dist = map(int, input().strip().split())
    adjList[n1].append((n2, dist))
    adjList[n2].append((n1, dist))
dijkstra(adjList, 0)
