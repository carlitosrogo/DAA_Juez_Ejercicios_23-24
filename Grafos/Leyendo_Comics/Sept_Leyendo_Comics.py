def visit_dfs(g, visited, node, listaVisitados):
    visited[node] = True
    print(node, ', ',listaVisitados)
    for nodeAdj in g[node]:
        if not visited[nodeAdj]:
            listaVisitados.append(nodeAdj)
            visit_dfs(g, visited, nodeAdj, listaVisitados)
def ord_topsport(g):
    visited = [False] * len(g)
    listaVisitados = []
    visited[0] = True
    listaVisitados.append(0)
    for nodeAdj in g[0]:
        if not visited[nodeAdj]:
            listaVisitados.append(nodeAdj)
            visit_dfs(g, visited, nodeAdj, listaVisitados)
    return listaVisitados

nComics, nConexiones = map(int, input().strip().split())
listaComics = [[] for _ in range(nComics)]
for i in range(nConexiones):
    nodo1, nodo2 = map(int, input().strip().split())
    listaComics[nodo1].append(nodo2)
print(listaComics)
print(ord_topsport(listaComics))