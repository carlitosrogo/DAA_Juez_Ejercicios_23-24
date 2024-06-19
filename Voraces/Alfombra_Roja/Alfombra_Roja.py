
def getBestFam(data, f):
    if data["Name"][f] in data["Entrevistado"]:
        for j in range(len(data["Name"])):
            if data["Name"][j] not in data["Entrevistado"]:
                f = j
                break
    for i in range(len(data["Name"])):
        if data["Name"][i] not in data["Entrevistado"] and i != f:
            if data["Fama"][f]/data["Amabilidad"][f] < data["Fama"][i]/data["Amabilidad"][i]:
                return i
    return f
def greedy(data):
    currentFamoso = 0
    while len(data["Name"]) != len(data["Entrevistado"]):
        bestFam = getBestFam(data, currentFamoso)
        currentFamoso = bestFam
        data["Entrevistado"].add(data["Name"][bestFam])
        if data["Name"][bestFam] != data["AbecedarioFam"] and data["AbecedarioFam"] not in data["Entrevistado"]:
            data["TimpoTotal"] += data["Tiempo"][bestFam]
        print(data["Name"][bestFam])
    return data["TimpoTotal"]

numFamosos = int(input())
data = {
    "Name" : [[] for _ in range(numFamosos)],
    "Amabilidad" : [[] for _ in range(numFamosos)],
    "Fama" : [[] for _ in range(numFamosos)],
    "Tiempo" : [[] for _ in range(numFamosos)],
    "Entrevistado" : set(),
    "AbecedarioFam" : str,
    "TimpoTotal" : 0
}
for i in range(numFamosos):
    inLine = input().strip().split()
    data["Name"][i] = inLine[0]
    data["Amabilidad"][i], data["Fama"][i],data["Tiempo"][i] = map(int, inLine[1:])

auxList = data["Name"].copy()
auxList.sort()
data["AbecedarioFam"] = auxList[0]

print("Data: ", data)

totalTime = greedy(data)
print(totalTime)