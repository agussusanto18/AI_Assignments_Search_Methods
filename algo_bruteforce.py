# Function for undirected (blind) brute-force approach
def brute_force(graph, start, goal):
    def recursive_dfs(current, path):
        if current == goal:
            return path
        for neighbor in graph[current]:
            if neighbor not in path:
                result = recursive_dfs(neighbor, path + [neighbor])
                if result:
                    return result
        return None

    return recursive_dfs(start, [start])
