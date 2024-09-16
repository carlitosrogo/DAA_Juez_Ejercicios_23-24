
def esSolucion(matriz):
    for fila in matriz:
        if 1 in fila:
            return False
    return True
def solucionFactible(x,y,matriz):
    if x > len(matriz) - 1 or y > len(matriz[x]) - 1 or x < 0 or y < 0:
        return False
    else:
        if matriz[x][y] == -1:
            return False
        elif matriz[x][y] == 1:
            matriz[x][y] = 2
            return True
        elif matriz[x][y] == 2:
            return False
        else:
            matriz[x][y] = 2
            return True

def rebotarArma(posicionX,posicionY,etapa, matriz):
    if esSolucion(matriz):
        return True
    else:
        if etapa > 0:
            x = [1, -1, 0, 0]
            y = [0, 0, 1, -1]
            for i in range(len(x)):
                newMatriz = matriz.copy()
                if solucionFactible(posicionX + x[i],posicionY + y[i],newMatriz):
                    if rebotarArma(posicionX + x[i],posicionY + y[i], etapa - 1, newMatriz):
                        return True
        else:
            return False



nFilas, nColumnas, nEnemigos = map(int,input().strip().split())
matriz = []
for i in range(nFilas):
    matriz.append(list(map(int, input().strip().split())))
filaPosicion, columnaPosicion, rebotes = map(int, input().strip().split())

accion = rebotarArma(filaPosicion,columnaPosicion, rebotes, matriz)
if accion:
    print("ATACA")
else:
    print("CORRE")