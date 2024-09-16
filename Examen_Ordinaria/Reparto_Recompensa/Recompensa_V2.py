def esFactible(concursante,pos, g):
    for j in concursante:
        if pos in g[j]:
            return False
    return True

def esSolucion(visited):
    return all(visited)
def recogerRecompensas(concursantes, g, visited, idx):
    if esSolucion(visited):
        for i in range(len(concursantes)):
            print(f"{i} ->", *concursantes[i])
        return True
    else:
        for i in range(len(concursantes)):
            for pos in range(idx, len(g)):
                if not visited[pos] and esFactible(concursantes[i], pos, g):
                    concursantes[i].append(pos)
                    visited[pos] = True

                    if recogerRecompensas(concursantes,g, visited, idx+1):
                        return True

                    visited[pos] = False
                    concursantes[i].remove(pos)
        return False

nRecompensas, nRestricciones, nConcursantes = map(int, input().strip().split())
g = [[] for _ in range(nRecompensas)]
concursantes = [[] for _ in range(nConcursantes)]
for i in range(nRestricciones):
    r1, r2 = map(int, input().strip().split())
    g[r1].append(r2)
    g[r2].append(r1)
visited = [False] * nRecompensas

recogerRecompensas(concursantes, g, visited, 0)
