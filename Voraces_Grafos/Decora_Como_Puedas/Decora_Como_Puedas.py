def sortRooms(g):
    rooms = []
    for node in g:
        for adj, timeTo in node:
            rooms.append((timeTo,adj))
    rooms.sort()
    return rooms
def roomUpdate(rooms, newRoom, lastRoom):
    for i in range(1, len(rooms)):
        if rooms[i] == lastRoom:
            rooms[i] = newRoom
def kruskal(g):
    roomsList = sortRooms(g)
    rooms = list(range(len(g)))
    count = len(rooms) -1
    i = 0
    sol = 0
    while count > 1 and len(rooms) > i:
        timeRoom, room = roomsList[i]
        print(rooms)
        print(roomsList[i])
        print(rooms[i], rooms[room])
        if rooms[i] != rooms[room]:
            sol += timeRoom
            count -= 1
            roomUpdate(rooms, rooms[i], rooms[room])
        i += 1
    print(rooms)
    return sol


numRooms, numDoors, maxTime = map(int, input().strip().split())
adjList = [[] for _ in range(numRooms)]
for _ in range(numDoors):
    h1,h2,d = map(int, input().strip().split())
    adjList[h1].append((h2,d))

print(adjList)
total = kruskal(adjList)
if total <= maxTime:
    print(total)
else:
    print("Aleg, ¡adecorar!")