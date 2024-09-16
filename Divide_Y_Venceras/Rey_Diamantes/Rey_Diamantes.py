def eliminarJugadores(matriz, jugador):
    encontrado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == jugador or (isinstance(matriz[i][j], int) and matriz[i][j] > jugador) :
                matriz[i][j] = 'X'
                encontrado = True
                break
        if encontrado:
            break


nTamaño = int(input())
matriz = []
for _ in range(nTamaño):
    matriz.append(list(map(int, input().strip().split())))
eliminados = list(map(int, input().strip().split()))
for elem in eliminados:
    eliminarJugadores(matriz, elem)
for fila in matriz:
    print(*fila)