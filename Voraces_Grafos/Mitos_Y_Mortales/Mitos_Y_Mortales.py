import math


def sortList(g):
    newList = []
    for node in g:
        for adjNode, dist in node:
            newList.append((dist, adjNode))
    newList.sort()
    return newList

def updateNodes(listaEnemigos, enemigoOrigen, enemigoDestino):
    for i in range(1, len(listaEnemigos)):
        if listaEnemigos[i] == enemigoDestino:
            listaEnemigos[i] = enemigoOrigen
def kruskal(g):
    orderList = sortList(g)
    emigosDisponibles = list(range(len(g)))
    count = len(emigosDisponibles) -1
    i = 0
    sol = 0
    while count > 1 and len(orderList) > i:
        dist, adjNode = orderList[i]
        print(orderList[i])
        print(emigosDisponibles)
        if emigosDisponibles[i] != emigosDisponibles[adjNode]:
            print(sol)
            sol += math.ceil(dist/5)
            count -= 1
            updateNodes(emigosDisponibles,emigosDisponibles[i], emigosDisponibles[adjNode])
        i += 1
    print(sol)

numEnemigos, numConexiones = map(int, input().strip().split())
adjList = [[] for i in range(numEnemigos)]
for _ in range(numConexiones):
    n1, n2, dist = map(int, input().strip().split())
    adjList[n1].append((n2, dist))
print(adjList)
kruskal(adjList)