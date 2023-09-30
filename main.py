import time
from coordinates import coordinates
from algo_bfs import bfs
from algo_dfs import dfs
from algo_befs import best_first_search
from algo_iddfs import iddfs
from algo_astar import astar_search
from algo_bruteforce import brute_force
from utils import haversine, read_file, show_graph

# adjacency = adjacency_list
adjacency = read_file('assets/Adjacencies.txt')
node_colors = {node: 'grey' for node in adjacency}

# Main program
while True:
    start_town = input("Enter starting town: ")
    end_town = input("Enter ending town: ")

    if start_town not in coordinates or end_town not in coordinates:
        print("Invalid town names. Please enter valid towns.")
        continue

    search_method = input("Select a search method (1. BFS, 2. DFS, 3. Best-First, 4. ID-DFS, 5. A*, 6. Brute-Force): ")

    start_time = time.time()

    if search_method == "1":
        result = bfs(adjacency, start_town, end_town)
    elif search_method == "2":
        result = dfs(adjacency, start_town, end_town)
    elif search_method == "3":
        visited = best_first_search(adjacency, start_town, end_town)
        result = [start_town] + list(visited) if visited else None
    elif search_method == "4":
        result = iddfs(adjacency, start_town, end_town)
    elif search_method == "5":
        result = astar_search(adjacency, start_town, end_town)
    elif search_method == "6":
        result = brute_force(adjacency, start_town, end_town)
    else:
        print("Invalid search method. Please select a valid method.")
        continue

    if result:
        print("Route:", ' -> '.join(result))
        print("Total Distance (node to node):", sum(haversine(coordinates[result[i]], coordinates[result[i+1]]) for i in range(len(result) - 1)), "km")
        print("Time taken:", time.time() - start_time, "seconds")
        
        show_graph(adjacency, node_colors, result)
    else:
        print("No route found.")
        print("Time taken:", time.time() - start_time, "seconds")

    another_search = input("Do you want to perform another search? (yes/no): ")
    if another_search.lower() != "yes":
        break
