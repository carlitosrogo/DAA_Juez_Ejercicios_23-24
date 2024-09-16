def bestNode(distancias, visited):
    minNode = None
    minDistance = float('inf')
    for i in range(len(distancias)):
        if not visited[i] and distancias[i] < minDistance:
            minNode = i
            minDistance = distancias[i]
    return minNode

def dijkstra (g, origen):
    distancias = [float('inf')] * len(g)
    visited = [False] * len(g)

    visited[origen] = True
    distancias[origen] = 0

    for nOrigen, nDestino, longitud in g[origen]:
        distancias[nDestino] = longitud
    for _ in range(len(g) -1):
        nextNode = bestNode(distancias,visited)
        visited[nextNode] = True
        for adjOrigen, adjDestino, distance in g[nextNode]:
            distancias[adjDestino] = min(distancias[nextNode] + distance, distancias[adjDestino])
    return  distancias

def visitAllNodes(g, tipoActividad):
    totalActividades = [float('inf')] * len(set(tipoActividad))

    for i in range(len(g)):
        bestLogitud = float('inf')
        if g[i]:
            distancias = dijkstra(g, i)
            for j in range(len(g)):
                if tipoActividad[i] == tipoActividad[j] and j != i and distancias[j] < bestLogitud:
                    bestLogitud = distancias[j]
            if bestLogitud < totalActividades[tipoActividad[i]]:
                totalActividades[tipoActividad[i]] = bestLogitud
    print(*totalActividades)

numActividades, numConexiones = map(int, input().strip().split())
adjList = [[] for _ in range(numActividades)]
tipoActividad = list(map(int,input().split()))
for i in range(numConexiones):
    c,d,l = map(int,input().strip().split())
    adjList[c].append((c,d,l))
    adjList[d].append((d,c,l))
visitAllNodes(adjList,tipoActividad)
