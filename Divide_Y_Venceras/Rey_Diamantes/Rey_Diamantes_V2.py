def eliminarJugadores(fila, jugador, low, high):
    if low > high:
        mid = (low + high) // 2
        if mid + 1 < len(fila):
            mid += 1
        else:
            mid = len(fila)
        return mid
    else:
        mid = (low + high) // 2
        if fila[mid] == jugador:
            return mid
        elif isinstance(fila[mid], int) and fila[mid] > jugador:
            return eliminarJugadores(fila, jugador, low, mid - 1)
        else:
            return eliminarJugadores(fila, jugador, mid + 1, high)

nTamaño = int(input())
matriz = []
for _ in range(nTamaño):
    matriz.append(list(map(int, input().strip().split())))
eliminados = list(map(int, input().strip().split()))
for elem in eliminados:
    for i in range(len(matriz)):
        if isinstance(matriz[i][-1], int) and matriz[i][-1] >= elem:
            posicionEliminar = eliminarJugadores(matriz[i], elem, 0, len(matriz[i]) - 1 )
            if matriz[i][posicionEliminar] >= elem:
                matriz[i][posicionEliminar] = 'X'
                break
for fila in matriz:
    print(*fila)