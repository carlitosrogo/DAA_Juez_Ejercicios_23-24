import copy


def inicializarSolucion():
    sol = {'candidatos': [], 'diferenciaContratar': [], 'totalBeneficio': 0, 'totalCoste': 0}
    return sol


def esMejorSolucion(sol, mejorSol):
    if sol['totalBeneficio'] > mejorSol['totalBeneficio']:
        return True
    return False


def esFactible(d, sol, pos):
    if sol['totalCoste'] + d['costes'][pos] <= d['presupuesto']:
        return True
    return False


def mochila(d, sol, mejorSol, solucionesPosibles, idx):
    if idx == d['numCandidatos']:
        if sol['totalBeneficio'] > 0 and sol['totalCoste'] <= d['presupuesto']:
            print(sol)
            solucionesPosibles += 1
            if esMejorSolucion(sol, mejorSol):
                mejorSol = copy.deepcopy(sol)
        return mejorSol, solucionesPosibles

    # No incluir al candidato actual
    mejorSol, solucionesPosibles = mochila(d, sol, mejorSol, solucionesPosibles, idx + 1)

    # Incluir al candidato actual si es factible
    if esFactible(d, sol, idx):
        sol['totalBeneficio'] += d['beneficios'][idx]
        sol['totalCoste'] += d['costes'][idx]
        sol['candidatos'].append(d['nombres'][idx])
        sol['diferenciaContratar'].append(d['beneficios'][idx] - d['costes'][idx])

        mejorSol, solucionesPosibles = mochila(d, sol, mejorSol, solucionesPosibles, idx + 1)

        sol['totalBeneficio'] -= d['beneficios'][idx]
        sol['totalCoste'] -= d['costes'][idx]
        sol['candidatos'].remove(d['nombres'][idx])
        sol['diferenciaContratar'].remove(d['beneficios'][idx] - d['costes'][idx])

    return mejorSol, solucionesPosibles


# Lectura de datos
nCandidatos, nPresupuesto = map(int, input().strip().split())
nombres = []
beneficios = []
costes = []

for i in range(nCandidatos):
    entrada = input().strip().split()
    nombre = entrada[0]
    beneficio, coste = map(int, entrada[1:])
    nombres.append(nombre)
    beneficios.append(beneficio)
    costes.append(coste)

data = {
    'nombres': nombres,
    'beneficios': beneficios,
    'costes': costes,
    'presupuesto': nPresupuesto,
    'numCandidatos': nCandidatos
}

sol = inicializarSolucion()
mejorSol = inicializarSolucion()

solFinal, numSoluciones = mochila(data, sol, mejorSol, 0, 0)

# Imprimir resultados
print(solFinal['totalBeneficio'], numSoluciones)
for i in range(len(solFinal['candidatos'])):
    print(solFinal['candidatos'][i], solFinal['diferenciaContratar'][i])
