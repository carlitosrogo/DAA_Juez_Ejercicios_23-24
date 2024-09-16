
def rec_dv(data, start, end, search):
    if start > end:
        mid = (start + end) // 2
        if mid + 1 < len(data):
            mid = mid + 1
        else:
            mid = len(data)
        return mid
    else:
        mid = (start + end) // 2
        if data[mid] == search:
            return mid
        else:
            if search > data[mid]:
                return rec_dv(data, mid + 1, end, search)
            else:
                return rec_dv(data, start, mid - 1, search)

#Entrada
n = int(input().strip())
boardMat = []

for i in range(n):
    fila = list(map(int, input().strip().split()))
    boardMat.append(fila)

eliminationList = list(map(int, input().strip().split()))
eliminationList.sort()

for eliminados in eliminationList:
    for i in range(len(boardMat)):
        if eliminados <= boardMat[i][-1]: #boardMat[i][-1] da el último elemento de la fila i
            aEliminar = rec_dv(boardMat[i], 0, len(boardMat[i])-1, eliminados)
            if boardMat[i][aEliminar] >= eliminados:
                boardMat[i][aEliminar] = -1
                break

for fila in range(n):
    for elements in range(n):
        if boardMat[fila][elements] == -1:
            boardMat[fila][elements] = 'X'

    print(*boardMat[fila])