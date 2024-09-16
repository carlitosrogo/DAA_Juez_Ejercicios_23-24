import math


def ordenarLista(g):
    nuevaLista = []
    for nodo in g:
        for ini, fin, peso, in nodo:
            nuevaLista.append((peso, ini, fin))
    nuevaLista.sort()
    return nuevaLista


def actualizarComponentes(componentes, ini, fin):
    for i in range(len(componentes)):
        if componentes[i] == fin:
            componentes[i] = ini


def kruskal(g):
    listaOrdenada = ordenarLista(g)
    componentes = list(range(len(g)))
    contador = len(componentes) - 1
    sol = 0
    i = 0

    while contador > 0 and i < len(listaOrdenada):
        (peso, ini, fin) = listaOrdenada[i]
        if componentes[ini] != componentes[fin]:
            sol += peso
            actualizarComponentes(componentes, componentes[ini], componentes[fin])
            contador -= 1
        i += 1
    print(componentes)
    print(math.ceil(sol/5))


nEnemigos, nConexiones = map(int, input().strip().split())
listaEnemigos = [[] for _ in range(nEnemigos)]
for _ in range(nConexiones):
    nodoOrg, nodoDest, peso = map(int, input().strip().split())
    listaEnemigos[nodoOrg].append((nodoOrg, nodoDest, peso))
    # listaEnemigos[nodoDest].append((nodoDest, nodoOrg, peso))
kruskal(listaEnemigos)
