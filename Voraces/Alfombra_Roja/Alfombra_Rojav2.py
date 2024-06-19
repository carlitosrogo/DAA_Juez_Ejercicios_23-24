import heapq


def getBestFam(data):
    # Crear una lista de prioridades basada en la relación fama/amabilidad
    heap = []
    for i in range(len(data["Name"])):
        if data["Name"][i] not in data["Entrevistado"]:
            ratio = data["Fama"][i] / data["Amabilidad"][i]
            heapq.heappush(heap, (-ratio, i))  # Usamos un heap negativo para obtener el máximo
    return heap


def greedy(data):
    heap = getBestFam(data)

    while heap:
        # Obtener el siguiente famoso a entrevistar
        _, bestFam = heapq.heappop(heap)
        data["Entrevistado"].add(data["Name"][bestFam])

        if data["Name"][bestFam] != data["AbecedarioFam"] and data["AbecedarioFam"] not in data["Entrevistado"]:
            data["TiempoTotal"] += data["Tiempo"][bestFam]

        print(data["Name"][bestFam])

        # Actualizar el heap para la siguiente iteración
        heap = getBestFam(data)

    return data["TiempoTotal"]


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
