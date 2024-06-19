
def getBestPareja(l,c, visited, value):
    for i in range(len(l)):
        if l[i][4]/l[i][value] < l[c][4]/l[c][value] and i not in visited or c in visited:
            c = i
    return c
def greedy(v,l):
    currentPareja = 0
    tiempo = maxTiempo
    visited = set()
    beneficio = 0
    while tiempo > 0 and len(visited) < len(l):
        bestPareja = getBestPareja(l,currentPareja,visited, v)
        visited.add(bestPareja)
        if tiempo -l[bestPareja][4] <= 0:
            beneficio += (l[bestPareja][v] * tiempo) / l[bestPareja][4]
        else:
            beneficio += l[bestPareja][v]
        print(l[bestPareja][0], end=' ')
        tiempo += -l[bestPareja][4]
    print()
    return beneficio



numConcursantes = int(input())
for i in range(numConcursantes):
    maxValor = input()
    maxTiempo = int(input())
    numParejas = int(input())
    listaParejas = []
    for _ in range(numParejas):
        inLine = input().split()
        b, i, k, t = map(int, inLine[1:])
        listaParejas.append((inLine[0], b, i, k, t))

    if maxValor == "kindness":
        value = 3
    elif maxValor == "intelligence":
        value = 2
    else: #beauty
        value = 1
    total = greedy(value, listaParejas)
    print(f"{total:.2f}")
