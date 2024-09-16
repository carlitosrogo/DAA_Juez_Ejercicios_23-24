import heapq


def dijkstra(g, origin):
    n = len(g)
    distances = [float('inf')] * n
    distances[origin] = 0
    priority_queue = [(0, origin)]

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if current_dist > distances[u]:
            continue

        for adjNode, weight in g[u]:
            distance = current_dist + weight

            if distance < distances[adjNode]:
                distances[adjNode] = distance
                heapq.heappush(priority_queue, (distance, adjNode))

    return distances


numRooms, numDoors, maxTime = map(int, input().strip().split())
adjList = [[] for _ in range(numRooms)]
for _ in range(numDoors):
    h1, h2, d = map(int, input().strip().split())
    adjList[h1].append((h2, d))
    adjList[h2].append((h1, d))  # Añadimos la conexión en ambos sentidos

distances = dijkstra(adjList, 0)
total_time = sum(dist for dist in distances if dist < float('inf'))

if all(dist < float('inf') for dist in distances) and total_time <= maxTime:
    print(total_time)
else:
    print("Aleg, ¡adecorar!")
