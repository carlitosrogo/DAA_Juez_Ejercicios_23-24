def obtenerMejorNodo(distancia, visitado):
    distanciaMin = float('inf')
    mejorNodo = 0
    for nodo in range(1, len(distancia)):
        if not visitado[nodo] and distancia[nodo] < distanciaMin:
            mejorNodo = nodo
            distanciaMin = distancia[nodo]
    return mejorNodo
def dijkstra(g, origen):
    distancia = [float('inf')] * len(g)
    visitado = [False] * len(g)

    distancia[origen] = 0
    visitado[origen] = True

    for ini, fin, peso in g[origen]:
        distancia[fin] = peso

    for _ in range(2, len(g)):
        mejorNodo = obtenerMejorNodo(distancia,visitado)
        visitado[mejorNodo] = True
        for ini, fin, peso in g[mejorNodo]:
            distancia[fin] = min(distancia[fin], distancia[ini] + peso)
    return sum(distancia)

nHabitaciones, nPuertas, tiempoMax = map(int, input().strip().split())
listaHabitaciones = [[] for _ in range(nHabitaciones)]
for _ in range(nPuertas):
    nodo1, nodo2, peso = map(int, input().strip().split())
    listaHabitaciones[nodo1].append((nodo1, nodo2, peso))
    listaHabitaciones[nodo2].append((nodo2, nodo1, peso))
sol = dijkstra(listaHabitaciones, 0)
if tiempoMax >= sol:
    print(sol)
else:
    print("Aleg, ¡a decorar!")
