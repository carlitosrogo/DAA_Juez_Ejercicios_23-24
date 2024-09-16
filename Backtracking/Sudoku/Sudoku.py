def esFactible(matriz, fila, columna, numero):
    if numero in matriz[fila]:
        return False
    for i in range(9):
        if numero == matriz[i][columna]:
            return False
    filaSubMatriz = (fila // 3) * 3
    columnaSubMatriz = (columna // 3) * 3
    for filaSub in range(filaSubMatriz, filaSubMatriz+3):
        for columnaSub in range(columnaSubMatriz, columnaSubMatriz+3):
            if matriz[filaSub][columnaSub] == numero:
                return False
    return True
def esSolucion(matriz):
    for fila in matriz:
        if 0 in fila:
            return False
    return True


def construirSudoku(matriz):
    if esSolucion(matriz):
        for fila in matriz:
            print(*fila)
        return True

    for f in range(9):
        for c in range(9):
            if matriz[f][c] == 0:
                for num in range(1, 10):
                    if esFactible(matriz, f, c, num):
                        matriz[f][c] = num
                        if construirSudoku(matriz):
                            return True
                        matriz[f][c] = 0
                return False

    return False

matriz = []
for i in range(9):
    matriz.append(list(map(int, input().strip().split())))

construirSudoku(matriz)
