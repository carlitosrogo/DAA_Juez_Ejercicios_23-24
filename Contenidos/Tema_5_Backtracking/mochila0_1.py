import copy


def inicializarDatos():
    datos = {}
    datos['N'] = 4
    datos['W'] = 8
    datos['Peso'] = [2, 3, 4, 5]
    datos['Valor'] = [3, 5, 6, 10]
    return datos

def inicializarSolucion(datos):
    sol = {}
    sol['Objetos'] = [0] * datos['N']
    sol['Peso'] = 0
    sol['Valor'] = 0
    return sol

def esSolucion(sol, datos):
    return sol['Peso'] + min(datos['Peso']) > datos['W']

#def esSolucion(k, datos):
    #return k == datos['N']
#def esSolucion(k, sol):
#    return k == len(sol['Objetos'] - 1)

def esFactible(sol, datos, i):
    return sol['Peso'] + datos['Peso'][i] <= datos ['W']

def asignar(sol, i, datos):
    sol['Objetos'][i] = 1
    sol['Valor'] += datos['Valor'][i]
    sol['Peso'] += datos['Peso'][i]
    return sol

def borrar(sol, i, datos):
    sol['Objetos'][i] = 0
    sol['Valor'] -= datos['Valor'][i]
    sol['Peso'] -= datos['Peso'][i]
    return sol


def mochilaVA(sol, mejorSol, datos, k):
    if esSolucion(sol, datos):
        if sol['Valor'] > mejorSol['Valor']:
            mejorSol = copy.deepcopy(sol)
    else:
        for i in range(k, datos['N']):
            if esFactible(sol,datos, i):
                sol = asignar(sol, i, datos)
                mejorSol = mochilaVA(sol, mejorSol, datos, i+1)
                sol = borrar(sol, i, datos)
    return mejorSol

#Prog. Principal

datos = inicializarDatos()
sol = inicializarSolucion(datos)
mejorSol = inicializarSolucion(datos)
k = 0
mejorSol = mochilaVA(sol, mejorSol, datos, k)
print(mejorSol)
