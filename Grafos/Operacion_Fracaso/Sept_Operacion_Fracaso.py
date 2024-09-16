def visit_dfs(g, nodo, visited, nPersonas, nota):
    if nota > 0:
        visited.add(nodo)
        print("Nodo: ", nodo,", Personas: ", nPersonas,", Nota: ", nota)
        nPersonas += 1
        for nodoAdj in g[nodo]:
            if nodoAdj not in visited:
                visit_dfs(g, nodoAdj, visited, nPersonas, nota - 1)


def ord_dfs(g, nota):
    n = len(g) - 1
    visited = set()
    nPersonas = 0
    visited.add(0)
    nPersonas += 1
    for nodo in range(1, n + 1):
        if nodo not in visited:
            visit_dfs(g, nodo, visited, nPersonas, nota)
    print(nPersonas)


nConcursantes = int(input().strip())
for _ in range(nConcursantes):
    nota, nFans, nConexiones = map(int, input().strip().split())
    listaConsursantes = [[] for _ in range(nFans)]
    for _ in range(nConexiones):
        nodo1, nodo2 = map(int, input().strip().split())
        listaConsursantes[nodo1].append(nodo2)
        listaConsursantes[nodo2].append(nodo1)
    ord_dfs(listaConsursantes, nota)
