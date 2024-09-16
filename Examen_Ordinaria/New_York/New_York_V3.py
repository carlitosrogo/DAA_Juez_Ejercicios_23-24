def mochila(d, visitados, energiaDiaria):

    datosSort = sorted(d["orden"], key=lambda x: d["energia"][x]/d["disfrute"][x])
    disfruteDiario = 0
    i = 0
    print("Dia x")
    while energiaDiaria>0 and i<len(datosSort):
        pos = datosSort[i]

        if not visitados[pos]:

            if energiaDiaria - d["energia"][pos]<0:
                disfruteDiario += d["disfrute"][pos] * (energiaDiaria / d["energia"][pos])
                energiaDiaria = 0
                visitados[pos] = True
                print("Nodo ", pos, d["energia"][pos]/d["disfrute"][pos])
            else:
                disfruteDiario += d["disfrute"][pos]
                energiaDiaria -= d["energia"][pos]
                visitados[pos] = True
                print("Nodo ", pos, d["energia"][pos]/d["disfrute"][pos])

        i += 1

    return visitados, disfruteDiario




d = {
    "nombre": [],
    "disfrute": [],
    "energia": []
}

energiaDaria = []


nDias, nLocalizaciones = map(int, input().strip().split())

for _ in range(nLocalizaciones):
    n, di, e = input().strip().split()

    d["nombre"].append(n)
    d["disfrute"].append(int(di))
    d["energia"].append(int(e))

for _ in range(nDias):
    m = int(input().strip())
    energiaDaria.append(m)

d["orden"] = list(range(len(d["nombre"])))

total = []
visitados = [False]*len(d["nombre"])
for i in energiaDaria:
    #visitados, dt = viajeNewYork(d, i, visitados)
    visitados, dt = mochila(d, visitados, i)
    total.append(dt)


print("{0:.2f}".format(max(total)))
for i in range(len(total)):
    print(str(i+1) + ": " + str("{0:.2f}".format(total[i])))