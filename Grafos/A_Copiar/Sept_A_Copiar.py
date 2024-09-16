from collections import deque

def visit_topSport(g, nodo):
    q = deque()
    g["visited"][nodo] = True
    print(g["visited"], g["totalGrupos"])
    g["totalGrupos"] = g["totalGrupos"] + 1
    q.append(nodo)
    while q:
        nodoAux = q.popleft()
        print(nodoAux, g["grafo"][nodoAux])
        for i in g["grafo"][nodoAux]:
            if not g["visited"][i]:
                q.append(i)
                g["visited"][i] = True


def ord_topSport(g):
    data = {
        "grafo" : g,
        "visited" : [False] * len(g),
        "totalGrupos" : 0
    }
    for i in range(len(data["grafo"])):
        if not data["visited"][i]:
            visit_topSport(data, i)
    print(data["totalGrupos"])

nEstudiantes, nConexiones = map(int, input().strip().split())
print(nEstudiantes, nConexiones)
listaAdyacencia = [[] for _ in range(nEstudiantes)]
print(listaAdyacencia)
for _ in range(nConexiones):
    nodo1, nodo2 = map(int, input().strip().split())
    listaAdyacencia[nodo1].append(nodo2)
    listaAdyacencia[nodo2].append(nodo1)
ord_topSport(listaAdyacencia)
print(listaAdyacencia)