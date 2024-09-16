def inicializarDatos():
    d = {"objeto": [], "peso": [], "beneficio": []}
    return d
def inicializarSol():
    sol = {"objetos":[], "pesoTotal": 0, "beneficioTotal": 0}
    return sol
def esSolucion(sol, maxPeso, minBeneficio):
    if sol["pesoTotal"] <= maxPeso and sol["beneficioTotal"] >= minBeneficio:
        return True
    else:
        return False
def esMejorSolucion(sol, mejorSol):
    print("¿Es mejor solucion?", sol , mejorSol)
    if (sol["beneficioTotal"] > mejorSol["beneficioTotal"]) or (sol["pesoTotal"] < mejorSol["pesoTotal"] and sol["beneficioTotal"] >= mejorSol["beneficioTotal"]):
        print("Solucion verdadera")
        return True
    else:
        print("Solucion falsa")
        return False
def copySolution(sol):
    return {
        "objetos": sol["objetos"][:],
        "pesoTotal": sol["pesoTotal"],
        "beneficioTotal": sol["beneficioTotal"]
    }
def esFactible(data,sol,maxPeso,i):
    print(data["objeto"][i], data["peso"][i], data["beneficio"][i])
    print(sol)
    print("peso total:" ,data["peso"][i] + sol["pesoTotal"], "Max peso: ",maxPeso)
    if data["peso"][i] + sol["pesoTotal"] <= maxPeso:
        return True
    else:
        return False
def encontrarSolucion(data, sol, mejorSol, maxPeso, minBeneficio, numObjetos, idx):
    if esSolucion(sol, maxPeso, minBeneficio):
        if esMejorSolucion(sol, mejorSol):
            mejorSol = copySolution(sol)

    for i in range(idx, numObjetos):
        if esFactible(data, sol, maxPeso, i):
            sol["objetos"].append(data["objeto"][i])
            sol["pesoTotal"] += data["peso"][i]
            sol["beneficioTotal"] += data["beneficio"][i]

            mejorSol = encontrarSolucion(data, sol, mejorSol, maxPeso, minBeneficio, numObjetos, i + 1)

            sol["objetos"].pop()
            sol["pesoTotal"] -= data["peso"][i]
            sol["beneficioTotal"] -= data["beneficio"][i]

    return mejorSol


nObjetos, maxPeso, minBeneficio = map(int, input().strip().split())
data = inicializarDatos()
sol = inicializarSol()
mejorSol = inicializarSol()
for i in range(nObjetos):
    entrada = input().strip().split()
    data["objeto"].append(entrada[0])
    peso, beneficio = map(int, entrada[1:])
    data["peso"].append(peso)
    data["beneficio"].append(beneficio)

solucion = encontrarSolucion(data, sol, mejorSol, maxPeso,minBeneficio, nObjetos, 0)
solucion["objetos"].sort()
print(" ".join(solucion["objetos"]))
print(solucion["pesoTotal"], solucion["beneficioTotal"])
if solucion["beneficioTotal"] > minBeneficio:
    print('SE VA')
else:
    print('VUELVE')