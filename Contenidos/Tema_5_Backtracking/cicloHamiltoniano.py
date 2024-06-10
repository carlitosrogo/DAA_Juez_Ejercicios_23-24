



def test_graph():
    """
    (0)---(1)---(2)
      \  /  \  /
      (3)---(4)
    """
    v = 5
    edges = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2,4), (3, 4)]
    graph = [[] for _ in range(v)]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    return graph

def esSolucion(g, sol, nodo):
    return nodo == sol[0] and len(sol)  == len(g) + 1

def esFactible(nodo, sol, n):
    return nodo not in sol or (nodo == sol[0] and len(sol) == n)


def hamiltonianVA(g, nodo, sol, numSol):
    if esSolucion(g, sol, nodo):
        numSol += 1
    else:
        for ady in g[nodo]:
            if esFactible(ady, sol, len(g)):
                sol.append(ady)
                numSol = hamiltonianVA(g, ady, sol, numSol)
                sol.pop()
    return numSol



grafo = test_graph()

ini = 0
sol = [ini]

numSoluciones = hamiltonianVA(grafo, ini, sol, 0)