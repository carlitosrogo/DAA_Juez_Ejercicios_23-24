def dfs(v, g, visited):
    visited.add(v)
    for adj in g[v]:
        if adj not in visited:
            dfs(adj, g, visited)


def getTranspose(g, numCitys):
    gT = [[] for _ in range(numCitys)]
    for u in range(numCitys):
        for v in g[u]:
            gT[v].append(u)
    return gT


def isStronglyConnected(g, numCitys):
    # Check from the initial node (e.g., node 0)
    visited = set()
    dfs(0, g, visited)
    if len(visited) != numCitys:
        return False

    # Get the transpose of the graph
    gT = getTranspose(g, numCitys)

    # Check from the initial node in the transposed graph
    visited = set()
    dfs(0, gT, visited)
    if len(visited) != numCitys:
        return False

    return True


numCitys, numConnections = map(int, input().strip().split())
adjList = [[] for _ in range(numCitys)]
for i in range(numConnections):
    u, v = map(int, input().strip().split())
    adjList[u].append(v)

if isStronglyConnected(adjList, numCitys):
    print("PERFECTO")
else:
    print("CAMBIA EL ITINERARIO")
