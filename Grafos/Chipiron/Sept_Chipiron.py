from collections import deque

def ord_dfs(m):
    q = deque([(0,0,1)])
    moveX = [0,0,1,-1]
    moveY = [1,-1,0,0]
    while q:
        x, y, t = q.popleft()
        if m[x][y] == 2:
            return t
        for i in range(4):
            newX = x + moveX[i]
            newY = y + moveY[i]
            if newX < 0 or newX >= len(m) or newY < 0 or newY >= len(m[0]) or (m[newX][newY] == -1 and t%2 == 0):
                continue
            q.append((newX, newY, t+1))
    return -1

nFilas, nColumnas = map(int, input().strip().split())
matriz = []
for i in range(nFilas):
    matriz.append(list(map(int,input().strip().split())))
print(matriz)
print(ord_dfs(matriz) - 1)