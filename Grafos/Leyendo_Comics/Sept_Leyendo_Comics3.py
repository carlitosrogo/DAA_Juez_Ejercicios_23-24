from collections import deque


def visit_bfs(g, visited, node, listaVisitados):
    q = deque()
    q.append(node)
    visited[node] = True
    print(node, ', ',listaVisitados)

    while q:
        nodeAux = q.popleft()
        for nodeAdj in g[nodeAux]:
            newNode = comprobar_anterirores_obtener_nodo(g, nodeAdj, visited)
            print(newNode)
            if newNode != -1:
                visited[newNode] = True
                listaVisitados.append(newNode)
                q.append(newNode)
            if not visited[nodeAdj]:
                if not comprobar_dependencias(g, nodeAdj, visited):
                    visited[nodeAdj] = True
                    listaVisitados.append(nodeAdj)
                    q.append(nodeAdj)
def ord_bfs(g):
    visited = [False] * len(g)
    listaVisitados = []
    for node in range(len(g)):
        if not visited[node]:
            if not comprobar_dependencias(g, node, visited):
                newNode = comprobar_anterirores_obtener_nodo(g, node, visited)
                if newNode != -1:
                    node = newNode
                listaVisitados.append(node)
                visit_bfs(g, visited, node, listaVisitados)
    return listaVisitados

def comprobar_dependencias(g,nodo, visited):
    dependencia = False
    for nodoPadre in range(len(g)):
        if nodo in g[nodoPadre] and not visited[nodoPadre]:
            print("No se puede leer aun ", nodo, "por que lo contiene", nodoPadre)
            dependencia = True
            break
    return dependencia

def comprobar_anterirores_obtener_nodo(g, nodo, visited):
    newNode = -1
    for nodoRev in range(0, nodo):
        print("Comprobar anteriores ", nodoRev)
        if not visited[nodoRev] and not comprobar_dependencias(g, nodoRev, visited):
            newNode = nodoRev
            break
    return newNode

nComics, nConexiones = map(int, input().strip().split())
listaComics = [[] for _ in range(nComics)]
for i in range(nConexiones):
    nodo1, nodo2 = map(int, input().strip().split())
    listaComics[nodo1].append(nodo2)
print(listaComics)
listaOrdenada = ord_bfs(listaComics)
print(" ".join(map(str, listaOrdenada)))