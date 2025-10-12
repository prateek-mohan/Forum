from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
