
def ordenarListaValores(l, g):
    newList = []
    for i in range(len(g)):
        for x,y in g[i]:
            newList.append(((abs(l[x][0] - l[y][0]) + abs(l[x][1] - l[y][1])),x,y))
    newList.sort()
    return newList

def updateNodos(nodosPosibles, nodoX, nodoY):
    for i in range(len(nodosPosibles)):
        if nodosPosibles[i] == nodoY:
            nodosPosibles[i] = nodoX


def kruskal(valoresList, g):
    candidatos = ordenarListaValores(valoresList, g)
    nodosPosibles = list(range(len(g)))
    contador = len(g)
    i = 0
    totalRed = 0
    listOrden = []
    while contador > 1 and i < len(candidatos):
        peso, nodoX, nodoY = candidatos[i]
        if nodosPosibles[nodoX] != nodosPosibles[nodoY]:
            updateNodos(nodosPosibles, nodosPosibles[nodoX], nodosPosibles[nodoY])
            contador -= 1
            totalRed += peso
            listOrden.append((nodoX,nodoY))
        i += 1
    return totalRed, listOrden

nBrawlers, nConexiones = map(int, input().strip().split())
valoresList = [[] for i in range(nBrawlers)]
for i in range(nBrawlers):
    x, y = map(int, input().strip().split())
    valoresList[i].append(x)
    valoresList[i].append(y)
adjList = [[] for i in range(nBrawlers)]
for _ in range(nConexiones):
    node1, node2 = map(int, input().strip().split())
    adjList[node1].append((node1, node2))
    adjList[node2].append((node2, node1))


total, lista = kruskal(valoresList, adjList)
print(total)
for tupla in lista:
    print(*tupla)
