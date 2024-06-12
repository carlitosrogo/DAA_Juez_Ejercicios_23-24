from collections import deque


def visitGruops(n, g, visited, cont):
    cont += 1
    q = deque()
    visited[n] = True
    q.append(n)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)
    return cont


def checkGroups(g):
    groups = 0
    visited = [False] * len(g)
    for n in range(len(g)):
        if not visited[n]:
            groups = visitGruops(n, g, visited, groups)
    print(groups)


numStudents, numRelations = map(int, input().strip().split())
adjacencyList = [[] for _ in range(numStudents)]

for v in range(numRelations):
    student1, student2 = map(int, input().strip().split())
    adjacencyList[student1].append(student2)
    adjacencyList[student2].append(student1)

checkGroups(adjacencyList)
