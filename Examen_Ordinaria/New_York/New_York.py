def getBestLocalizacion(d, visited, node):
    bestNode = node
    for i in range(d['localizaciones']):
        print("Disfrute i:", i, d['disfrute'][i] / d['energia'][i], "/", "Disfrute node: ", bestNode,
              d['disfrute'][bestNode] / d['energia'][bestNode])
        if d['disfrute'][i] / d['energia'][i] > d['disfrute'][bestNode] / d['energia'][bestNode] and not visited[i] or \
                visited[bestNode]:
            bestNode = i
    return bestNode


def greedy(d):
    visited = [False] * d['localizaciones']
    for i in range(d['dias']):
        print("Dia: ", i)
        concurrentNode = 0
        while d['energiaPorDia'][i] >= 0:
            bestNode = getBestLocalizacion(d, visited, concurrentNode)
            print(bestNode)
            if d['energiaPorDia'][i] - d['energia'][bestNode] < 0:
                d['beneficioDia'][i] += d['disfrute'][bestNode] * d['energiaPorDia'][i] / d['energia'][bestNode]
                d['energiaPorDia'][i] -= d['energia'][bestNode]
                visited[bestNode] = True
            else:
                d['energiaPorDia'][i] -= d['energia'][bestNode]
                d['beneficioDia'][i] += d['disfrute'][bestNode]
                visited[bestNode] = True
    return d


nDias, nLocalizaciones = map(int, input().strip().split())
data = {}
ciudades = []
disfrute = []
energia = []
energiaPorDia = []
beneficioDia = []
for _ in range(nLocalizaciones):
    entrada = input().strip().split()
    disf, ener = map(int, entrada[1:])
    ciudades.append(entrada[0])
    disfrute.append(disf)
    energia.append(ener)
for _ in range(nDias):
    energiaPorDia.append(int(input().strip()))
    beneficioDia.append(0)

data['dias'] = nDias
data['localizaciones'] = nLocalizaciones
data['ciudades'] = ciudades
data['disfrute'] = disfrute
data['energia'] = energia
data['energiaPorDia'] = energiaPorDia
data['beneficioDia'] = beneficioDia
print(data)
sol = greedy(data)
mayorSol = 0
print(sol)
for beneficio in sol['beneficioDia']:
    if beneficio > mayorSol:
        mayorSol = beneficio
print("{0:.2f}".format(mayorSol))
for i in range(len(sol['beneficioDia'])):
    print(f"{i + 1}: ", "{0:.2f}".format(sol['beneficioDia'][i]))
