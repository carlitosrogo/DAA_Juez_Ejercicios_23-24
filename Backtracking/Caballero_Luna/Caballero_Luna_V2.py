import copy
from math import inf





def inicializarMejorSol(lab):
    mejorSol = copy.deepcopy(lab)
    mejorSol[len(lab) -1][len(lab[0]) - 1] = inf
    return mejorSol

def esMejor(sol1, sol2):
    n = len(sol1) - 1
    m = len(sol1[0]) - 1
    return sol1[n][m] < sol2[n][m]

def esFactible(lab, f, c):
    if f >= 0 and f < len(lab) and c >= 0 and c < len(lab[0]):
        return lab[f][c] >= 0 and lab[f][c] != inf
    else:
        return False

# c,f = casilla en la que está      k = pasos que lleva
def laberintoVA(lab, f, c, nEnemigos, distanciaMax):
    mejorSol = False

    if nEnemigos == 0:
        mejorSol = True
    elif distanciaMax == 0 and nEnemigos>0:
        mejorSol = False
    else:
        desp = [[1,0],[0,1], [-1,0], [0, -1]]
        i = 0
        while i < len(desp):                    #probar con todos los tipos de desplazamiento
            newF = f + desp[i][0]                   #calcular en qué pasilla se posicionaría dependiendo del paso que de
            newC = c + desp[i][1]                   #lo mismo que lo anterior
            if esFactible(lab, newF, newC):
                eraMalo = False
                if lab[newF][newC] == 1:
                    nEnemigos -= 1
                    eraMalo = True
                lab[newF][newC] = inf
                distanciaMax -=1

                mejorSol = laberintoVA(lab, newF, newC, nEnemigos, distanciaMax)
                if mejorSol:
                    return True

                if eraMalo:
                    lab[newF][newC] = 1
                    nEnemigos += 1
                else:
                    lab[newF][newC] = 0
                distanciaMax += 1

            i += 1
    return mejorSol



#Datos

lab = []

f, c, nEnemigos = map(int, input().strip().split())

for _ in range(f):
    lab.append([])

for i in range(f):
    lab[i] = list(map(int, input().strip().split()))

lunaF, lunaC, distanciaMax = map(int, input().strip().split())





#Programa


lab[lunaF][lunaC] = inf
if laberintoVA(lab, lunaF, lunaC, nEnemigos, distanciaMax):
    print("ATACA")
else:
    print("CORRE")






