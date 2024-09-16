
def getCandidates(g):
    candidates = []

    for adj in g:
        for adj in adj:
            candidates.append(adj)

    return sorted(candidates, key=lambda x: x[2])


def updateConcursantes(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id



def kruskal(g):
    candidates = getCandidates(g)
    concursantes = list(range(len(g)))

    esfuerzoIndividual = [0] * len(g)
    esfuerzoTotal = 0

    visited = len(g)

    i = 0
    while visited>0 and len(candidates)>i:
        adj = candidates[i]
        print(adj, i)
        print(concursantes)
        if concursantes[adj[0]] != concursantes[adj[1]]:
            visited -= 1
            esfuerzoTotal += adj[2]
            esfuerzoIndividual[adj[0]] += adj[2]
            esfuerzoIndividual[adj[1]] += adj[2]
            updateConcursantes(concursantes, concursantes[adj[0]], concursantes[adj[1]])
        print(concursantes)
        i += 1


    for i in range(n):
        print('C{} -> '.format(i), esfuerzoIndividual[i])
    print('Esfuerzo realizado -> ', esfuerzoTotal)


g = []
n, c = map(int, input().strip().split())
for _ in range(n):
    g.append([])

for _ in range(c):
    ini, fin, relacion = map(int, input().strip().split())
    g[ini].append((ini, fin, relacion))
    g[fin].append((fin, ini, relacion))


kruskal(g)