
def bestNode(esfuerzo, visited):
    node = None
    minEsfuerzo = float('inf')
    for i in range(len(esfuerzo)):
        if not visited[i] and esfuerzo[i] < minEsfuerzo:
            minEsfuerzo = esfuerzo[i]
            node = i
    return node, minEsfuerzo

def dijkstra(g):
    esfuerzo = [float('inf')] * len(g)
    visited = [False] * len(g)

    #Empezamos en el 0
    visited[0] = True
    esfuerzo[0] = 0

    for node, esfuerzoHecho in g[0]:
        esfuerzo[node] = esfuerzoHecho
    for _ in range(len(g) - 1):
        minNode, esfuerzoRealizado = bestNode(esfuerzo, visited)
        if esfuerzoRealizado > float('inf'):
            visited[minNode] = True
        for adj, adjEsfuerzo in g[minNode]:
            if not visited[adj]:
                esfuerzo[adj] = min(esfuerzo[adj], adjEsfuerzo)

    for i in range(len(esfuerzo)):
        print("C{} -> ".format(i), esfuerzo[i])
    print("Esfuerzo realizado ->", sum(esfuerzo))


numConsursantes, numRelaciones = map(int, input().strip().split())
adjList = [[] for i in range(numConsursantes)]
for _ in range(numRelaciones):
    Ci,Cj,E = map(int, input().strip().split())
    adjList[Ci].append((Cj,E))
    adjList[Cj].append((Ci,E))
print(adjList)
dijkstra(adjList)