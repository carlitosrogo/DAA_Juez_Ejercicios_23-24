import math


def getBestNode(distances, visited):
    node = None
    metros = float('inf')

    for i in range(1, len(distances)):
        if distances[i] < metros and not visited[i]:
            metros = distances[i]
            node = i

    return node, metros

def mitos(g):
    distances = [float('inf')]*len(g)
    visited = [False] * len(g)

    distances[0] = 0
    visited[0] = True
    sol = 0

    for n in g[0]:
        distances[n[1]] = n[2]


    for _ in range(len(g)-1):
        end, metros = getBestNode(distances, visited)

        if metros < float('inf'):
            sol += metros
            visited[end] = True

        for adj in g[end]:
            if not visited[adj[1]]:
                distances[adj[1]] = min(distances[adj[1]], adj[2])
    print(distances)
    print(math.ceil((sum(distances)/5)))




g = []

n, c = map(int, input().strip().split())
for _ in range(n):
    g.append([])

for _ in range(c):
    ini, fin, metros = map(int, input().strip().split())
    g[ini].append((ini, fin, metros))
    g[fin].append((fin, ini, metros))

print(g)
mitos(g)