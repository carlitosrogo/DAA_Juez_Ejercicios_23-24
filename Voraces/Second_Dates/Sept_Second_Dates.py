def obtenerValorMax(lNombres, lEdades, agrupados):
    participanteActual = 0
    for p in range(len(lNombres)):
        if p not in agrupados and lEdades[p] > lEdades[participanteActual]:
            participanteActual = p
    return participanteActual

def obtenerValorMin(lNombres, lEdades, agrupados):
    participanteActual = 0
    for p in range(len(lNombres)):
        if p not in agrupados and lEdades[p] < lEdades[participanteActual]:
            participanteActual = p
    return participanteActual

def greedy(lNombres, lEdades):
    agrupados = set()
    grupoMayores = []
    grupoMenores = []
    totalMayores= 0
    totalMenores = 0
    participanteMenor = obtenerValorMin(lNombres, lEdades, agrupados)
    participanteMayor = obtenerValorMax(lNombres, lEdades, agrupados)
    if participanteMenor not in agrupados:
        grupoMenores.append(lNombres[participanteMenor])
        agrupados.add(lNombres[participanteMenor])
        totalMenores += lEdades[participanteMenor]
    if participanteMayor not in agrupados:
        grupoMenores.append(lNombres[participanteMayor])
        agrupados.add(lNombres[participanteMayor])
        totalMayores += lEdades[participanteMayor]
    while len(lNombres) != len(agrupados):
        siguienteParticipante = obtenerValorMin(lNombres, lEdades, agrupados)


nParticipantes, nGrupos = map(int, input().strip().split())
listaNombres = []
listaEdades = []
for i in range(nParticipantes):
    entrada = input().strip().split()
    listaNombres.append(entrada[0])
    listaEdades.append(int(entrada[1]))
greedy(listaNombres, listaEdades)
