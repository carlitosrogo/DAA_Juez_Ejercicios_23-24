def obtenerGeneracion(arbol, persona, nGeneracion, nivel):
    nGeneracion[persona] = nivel
    for hijo in arbol.get(persona, []):
        obtenerGeneracion(arbol, hijo, nGeneracion, nivel + 1)


nMiembros = int(input())
arbol = {}
for _ in range(nMiembros):
    data = list(map(int, input().strip().split()))
    padre = data[0]
    hijos = data[1:]
    arbol[padre] = hijos

nConsultas = int(input())
generaciones = {}
for persona in arbol:
    if persona not in generaciones:
        obtenerGeneracion(arbol, persona, generaciones, 1)
for _ in range(nConsultas):
    q = int(input())
    print(generaciones[q])