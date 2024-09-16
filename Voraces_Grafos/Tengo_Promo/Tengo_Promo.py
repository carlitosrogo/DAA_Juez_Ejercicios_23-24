
def ordernarListaActividades(g):
    actividadesLista = []
    for node in g:
        for tipoActividad, origen, destino, longitud in node:
            actividadesLista.append((longitud,tipoActividad,origen,destino))
    actividadesLista.sort()
    return actividadesLista

def kruskal (g, totalActividades):
    candidatos = ordernarListaActividades(g)
    actividades = list(range(len(g)))
    contador = len(g)
    i = 0
    while contador > 0 and len(candidatos)>i:
        print(candidatos[i])
        long, tipoAct, nodeOrigen, nodeDest = candidatos[i]
        print(totalActividades)
        print(tipoAct, g[nodeDest])
        for tipo, nOrigen, nDestino, longitud in g[nodeDest]:
            if nodeOrigen == nDestino and nodeDest == nOrigen and tipo == tipoAct and totalActividades[tipoAct] == 0:
                totalActividades[tipoAct] += long
                contador -= 1
        i += 1
    print(*totalActividades)

numActividades, numConexiones = map(int, input().strip().split())
adjList = [[] for _ in range(numActividades)]
tipoActividad = list(map(int,input().split()))
elementosUnicos = set(tipoActividad)
totalActividades = [0] * len(elementosUnicos)
print(tipoActividad)
for i in range(numConexiones):
    c,d,l = map(int,input().strip().split())
    adjList[c].append((tipoActividad[c],c,d,l))
    adjList[d].append((tipoActividad[d],d,c,l))
print(adjList)
kruskal(adjList,totalActividades)
