def minArist(distances,visited):
    arist = float('inf')
    bestNode = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < arist:
            arist = distances[i]
            bestNode = i
    return bestNode

def dijkstra(g, o, d):
    distances = [float('inf')] * len(g)
    visited = [False] * len(g)
    predecessors = [-1] * len(g)  # Arreglo para rastrear los predecesores

    distances[o] = 0
    visited[o] = True
    for node, dist in g[o]:
        distances[node] = dist
        predecessors[node] = o  # Set the predecessor of the initial connections
    for _ in range(2, len(g)):
        nextNode = minArist(distances, visited)
        visited[nextNode] = True
        for adj, weight in g[nextNode]:
            if distances[nextNode] + weight < distances[adj]:
                distances[adj] = distances[nextNode] + weight
                predecessors[adj] = nextNode  # Update the predecessor
    print(distances[d])

    # Construir el recorrido desde el destino hasta el origen
    path = []
    current = d
    while current != -1:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    for i in range(len(path)):
        print(path[i], end=' ')

numBeds, numConections = map(int, input().strip().split())
adjList = [[] for i in range(numBeds)]
for _ in range(numConections):
    c1, c2, d = map(int, input().strip().split())
    adjList[c1].append((c2, d))
    adjList[c2].append((c1, d))
origen, destino = map(int, input().strip().split())
dijkstra(adjList,origen,destino)
