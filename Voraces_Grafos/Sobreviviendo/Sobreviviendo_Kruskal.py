def sortConcursantes(g):
    consursantesSoreted = []
    for node in g:
        for origen, destino, costed in node:
            consursantesSoreted.append((costed, origen, destino))
    consursantesSoreted.sort()
    return consursantesSoreted


def updateConcursantes(concursantes, nodeOrigen, nodeDestino):
    for i in range(len(concursantes)):
        if concursantes[i] == nodeDestino:
            concursantes[i] = nodeOrigen


def kruskal(g):
    consursantesList = sortConcursantes(g)
    concursantes = list(range(len(g)))

    esfuerzoIndividual = [0] * len(g)
    esfuerzoTotal = 0
    count = len(g)
    i = 0
    while count > 0 and len(consursantesList) > i:
        esfuerzo, origen, destino = consursantesList[i]
        if concursantes[origen] != concursantes[destino]:
            count -= 1
            esfuerzoTotal += esfuerzo
            esfuerzoIndividual[origen] += esfuerzo
            esfuerzoIndividual[destino] += esfuerzo
            updateConcursantes(concursantes, concursantes[origen], concursantes[destino])
        i += 1

    for i in range(len(esfuerzoIndividual)):
        print('C{} -> '.format(i), esfuerzoIndividual[i])
    print("Esfuerzo realizado ->", esfuerzoTotal)


numConsursantes, numRelaciones = map(int, input().strip().split())
adjList = [[] for i in range(numConsursantes)]
for _ in range(numRelaciones):
    Ci, Cj, E = map(int, input().strip().split())
    adjList[Ci].append((Ci, Cj, E))
    adjList[Cj].append((Cj, Ci, E))
kruskal(adjList)
