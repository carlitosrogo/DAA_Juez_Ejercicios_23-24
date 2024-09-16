def DyV(g, nivelMax, low, max):
    if low > max:
        return max
    else:
        mid = low + max // 2
        if g[]

nEnemigos = int(input().strip())
listaEnemigos = map(int, input().strip().split())
nCasos = int(input().strip())
for _ in range(nCasos):
    nivel = int(input().strip())
    DyV(listaEnemigos, nivel, 0, len(listaEnemigos) - 1)
