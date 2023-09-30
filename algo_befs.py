from coordinates import coordinates
from utils import haversine

# Function for best-first search using straight-line distance heuristic
def best_first_search(graph, start, goal):
    visited = set()
    queue = [(0, start)]
    while queue:
        queue.sort()
        cost, node = queue.pop(0)
        if node == goal:
            return visited
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    h = haversine(coordinates[node], coordinates[neighbor])
                    queue.append((h, neighbor))
    return None
