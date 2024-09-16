def obtenerNodoMin(distancias, visitados):
    distanciaMin = float('inf')
    mejorNodo = 0
    for nodo in range(1, len(distancias)):
        if not visitados[nodo] and distancias[nodo] < distanciaMin:
            distanciaMin = distancias[nodo]
            mejorNodo = nodo
    return mejorNodo


def dijkstra(g, origen, destino):
    n = len(g) - 1
    distancias = [float('inf')] * (n + 1)  # len(g)
    visitados = [False] * (n + 1)  # len(g)
    predecesor = [-1] * len(g)

    distancias[origen] = 0
    visitados[origen] = True

    for ini, fin, peso in g[origen]:
        distancias[fin] = peso
        print("Asigno los adyacentes del nodo origen: ", ini, "nodo destino: ", fin, "peso: ", peso)
        predecesor[fin] = ini
    print("Bucle voraz")
    for _ in range(2, len(g)):
        siguienteNodo = obtenerNodoMin(distancias, visitados)
        print("Obtengo el siguiente mejor nodo:", siguienteNodo)
        visitados[siguienteNodo] = True
        for ini, fin, peso in g[siguienteNodo]:
            if ((distancias[ini] + peso) < distancias[fin]):
                predecesor[fin] = ini
            distancias[fin] = min(distancias[ini] + peso, distancias[fin])
            print("Asigno la distancia a los adyacentes del mejor nodo encontrado: ", ini, "nodo destino: ", fin,
                  "peso: ", peso)

    recorrido = []
    actual = destino
    while actual != -1:
        recorrido.append(actual)
        actual = predecesor[actual]
    recorrido.reverse()
    print(distancias[destino])
    for i in range(len(recorrido)):
        print(recorrido[i], end=' ')


nCamas, nConexiones = map(int, input().strip().split())
listaCamas = [[] for _ in range(nCamas)]
for _ in range(nConexiones):
    nodoOrg, nodoDes, peso = map(int, input().strip().split())
    listaCamas[nodoOrg].append((nodoOrg, nodoDes, peso))
    listaCamas[nodoDes].append((nodoDes, nodoOrg, peso))
origen, destino = map(int, input().strip().split())
print(listaCamas)
dijkstra(listaCamas, origen, destino)
