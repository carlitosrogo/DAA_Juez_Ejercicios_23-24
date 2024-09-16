import copy


def mochila(d, sol, mejorSol, k):

    if esSolucion(d, sol):

        if mejorSol["beneficio"] < sol["beneficio"]:
            mejorSol = copy.deepcopy(sol)

    else:
        for i in range(k, d["N"]):
            if not sol["elegido"][i] and sol["peso"] + d["peso"][i] <= d["W"]:

                sol["beneficio"] += d["beneficio"][i]
                sol["peso"] += d["peso"][i]
                sol["nombre"].append(d["nombre"][i])
                sol["elegido"][i] = True

                mejorSol = mochila(d, sol, mejorSol, i+1)

                sol["beneficio"] -= d["beneficio"][i]
                sol["peso"] -= d["peso"][i]
                sol["nombre"].pop()
                sol["elegido"][i] = False

    return mejorSol


def esSolucion(d, sol):
    min_peso = float("inf")
    for i in range(len(d["peso"])):
        if not sol["elegido"][i] and min_peso>d["peso"][i]:
            min_peso = d["peso"][i]
    return sol["peso"] + min_peso > d["W"]



def printSol(sol, beneficioMin):
    nombresSol = sorted(sol["nombre"])
    print(" ".join(nombresSol))

    print(sol["peso"], sol["beneficio"])

    if(sol["beneficio"] > beneficioMin):
        print("SE VA")
    else:
        print("VUELVE")





d = {}
sol = {}

nObjetos, pesoMax, beneficioMin = map(int, input().split())

d["W"] = pesoMax
d["N"] = nObjetos
d["nombre"] = list()
d["peso"] = list()
d["beneficio"] = list()

for n in range(nObjetos):
    nombre, peso, beneficio = input().strip().split()
    d["nombre"].append(nombre)
    d["peso"].append(int(peso))
    d["beneficio"].append(int(beneficio))

sol["elegido"] = [False] * d["N"]
sol["nombre"] = list()
sol["peso"] = 0
sol["beneficio"] = 0


mejorSol = copy.deepcopy(sol)

printSol(mochila(d, sol, mejorSol, 0), beneficioMin)