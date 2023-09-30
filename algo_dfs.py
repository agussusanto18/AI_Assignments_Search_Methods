# Function for depth-first search
def dfs(graph, start, goal):
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None