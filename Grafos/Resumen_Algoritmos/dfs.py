def visit_dfs(g, nodo, visited):
    visited.add(nodo)
    for nodoAdj in g[nodo]:
        visit_dfs(g, nodoAdj, visited)
def dfs(g):
    '''La parte comentada es en caso de empezar siempre primero por el nodo 0'''
    # n = len(g) -1
    visited = set()
    # visited.add(0)
    # for nodo in range(1, n + 1):
    for nodo in range(len(g)):
        if nodo not in visited:
            visit_dfs(g,nodo, visited)