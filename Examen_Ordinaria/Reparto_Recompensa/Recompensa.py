def esFactible(concursante, pos, g):
    for j in concursante:
        if pos in g[j]:
            return False
    return True


def recogerRecompensas(concursantes, g, visited, idx, nConcursantes):
    if all(visited):
        for i in range(len(concursantes)):
            print(f"{i} ->", *concursantes[i])
        return True

    for i in range(nConcursantes):
        for pos in range(len(g)):
            if not visited[pos] and esFactible(concursantes[i], pos, g):
                concursantes[i].append(pos)
                visited[pos] = True

                if recogerRecompensas(concursantes, g, visited, idx + 1, nConcursantes):
                    return True

                visited[pos] = False
                concursantes[i].remove(pos)

    return False


# Leer la entrada
nRecompensas, nRestricciones, nConcursantes = map(int, input().strip().split())
g = [[] for _ in range(nRecompensas)]
concursantes = [[] for _ in range(nConcursantes)]

for _ in range(nRestricciones):
    r1, r2 = map(int, input().strip().split())
    g[r1].append(r2)
    g[r2].append(r1)

visited = [False] * nRecompensas

# Ejecutar la función
recogerRecompensas(concursantes, g, visited, 0, nConcursantes)
