import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from algo_bfs import bfs
from algo_dfs import dfs
from algo_befs import best_first_search
from algo_iddfs import iddfs
from algo_astar import astar_search
from algo_bruteforce import brute_force
from utils import haversine, read_file, show_graph, read_coordinates

# adjacency = adjacency_list
adjacency = read_file('assets/Adjacencies.txt')
coordinates = read_coordinates('assets/coordinates.csv')
node_colors = {node: 'grey' for node in adjacency}


# Function to perform the search and display the result
def perform_search():
    start_town = start_town_entry_var.get()
    end_town = end_town_entry_var.get()

    if start_town not in coordinates or end_town not in coordinates:
        messagebox.showerror("Invalid Input", "Invalid town names. Please enter valid towns.")
        return

    search_method = search_method_var.get()

    start_time = time.time()

    if search_method == "BFS":
        result = bfs(adjacency, start_town, end_town)
    elif search_method == "DFS":
        result = dfs(adjacency, start_town, end_town)
    elif search_method == "Best-First":
        visited = best_first_search(adjacency, start_town, end_town)
        result = [start_town] + list(visited) if visited else None
    elif search_method == "ID-DFS":
        result = iddfs(adjacency, start_town, end_town)
    elif search_method == "A*":
        result = astar_search(adjacency, start_town, end_town)
    elif search_method == "Brute-Force":
        result = brute_force(adjacency, start_town, end_town)
    else:
        messagebox.showerror("Invalid Input", "Invalid search method. Please select a valid method.")
        return

    if result:
        route_label.config(text="Route: " + ' -> '.join(result))
        total_distance_label.config(text="Total Distance (node to node): {:.2f} km".format(
            sum(haversine(coordinates[result[i]], coordinates[result[i + 1]]) for i in range(len(result) - 1))))
        time_taken_label.config(text="Time taken: " + str(time.time() - start_time) + "seconds")

        show_graph(adjacency, node_colors, result)
    else:
        route_label.config(text="No route found.")
        total_distance_label.config(text="")
        time_taken_label.config(text="Time taken: {:.2f} seconds".format(time.time() - start_time))

# Create a Tkinter window
root = Tk()
root.title("Route Search")

# Create and pack GUI elements
start_town_label = Label(root, text="Enter starting town:")
start_town_label.pack()

start_town_entries = [key for key, val in adjacency.items()]
start_town_entry_var = StringVar()
start_town_entry_var.set(start_town_entries[0])
start_town_entry_option = OptionMenu(root, start_town_entry_var, *start_town_entries)
start_town_entry_option.config(width=30)
start_town_entry_option.pack()

end_town_label = Label(root, text="Enter ending town:")
end_town_label.pack()

end_town_entries = [key for key, val in adjacency.items()]
end_town_entry_var = StringVar()
end_town_entry_var.set(end_town_entries[0])
end_town_entry_option = OptionMenu(root, end_town_entry_var, *end_town_entries)
end_town_entry_option.config(width=30)
end_town_entry_option.pack()

search_method_label = Label(root, text="Select a search method:")
search_method_label.pack()

search_methods = ["BFS", "DFS", "Best-First", "ID-DFS", "A*", "Brute-Force"]
search_method_var = StringVar()
search_method_var.set(search_methods[0])
search_method_option = OptionMenu(root, search_method_var, *search_methods)
search_method_option.config(width=30)
search_method_option.pack()

search_button = Button(root, text="Search", command=perform_search)
search_button.pack()

route_label = Label(root, text="")
route_label.pack()

total_distance_label = Label(root, text="")
total_distance_label.pack()

time_taken_label = Label(root, text="")
time_taken_label.pack()

# Start the Tkinter main loop
root.mainloop()
