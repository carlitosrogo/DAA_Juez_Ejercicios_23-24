def dfsVisit(v, g, visited):
    visited.add(v)
    for adj in g[v]:
        if adj not in visited:
            dfsVisit(adj, g, visited)

def isConnected(g, numCitys):
    for start in range(numCitys):
        visited = set()
        dfsVisit(start, g, visited)
        if len(visited) != numCitys:
            return False
    return True

def dfs(g, numCitys):
    if isConnected(g, numCitys):
        return "PERFECTO"
    else:
        return "CAMBIA EL ITINERARIO"

numCitys, numConnections = map(int, input().strip().split())
adjList = [[] for _ in range(numCitys)]
for i in range(numConnections):
    u, v = map(int, input().strip().split())
    adjList[u].append(v)

text = dfs(adjList, numCitys)
print(text)
