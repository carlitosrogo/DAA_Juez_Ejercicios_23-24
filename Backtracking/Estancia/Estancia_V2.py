def inicializarDatos():
    return {"objeto": [], "peso": [], "beneficio": []}

def inicializarSol():
    return {"objetos": [], "pesoTotal": 0, "beneficioTotal": 0}

def esSolucion(sol, maxPeso, minBeneficio):
    return sol["pesoTotal"] <= maxPeso and sol["beneficioTotal"] >= minBeneficio

def esMejorSolucion(sol, mejorSol):
    if (sol["beneficioTotal"] > mejorSol["beneficioTotal"]) or (
        sol["beneficioTotal"] == mejorSol["beneficioTotal"] and sol["pesoTotal"] < mejorSol["pesoTotal"]
    ):
        return True
    return False

def esFactible(data, sol, maxPeso, i):
    return data["peso"][i] + sol["pesoTotal"] <= maxPeso

def copySolution(sol):
    return {
        "objetos": sol["objetos"][:],
        "pesoTotal": sol["pesoTotal"],
        "beneficioTotal": sol["beneficioTotal"]
    }

def encontrarSolucion(data, sol, mejorSol, maxPeso, minBeneficio, numObjetos, idx):
    if esSolucion(sol, maxPeso, minBeneficio):
        if esMejorSolucion(sol, mejorSol):
            mejorSol = copySolution(sol)

    for i in range(idx, numObjetos):
        if esFactible(data, sol, maxPeso, i):
            # Agregar objeto actual a la solución
            sol["objetos"].append(data["objeto"][i])
            sol["pesoTotal"] += data["peso"][i]
            sol["beneficioTotal"] += data["beneficio"][i]

            # Llamada recursiva para la siguiente posición
            mejorSol = encontrarSolucion(data, sol, mejorSol, maxPeso, minBeneficio, numObjetos, i + 1)

            # Eliminar objeto actual de la solución (backtracking)
            sol["objetos"].pop()
            sol["pesoTotal"] -= data["peso"][i]
            sol["beneficioTotal"] -= data["beneficio"][i]

    return mejorSol

# Entrada de datos
nObjetos, maxPeso, minBeneficio = map(int, input().strip().split())
data = inicializarDatos()
for i in range(nObjetos):
    entrada = input().strip().split()
    data["objeto"].append(entrada[0])
    peso, beneficio = map(int, entrada[1:])
    data["peso"].append(peso)
    data["beneficio"].append(beneficio)

sol = inicializarSol()
mejorSol = inicializarSol()

solucion = encontrarSolucion(data, sol, mejorSol, maxPeso, minBeneficio, nObjetos, 0)

# Ordenar los objetos de la mejor solución final
solucion["objetos"].sort()

print(" ".join(solucion["objetos"]))
print(solucion["pesoTotal"], solucion["beneficioTotal"])
if solucion["beneficioTotal"] >= minBeneficio:
    print('SE VA')
else:
    print('VUELVE')
