import copy

def obtenerMejorFamoso(listaNombres, listaAmabilidad, listaFama, famosoActual, entrevistados):
    if listaNombres[famosoActual] in entrevistados:
        for famosoNuevo in range(len(listaNombres)):
            if listaNombres[famosoNuevo] not in entrevistados:
                famosoActual = famosoNuevo
                break
    mejorFamoso = famosoActual
    for candidato in range(len(listaNombres)):
        if listaNombres[candidato] not in entrevistados and candidato != famosoActual:
            if listaAmabilidad[candidato] / listaFama[candidato] < listaAmabilidad[mejorFamoso] / listaFama[mejorFamoso]:
                mejorFamoso = candidato
    return mejorFamoso
def greedy(listaNombres, listaAmabilidad,listaFama,listaTiempo):
    entrevistados = set()
    famosoActual = 0
    listaNombresAux = copy.deepcopy(listaNombres)
    listaNombresAux.sort()
    totalTiempo = 0
    while len(listaNombres) != len(entrevistados):
        mejorFamoso = obtenerMejorFamoso(listaNombres,listaAmabilidad,listaFama, famosoActual, entrevistados)
        famosoActual = mejorFamoso
        entrevistados.add(listaNombres[mejorFamoso])
        if listaNombres[mejorFamoso] != listaNombresAux[0] and listaNombresAux[0] not in entrevistados:
            totalTiempo += listaTiempo[mejorFamoso]
        print(listaNombres[mejorFamoso])
    print(totalTiempo)
nFamosos = int(input().strip())
listaNombres = []
listaAmabilidad = []
listaFama = []
listaTiempo = []
for _ in range(nFamosos):
    entrada = input().strip().split()
    listaNombres.append(entrada[0])
    amabilidad, fama, tiempo = map(int, entrada[1:])
    listaAmabilidad.append(amabilidad)
    listaFama.append(fama)
    listaTiempo.append(tiempo)
greedy(listaNombres, listaAmabilidad, listaFama, listaTiempo)