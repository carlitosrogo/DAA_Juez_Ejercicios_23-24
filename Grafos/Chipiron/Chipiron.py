from collections import deque


def bfs(g):
    moveX = [-1, 0, 1, 0]
    moveY = [0, 1, 0, -1]
    visited = [[[False] * 2 for _ in range(numColumnas)] for _ in range(numFilas)]
    q = deque([(0, 0, 1)])
    visited[0][0][1] = True
    while q:
        x, y, t = q.popleft()
        if g[x][y] == 2:
            return t
        else:
            for i in range(len(moveX)):
                newX = moveX[i] + x
                newY = moveY[i] + y
                if newX < 0 or newX >= numFilas or newY < 0 or newY >= numColumnas:
                    continue
                if visited[newX][newY][t % 2] or (g[newX][newY] == -1 and t % 2 == 0):
                    print(t%2)
                    continue
                visited[newX][newY][t % 2] = True
                q.append((newX, newY, t + 1))


numFilas, numColumnas = map(int, input().strip().split())
adjancecyMatrix = [list(map(int, input().split())) for _ in range(numFilas)]
result = bfs(adjancecyMatrix)
print(result - 1)
