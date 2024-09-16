
def nextNodeSort(dist,v):
    minDist = float('inf')
    bestNode = 0
    for i in range(1, len(dist)):
        if dist[i] < minDist and not v[i]:
            minDist = dist[i]
            bestNode = i
    return bestNode

def dijkstra(g,origin, timeToOrdenate):
    distances = [float('inf')] * len(g)
    visited = [False] * len(g)

    visited[origin] = True #Siempre empezamos por el nodo 0
    distances[origin] = 0

    for adjNode, time in g[origin]:
        distances[adjNode] = time
    for _ in range(2, len(g)):
        bestNode = nextNodeSort(distances,visited)
        visited[bestNode] = True
        for adjNode, time in g[bestNode]:
            distances[adjNode] = min(distances[bestNode] + time, distances[adjNode])
    isConexo = True
    for i in range(len(distances)):
        if distances[i] == float('inf'):
            isConexo = False
            break
    sol = 0
    if isConexo:
        for i in range(len(distances)):
            sol += distances[i]
        if sol > timeToOrdenate:
            print("Aleg, ¡adecorar!")
        else:
            print(sol)
    else:
        print("Aleg, ¡adecorar!")


numRooms, numDoors, maxTime = map(int, input().strip().split())
adjList = [[] for _ in range(numRooms)]
for _ in range(numDoors):
    h1,h2,d = map(int, input().strip().split())
    adjList[h1].append((h2,d))

dijkstra(adjList, 0, maxTime)
