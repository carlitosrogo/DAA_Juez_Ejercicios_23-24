def dfsPath(node, graph, visited):
    visited.add(node)
    for ady in graph[node]:
        if ady not in visited:
            dfsPath(ady, graph, visited)

def dfs (g):
    n = len(g - 1)
    pila = [0]
    visited = set()
    for v in range(1, n + 1):
        if not v in visited:
            dfsPath(v,g,visited)

