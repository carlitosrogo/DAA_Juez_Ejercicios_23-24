from collections import deque

def bfs(grid, N, M):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque([(0, 0, 1)])
    visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = True
    while queue:
        x, y, t = queue.popleft()
        if grid[x][y] == 2:
            return t
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny][t%2] or (grid[nx][ny] == -1 and t%2 == 0):
                continue
            visited[nx][ny][t%2] = True
            queue.append((nx, ny, t+1))
    return -1

def solve():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = bfs(grid, N, M)
    print(result - 1)

solve()