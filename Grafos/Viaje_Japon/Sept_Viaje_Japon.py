import copy


def darVueltaALista(g):
    nuevaLista = []
    for i in g:
        nuevaLista.insert(0,i)
    return nuevaLista
def visit_dfs(g, nodo, visited):
    visited.add(nodo)
    print("Nodo", nodo, "visitado ")
    for nodoAdj in g[nodo]:
        if nodoAdj not in visited:
            visit_dfs(g, nodoAdj, visited)
def ord_dfs(g):
    visited = set()
    visit_dfs(g,0, visited)
    if len(g) > len(visited):
        print("CAMBIA EL ITINERARIO")
        return
    listaReordenada = darVueltaALista(g)
    print("Lista dada la vuelta:",listaReordenada)
    listaAux = copy.deepcopy(g)
    listaAux.reverse()
    listaReordenada = listaAux
    print("Lista dada la vuelta:",listaReordenada)

    listaReordenada = g[::-1]
    print("Lista dada la vuelta:",listaReordenada)

    listaReordenada = list(reversed(g))

    print("Lista dada la vuelta:",listaReordenada)
    print("Lista orginial:", g)
    visited = set()
    visit_dfs(listaReordenada, 0, visited)
    if len(listaReordenada) > len(visited):
        print("CAMBIA EL ITINERARIO")
    else:
        print("PERFECTO")

nCuidades, nConexiones = map(int, input().strip().split())
listaCuidades = [[] for _ in range(nCuidades)]
for _ in range(nConexiones):
    nodo1, nodo2 = map(int, input().strip().split())
    listaCuidades[nodo1].append(nodo2)
ord_dfs(listaCuidades)

