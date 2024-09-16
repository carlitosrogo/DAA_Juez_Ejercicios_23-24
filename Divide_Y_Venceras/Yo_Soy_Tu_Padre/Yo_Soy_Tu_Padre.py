def obtenerGeneracion(idPersona, nGeneracion, low, high):
    if low > high:
        return high
    else:
        mid = (low + high) // 2
        if idPersona in nGeneracion[mid]:
            return mid
        elif idPersona in nGeneracion[low]:
            return low
        elif idPersona in nGeneracion[high]:
            return high
        else:
            return obtenerGeneracion(idPersona, nGeneracion, low + 1, high - 1)


nMiembros = int(input())
arbolFamiliar = []
nGeneracion = [[0]]
for _ in range(nMiembros):
    data = list((map(int, input().strip().split())))
    padre = data[0]
    hijos = data[1:]
    index = None
    print(nGeneracion)
    for i in range(len(nGeneracion)):
        if padre in nGeneracion[i]:
            index = i - 1
            break
    arbolFamiliar.append(padre)
    if hijos and not index:
        nGeneracion.append(hijos)
    elif hijos and index:
        nGeneracion[index].append(hijos)
print("arbolFamiliar ", arbolFamiliar)
print("nGeneracion ", nGeneracion)
nConsultas = int(input())
for _ in range(nConsultas):
    q = int(input())
    generacion = obtenerGeneracion(q, nGeneracion, 0, len(nGeneracion) - 1)
    print(generacion + 1)