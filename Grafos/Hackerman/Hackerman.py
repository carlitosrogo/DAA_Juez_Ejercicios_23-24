from collections import deque

def bsf(v,data):
    q = deque()
    data["visited"][v] = True
    q.append(v)
    while q:
        v = q.popleft()
        critico = 0
        for j in range(len(data["grafo"])):
            if v in data["grafo"][j] and not (set(data["grafo"][j]) & set(data["grafo"][v])):
                critico +=1
            if critico >= 1:
                data["totalCoste"]+= data["costes"][v]
                break
        for adj in data["grafo"][v]:
            if not data["visited"][adj]:
                data["visited"][adj] = True
                q.append(adj)

def topSport(g,c):
    visited = [False for _ in range(len(g))]
    data = {
        "grafo" : g,
        "costes" : c,
        "totalCoste" : 0,
        "visited" : visited,
    }
    for i in range(len(g)):
        if not data["visited"][i]:
            bsf(i,data)
    return data["totalCoste"]


numNodes, numConections = map(int, input().strip().split())
adjacencyList = [[] for _ in range(numNodes)]
costList = list()

for _ in range(numNodes):
    costList.append(int(input()))

for _ in range(numConections):
    node1, node2 = map(int, input().strip().split())
    adjacencyList[node1].append(node2)
    adjacencyList[node2].append(node1)

totalCoste = topSport(adjacencyList,costList)
print(totalCoste)