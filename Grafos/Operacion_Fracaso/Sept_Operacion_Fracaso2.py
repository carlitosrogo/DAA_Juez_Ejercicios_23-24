from collections import deque


def visit_bfs(g, nodo, visited, nPersonas, nota):
    q = deque()
    visited[nodo] = True
    q.append((nodo, nota))
    print("Nodo: ", nodo, ", Personas: ", nPersonas, ", Nota: ", nota)
    while q:
        nodoAux, notaLocal = q.popleft()
        if notaLocal <= 0:
            continue
        nPersonas += 1
        print("Nodo adj: ", nodoAux, ", Personas: ", nPersonas, ", Nota: ", notaLocal)
        for nodoAdj in g[nodoAux]:
            if not visited[nodoAdj]:
                q.append((nodoAdj, notaLocal - 1))
                visited[nodoAdj] = True
    return nPersonas, notaLocal


def ord_bfs(g, nota):
    visited = [False] * len(g)
    nPersonas = 0
    for nodo in range(len(g)):
        if not visited[nodo]:
            nPersonas, nota = visit_bfs(g, nodo, visited, nPersonas, nota)
    print(nPersonas)


nConcursantes = int(input().strip())
for _ in range(nConcursantes):
    nota, nFans, nConexiones = map(int, input().strip().split())
    listaConsursantes = [[] for _ in range(nFans)]
    for _ in range(nConexiones):
        nodo1, nodo2 = map(int, input().strip().split())
        listaConsursantes[nodo1].append(nodo2)
        listaConsursantes[nodo2].append(nodo1)
    ord_bfs(listaConsursantes, nota)
