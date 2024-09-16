def ordenarCandidatos(g):
    candidatos = []
    for nodos in g:
        for nodoOrg, nodoDest, peso in nodos:
            candidatos.append((peso, nodoOrg, nodoDest))
    candidatos.sort()
    return candidatos


def actualizarComponentes(componentes, ini, fin):
    for i in range(1, len(componentes)):
        print(componentes, "i:", i, "fin:", fin)
        if componentes[i] == fin:
            componentes[i] = ini
            print(componentes, "ini:", ini)


def kruskal(g):
    candidatos = ordenarCandidatos(g)
    componentes = list(range(len(g)))
    contador = len(componentes) - 1
    sol = 0

    i = 0
    while contador > 1 and len(candidatos) > i:
        (peso, ini, fin) = candidatos[i]
        if componentes[ini] != componentes[fin]:
            sol += peso
            contador -= 1
            actualizarComponentes(componentes, componentes[ini], componentes[fin])
        i += 1
    return sol


nHabitaciones, nPuertas, tiempoMax = map(int, input().strip().split())
listaHabitaciones = [[] for _ in range(nHabitaciones)]
for _ in range(nPuertas):
    nodo1, nodo2, peso = map(int, input().strip().split())
    listaHabitaciones[nodo1].append((nodo1, nodo2, peso))
    listaHabitaciones[nodo2].append((nodo2, nodo1, peso))
sol = kruskal(listaHabitaciones)
if tiempoMax >= sol:
    print(sol)
else:
    print("Aleg, ¡a decorar!")
