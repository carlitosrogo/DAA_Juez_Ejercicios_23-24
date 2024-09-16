def buscarPosicion(fila, jugador, low, high):
    while low <= high:
        mid = (low + high) // 2
        if fila[mid] == jugador:
            return mid
        elif isinstance(fila[mid], int) and fila[mid] > jugador:
            high = mid - 1
        else:
            low = mid + 1
    # Si no se encuentra el jugador, se devuelve la posición más cercana
    return low if low < len(fila) and isinstance(fila[low], int) and fila[low] > jugador else -1

nTamaño = int(input())
matriz = []
for _ in range(nTamaño):
    matriz.append(list(map(int, input().strip().split())))
eliminados = list(map(int, input().strip().split()))

for elem in eliminados:
    for i in range(len(matriz)):
        # Realizar la búsqueda solo si el último elemento de la fila es un número y es mayor o igual al jugador
        if isinstance(matriz[i][-1], int) and matriz[i][-1] >= elem:
            posicionEliminar = buscarPosicion(matriz[i], elem, 0, len(matriz[i]) - 1)
            if posicionEliminar != -1 and matriz[i][posicionEliminar] >= elem:
                matriz[i][posicionEliminar] = 'X'
                break

for fila in matriz:
    print(*fila)
