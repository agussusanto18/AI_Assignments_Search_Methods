from coordinates import coordinates
from utils import haversine

# Function for A* search using straight-line distance heuristic
def astar_search(graph, start, goal):
    came_from = {}
    
    open_set = [(0, start)]
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = haversine(coordinates[start], coordinates[goal])

    while open_set:
        open_set.sort()
        _, current = open_set.pop(0)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + haversine(coordinates[current], coordinates[neighbor])
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + haversine(coordinates[neighbor], coordinates[goal])
                open_set.append((f_score[neighbor], neighbor))
    return None
