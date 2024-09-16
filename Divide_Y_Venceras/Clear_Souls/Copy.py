def obtenerEnemigosDerrotados(nivelCaballero, numNivelesEnemigos, low , high):
    if low > high:
        print("high", high)
        return high
    else:
        mid = (low + high) // 2
        if numNivelesEnemigos[mid] < nivelCaballero:
            print("numNivelesEnemigos[mid] < nivelCaballero, mid: ", mid + 1, "high : ", high)
            return obtenerEnemigosDerrotados(nivelCaballero, numNivelesEnemigos, mid + 1, high)
        elif numNivelesEnemigos[mid] > nivelCaballero:
            print("numNivelesEnemigos[mid] > nivelCaballero, low: ", low, "mid : ", mid -1)
            return obtenerEnemigosDerrotados(nivelCaballero, numNivelesEnemigos, low, mid -1)
        else: # mid == nivelCaballero
            print("mid", mid)
            return mid


numEnemigosOleada = int(input())
print("numEnemigosOleada ",numEnemigosOleada )
numNivelesEnemigos = list(map(int, input().strip().split()))
print("numNivelesEnemigos ",numNivelesEnemigos)
listaExperienciaNivel = [numNivelesEnemigos[0]]
for i in range(1, len(numNivelesEnemigos)):
    listaExperienciaNivel.append(numNivelesEnemigos[i] + listaExperienciaNivel[i - 1])
print("listaExperienciaNivel ",listaExperienciaNivel)
numOleadas = int(input())
print("numOleadas ",numOleadas)

for i in range(numOleadas):
    q = int(input())
    maxLevel = obtenerEnemigosDerrotados(q,numNivelesEnemigos,0, len(numNivelesEnemigos)-1)

    if maxLevel == -1:
        print(0, 0)
    else:
        print(numNivelesEnemigos[maxLevel], listaExperienciaNivel[maxLevel])



