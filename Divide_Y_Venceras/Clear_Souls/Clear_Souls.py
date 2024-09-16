def obtenerEnemigosDerrotados(nivelCaballero, numNivelesEnemigos, low , high):
    if low > high:
        return high
    else:
        mid = (low + high) // 2
        if numNivelesEnemigos[mid] < nivelCaballero:
            return obtenerEnemigosDerrotados(nivelCaballero, numNivelesEnemigos, mid + 1, high)
        elif numNivelesEnemigos[mid] > nivelCaballero:
            return obtenerEnemigosDerrotados(nivelCaballero, numNivelesEnemigos, low, mid -1)
        else: # mid == nivelCaballero
            return mid


numEnemigosOleada = int(input())
numNivelesEnemigos = list(map(int, input().strip().split()))
listaExperienciaNivel = [numNivelesEnemigos[0]]
for i in range(1, len(numNivelesEnemigos)):
    listaExperienciaNivel.append(numNivelesEnemigos[i] + listaExperienciaNivel[i - 1])
numOleadas = int(input())

for i in range(numOleadas):
    q = int(input())
    maxLevel = obtenerEnemigosDerrotados(q,numNivelesEnemigos,0, len(numNivelesEnemigos)-1)

    if maxLevel == -1:
        print(0, 0)
    else:
        print(maxLevel + 1, listaExperienciaNivel[maxLevel])



