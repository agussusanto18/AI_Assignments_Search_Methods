from algo_dfs import dfs

def dfs(graph, current, goal, depth, visited):
    if depth == 0 and current == goal:
        return [current]
    if depth > 0:
        visited.append(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                result = dfs(graph, neighbor, goal, depth - 1, visited)
                if result is not None:
                    return [current] + result
        visited.pop()
    return None

# Function for ID-DFS search
def iddfs(graph, start, goal):
    for depth in range(len(graph)):
        result = dfs(graph, start, goal, depth, [])
        if result:
            return result
    return None