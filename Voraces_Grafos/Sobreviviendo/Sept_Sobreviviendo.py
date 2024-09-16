def obtenerMejorNodo(distancia, visitado):
    distanciaMin = float('inf')
    mejorNodo = 0
    for nodo in range(1, len(distancia)):
        if not visitado[nodo] and distancia[nodo] < distanciaMin:
            distanciaMin = distancia[nodo]
            mejorNodo = nodo
    return mejorNodo


def dijkstra(g, origen):
    distancia = [float('inf')] * len(g)
    visitado = [False] * len(g)

    distancia[origen] = 0
    visitado[origen] = True

    for ini, fin, peso in g[origen]:
        distancia[fin] = peso
    for _ in range(2, len(g)):
        mejorNodo = obtenerMejorNodo(distancia, visitado)
        visitado[mejorNodo] = True
        for ini, fin, peso in g[mejorNodo]:
            distancia[fin] = min(distancia[fin], distancia[ini] + peso)
    for i in range(len(distancia)):
        print("C{} ->".format(i), distancia[i])
    print("Esfuerzo realizado ->", sum(distancia))


nConcursantes, nRelaciones = map(int, input().strip().split())
listaConcursantes = [[] for _ in range(nConcursantes)]
for _ in range(nRelaciones):
    nodo1, nodo2, peso = map(int, input().strip().split())
    listaConcursantes[nodo1].append((nodo1, nodo2, peso))
    listaConcursantes[nodo2].append((nodo2, nodo1, peso))
dijkstra(listaConcursantes, 0)
