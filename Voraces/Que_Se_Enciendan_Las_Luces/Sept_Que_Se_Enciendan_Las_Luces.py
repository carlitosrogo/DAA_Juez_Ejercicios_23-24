
def obtenerMejorConcursante(c, tMax, lNombres, lBelleza, lInteligencia, lAmabilidad, lTiempo, concursanteActual, seducidos):
    if lNombres[concursanteActual] in seducidos:
        for i in range(len(lNombres)):
            if lNombres[i] not in seducidos:
                concursanteActual = i
                break
    for j in range(len(lNombres)):
        if lNombres[j] not in seducidos:
            if c == "kindness":
                if lAmabilidad[j]/lTiempo[j] > lAmabilidad[concursanteActual]/lTiempo[concursanteActual]:
                    concursanteActual = j
            elif c == "intelligence":
                if lInteligencia[j]/lTiempo[j] > lInteligencia[concursanteActual]/lTiempo[concursanteActual]:
                    concursanteActual = j
            elif c == "beauty":
                if lBelleza[j]/lTiempo[j] > lBelleza[concursanteActual]/lTiempo[concursanteActual]:
                    concursanteActual = j
    return concursanteActual

def greedy(c,tMax, lNombres, lBelleza, lInteligencia, lAmabilidad, lTiempo):
    seducidos = set()
    concursanteActual = 0
    beneficioTotal = 0
    while tMax > 0 and len(lNombres) != len(seducidos):
        mejorConcursante = obtenerMejorConcursante(c, tMax, lNombres, lBelleza, lInteligencia, lAmabilidad, lTiempo, concursanteActual, seducidos)
        concursanteActual = mejorConcursante
        seducidos.add(lNombres[concursanteActual])
        print(lNombres[concursanteActual], end=" ")
        if tMax - lTiempo[concursanteActual] >= 0:
            if c == "kindness":
                beneficioTotal += lAmabilidad[concursanteActual]
            elif c == "intelligence":
                beneficioTotal += lInteligencia[concursanteActual]
            elif c == "beauty":
                beneficioTotal += lBelleza[concursanteActual]
        else:
            if c == "kindness":
                beneficioTotal += (lAmabilidad[concursanteActual] * tMax )/ lTiempo[concursanteActual]
            elif c == "intelligence":
                beneficioTotal += (lInteligencia[concursanteActual] * tMax )/ lTiempo[concursanteActual]
            elif c == "beauty":
                beneficioTotal += (lBelleza[concursanteActual] * tMax )/ lTiempo[concursanteActual]
        tMax -= lTiempo[concursanteActual]
    print()
    print("{:.2f}".format(beneficioTotal))
    # print("\n", "{:.2f}".format(beneficioTotal))
    # print("\n", f"{beneficioTotal:.2f}")
    # print("\n", "%.2f" % (beneficioTotal))

nConcursantes = int(input().strip())
for _ in range(nConcursantes):
    cualidad = input().strip()
    tiempoMax = int(input().strip())
    nParejas = int(input().strip())
    listaNombres = []
    listaBelleza = []
    listaInteligencia = []
    listaAmabilidad = []
    listaTiempo = []
    for _ in range(nParejas):
        entrada = input().strip().split()
        listaNombres.append(entrada[0])
        b, i, a, t = map(int, entrada[1:])
        listaBelleza.append(b)
        listaInteligencia.append(i)
        listaAmabilidad.append(a)
        listaTiempo.append(t)
    greedy(cualidad, tiempoMax, listaNombres, listaBelleza, listaInteligencia, listaAmabilidad, listaTiempo)

