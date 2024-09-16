def visit_dfs(g, visited, node, listaVisitados):
    visited.add(node)
    print(node, ', ',listaVisitados)
    for nodeAdj in g[node]:
        if not nodeAdj in visited:
            listaVisitados.append(nodeAdj)
            visit_dfs(g, visited, nodeAdj, listaVisitados)
def ord_topsport(g):
    n = len(g) -1
    visited = set()
    listaVisitados = []
    visited.add(0)
    listaVisitados.append(0)
    for nodeAdj in range(1, n +1):
        if not nodeAdj in visited:
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