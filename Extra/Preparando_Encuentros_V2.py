import copy


def inicializarSolucion():
    sol = {'candidatos': [], 'diferenciaContratar': [], 'totalBeneficio': 0}
    return sol


def esSolucion(sol, presupuesto):
    return sol['totalBeneficio'] > 0 and sol['totalBeneficio'] <= presupuesto


def esMejorSolucion(sol, mejorSol):
    return sol['totalBeneficio'] > mejorSol['totalBeneficio']


def esFactible(d, sol, pos):
    return d['beneficios'][pos] + sol['totalBeneficio'] <= d['presupuesto']


def mochila(d, sol, mejorSol, solucionesPosibles):
    if esSolucion(sol, d['presupuesto']):
        solucionesPosibles += 1
        if esMejorSolucion(sol, mejorSol):
            mejorSol = copy.deepcopy(sol)
            print(mejorSol)
    else:
        for i in range(d['numCandidatos']):
            if esFactible(d, sol, i):
                nuevaSol = copy.deepcopy(sol)
                nuevaSol['totalBeneficio'] += d['beneficios'][i]
                nuevaSol['candidatos'].append(d['nombres'][i])
                nuevaSol['diferenciaContratar'].append(d['beneficios'][i] - d['costes'][i])
                print(nuevaSol, d['beneficios'][i])

                mejorSol, solucionesPosibles = mochila(d, nuevaSol, mejorSol, solucionesPosibles)

    return mejorSol, solucionesPosibles


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

solFinal, numSoluciones = mochila(data, sol, mejorSol, 0)
print(solFinal)
print(f'Número de soluciones posibles: {numSoluciones}')
