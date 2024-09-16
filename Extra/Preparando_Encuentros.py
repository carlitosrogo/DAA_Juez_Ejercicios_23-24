import copy

numCandidatosExplorados = 0


def inicializarSolucion():
    sol = {'candidatos': [], 'diferenciaContratar': [], 'totalBeneficio': 0}
    return sol


def esSolucion(sol, presupuesto):
    if sol['totalBeneficio'] > 0 and sol['totalBeneficio'] <= presupuesto and not len(sol['candidatos']) % 2:
        return True
    return False


def esMejorSolucion(sol, mejorSol):
    if sol['totalBeneficio'] > mejorSol['totalBeneficio']:
        return True
    return False


def esFactible(d, sol, pos):
    if d['beneficios'][pos] + sol['totalBeneficio'] <= d['presupuesto']:
        return True
    return False


def mochila(d, sol, mejorSol):
    global numCandidatosExplorados
    if esSolucion(sol, d['presupuesto']):
        if esMejorSolucion(sol, mejorSol):
            mejorSol = copy.deepcopy(sol)
            numCandidatosExplorados += 1
    else:
        for i in range(d['numCandidatos']):
            if esFactible(d, sol, i):
                sol['totalBeneficio'] += d['beneficios'][i]
                sol['candidatos'].append(d['nombres'][i])
                sol['diferenciaContratar'].append(d['beneficios'][i] - d['costes'][i])

                mejorSol = mochila(d, sol, mejorSol)

                sol['totalBeneficio'] -= d['beneficios'][i]
                sol['candidatos'].remove(d['nombres'][i])
                sol['diferenciaContratar'].remove(d['beneficios'][i] - d['costes'][i])

    return mejorSol


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
data = {}
data['nombres'] = nombres
data['beneficios'] = beneficios
data['costes'] = costes
data['presupuesto'] = nPresupuesto
data['numCandidatos'] = nCandidatos

sol = inicializarSolucion()
mejorSol = inicializarSolucion()

solFinal = mochila(data, sol, mejorSol)

candidatos_con_diferencias = list(zip(solFinal['candidatos'], solFinal['diferenciaContratar']))
candidatos_con_diferencias.sort(key=lambda x: x[1], reverse=True)
print(solFinal['totalBeneficio'], numCandidatosExplorados)
for nombre, diferencia in candidatos_con_diferencias:
    print(nombre, diferencia)
