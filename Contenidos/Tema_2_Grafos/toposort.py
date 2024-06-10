from collections import deque

def topSortVisit(data, k):
    data["state"][k] = "VISITED"
    data["time"] = data["time"] + 1
    data["d"][k] = data["time"]
    for adj in data["graph"][k]:
        if data["state"][adj] == "NOT VISITED":
            topSortVisit(data, adj)
    data["state"][k] = "FINISH"
    data["time"] = data["time"] + 1
    data["f"][k] = data["time"]
    data["list"].appendleft(k)

def topsort(g):
    n = len(g)
    data = {
        "graph": g,
        "state": dict(),
        "d": dict(),
        "f": dict(),
        "time": 0,
        "list": deque()
    }

    for k in g.keys():
        data["state"][k] = "NOT VISITED"
        data["d"][k] = 0
        data["f"][k] = 0

    for k in g.keys():
        if data["state"][k] == "NOT VISITED":
            topSortVisit(data, k)

    print(data["list"])


g1 = dict()

g1 = {
    "calcetines": ["zapatos"],
    "pantalon": ["zapatos", "cinturon"],
    "camisa": ["cinturon", "jersey"],
    "zapatos": [],
    "cinturon": [],
    "jersey": []
}

g = {
    "0": [],
    "1": [],
    "2": ["3"],
    "3": ["1"],
    "4": ["0", "1"],
    "5": ["0", "2"]
}


topsort(g1)


#calcetines ->1
#pantalon -> 2
#camisa-> 3
#zapatos -> 4
#cinturon ->5
#jersey ->6

grafo = [
    [],
    [],
    [3],
    [1],
    [0,1],
    [0,2]
]


