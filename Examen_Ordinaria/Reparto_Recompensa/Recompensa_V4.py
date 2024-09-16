def esFactible(concursante, pos, g):
    for j in concursante:
        if pos in g[j]:
            return False
    return True


def esSolucion(visited):
    return all(visited)


def recogerRecompensas(concursantes, g, visited, nConcursantes, memo):
    if esSolucion(visited):
        for i in range(len(concursantes)):
            print(f"{i} ->", *concursantes[i])
        return True

    state = tuple(visited)
    if state in memo:
        return memo[state]

    for i in range(nConcursantes):
        for pos in range(len(g)):
            if not visited[pos] and esFactible(concursantes[i], pos, g):
                concursantes[i].append(pos)
                visited[pos] = True

                if recogerRecompensas(concursantes, g, visited, nConcursantes, memo):
                    memo[state] = True
                    return True

                visited[pos] = False
                concursantes[i].remove(pos)

    memo[state] = False
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
memo = {}

# Ejecutar la función
recogerRecompensas(concursantes, g, visited, nConcursantes, memo)
