
def getBestItem(data, candidates):
    bestProfit = -1
    bestItem = -1

    for c in candidates:
        profit = data['profit'][c]
        if profit > bestProfit:
            bestProfit = profit
            bestItem = c
    return bestItem

def greedySchedule(data):
    n = len(data['profit'])
    candidates = set()
    for i in range(n):
        candidates.add(i)
    schedule = [-1] * n
    #Llevarlo a un isSol
    lastDate = max(data['deadLine'])
    ####
    j = 0
    while j <= lastDate and candidates:
        bestItem = getBestItem(data, candidates)
        candidates.remove(bestItem)
        i = data['deadLine'][bestItem]
        ###isFeasible
        found = False
        while i >=0 and not found:
            if schedule[i] == -1:
                schedule[i] = bestItem
                found = True
            i -= 1
        j += 1
    return schedule




#Schedule

data = {
    'profit' : [50, 10, 15, 30],
    'deadLine' : [2,1,2,1]
}

schedule = greedySchedule(data)
print(schedule)