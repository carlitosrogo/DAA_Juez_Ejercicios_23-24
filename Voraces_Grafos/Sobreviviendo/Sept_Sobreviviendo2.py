def ordenarLista(g):
    nuevaLista = []
    for nodo in g:
        for ini, fin, peso in nodo:
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
    esfuerzoIndividual = [0] * len(g)
    contador = len(g) - 1
    sol = 0
    i = 0

    while contador > 0 and len(listaOrdenada) > i:
        (peso, ini, fin) = listaOrdenada[i]
        if componentes[ini] != componentes[fin]:
            sol+= peso
            esfuerzoIndividual[ini] += peso
            esfuerzoIndividual[fin] += peso
            actualizarComponentes(componentes, componentes[ini], componentes[fin])
            contador += 1
        i += 1
    for i in range(len(esfuerzoIndividual)):
        print("C{} ->".format(i), esfuerzoIndividual[i])
    print("Esfuerzo realizado ->", sol)
nConcursantes, nRelaciones = map(int, input().strip().split())
listaConcursantes = [[] for _ in range(nConcursantes)]
for _ in range(nRelaciones):
    nodo1, nodo2, peso = map(int, input().strip().split())
    listaConcursantes[nodo1].append((nodo1, nodo2, peso))
    listaConcursantes[nodo2].append((nodo2, nodo1, peso))
kruskal(listaConcursantes)
