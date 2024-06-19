def greedy(data):
    # Calcular la prioridad (fama/amabilidad) y ordenar al principio
    famosos = [(data["Fama"][i] / data["Amabilidad"][i], data["Name"][i], data["Tiempo"][i], i) for i in
               range(len(data["Name"]))]
    famosos.sort(reverse=True, key=lambda x: x[0])  # Ordenar por prioridad de mayor a menor

    totalTime = 0
    abecedarioFamIndex = data["Name"].index(data["AbecedarioFam"])

    for priority, name, tiempo, i in famosos:
        if name not in data["Entrevistado"]:
            data["Entrevistado"].add(name)
            if name != data["AbecedarioFam"] and data["AbecedarioFam"] not in data["Entrevistado"]:
                totalTime += tiempo
            print(name)

    return totalTime


# Inicialización de datos
numFamosos = int(input())
data = {
    "Name": ["" for _ in range(numFamosos)],
    "Amabilidad": [0 for _ in range(numFamosos)],
    "Fama": [0 for _ in range(numFamosos)],
    "Tiempo": [0 for _ in range(numFamosos)],
    "Entrevistado": set(),
    "AbecedarioFam": "",
    "TiempoTotal": 0
}

# Lectura de datos
for i in range(numFamosos):
    inLine = input().strip().split()
    data["Name"][i] = inLine[0]
    data["Amabilidad"][i], data["Fama"][i], data["Tiempo"][i] = map(int, inLine[1:])

# Determinar el primer famoso en orden alfabético
auxList = data["Name"].copy()
auxList.sort()
data["AbecedarioFam"] = auxList[0]

# Ejecutar el algoritmo greedy
totalTime = greedy(data)
print(totalTime)
