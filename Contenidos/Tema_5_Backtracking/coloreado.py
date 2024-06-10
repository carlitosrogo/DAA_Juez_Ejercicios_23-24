def inicializarGrafo():
    grafo = {}
    grafo['n'] = 4
    grafo['Adyacencia'] = [[1,2,3], [0], [0,3], [0,2]]
    return grafo

def inicializarSolucion(g):
    sol = [0] * g['n']
    return sol

def esSolucion(nodo, grafo):
    return nodo == grafo['n']

def esFactible(grafo, sol, nodo, color):
    factible = True
    adyacenciaNodo = grafo['Adyacencia'][nodo]
    i = 0
    while factible and i < len(adyacenciaNodo):
        if adyacenciaNodo[i] < nodo:
            factible = (color != sol[adyacenciaNodo[i]])
        i += 1
    return factible


def coloreadoVA(grafo, m, sol, nodo):
    if esSolucion(nodo, grafo):
        esSol = True
    else:
        esSol = False
        color = 1
        while not esSol and color <= m:
            if esFactible(grafo, sol, nodo, color):
                sol[nodo] = color
                (sol, esSol) = coloreadoVA(grafo, m, sol, nodo + 1)
                if not esSol:
                    sol[nodo] = 0
            color += 1
    return sol, esSol

grafo = inicializarGrafo()
m = 4 #número de colores disponibles
nodo = 0 #primer nodo a colorear
sol = inicializarSolucion(grafo)
(sol, esSol) = coloreadoVA(grafo, m, sol, nodo)
if esSol:
    print(sol)
else:
    print("La instancia del problema no tiene solución")
