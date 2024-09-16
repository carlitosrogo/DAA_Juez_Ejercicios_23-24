def buscarPosicionPersona(grupo, persona, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if grupo[mid] == persona:
            return mid
        elif grupo[mid] > persona:
            return buscarPosicionPersona(grupo, persona, low, mid - 1)
        else:
            return buscarPosicionPersona(grupo, persona, mid + 1, high)


nPersonas1 = int(input())
grupo1 = list(map(int, input().strip().split()))
nPersonas2 = int(input())
grupo2 = list(map(int, input().strip().split()))
nParejas = int(input())
for _ in range(nParejas):
    p1, p2 = map(int, input().strip().split())
    posicionGrupo1 = buscarPosicionPersona(grupo1,p1,0,len(grupo1)-1)
    posicionGrupo2 = buscarPosicionPersona(grupo2,p2,0,len(grupo2)-1)
    if posicionGrupo1 != -1 and posicionGrupo2 != -1:
        print(posicionGrupo1, posicionGrupo2)
    else:
        print("SIN DESTINO")