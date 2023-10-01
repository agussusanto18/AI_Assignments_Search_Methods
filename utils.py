import math
import networkx as nx
import matplotlib.pyplot as plt


# Function to calculate distance between two coordinates using Haversine formula
def haversine(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Radius of the Earth in km
    R = 6371
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (pow(math.sin(math.radians(dlat) / 2), 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         pow(math.sin(math.radians(dlon) / 2), 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def read_file(filename):
     adjacency_list = {}

     with open(filename, 'r') as file:
          for line in file:
               node1, node2 = line.strip().split()

               if node1 in adjacency_list:
                    adjacency_list[node1].append(node2)
               else:
                    adjacency_list[node1] = [node2]

               if node2 in adjacency_list:
                    adjacency_list[node2].append(node1)
               else:
                    adjacency_list[node2] = [node1]

     return adjacency_list

def read_coordinates(filename):
     coordinates = {}

     with open(filename, 'r') as file:
          for line in file:
               city, latitude, longitude = line.strip().split(',')
               coordinates[city] = [float(latitude.strip()), float(longitude.strip())]

     return coordinates


def show_graph(adjacency_list, node_colors, route_nodes):

     # # Change the node color for every visited node
     for i, route_node in enumerate(route_nodes):
          if i == 0:
               node_colors[route_node] = 'green'
          elif i == len(route_nodes) - 1:
               node_colors[route_node] = 'orange'
          else:
               node_colors[route_node] = 'red'

     # Change the edge color for every single pair node
     edge_colors = {}
     for i, route_node in enumerate(route_nodes):
          if i < len(route_nodes) - 1:
               edge_colors[(route_node, route_nodes[i + 1])] = 'red'

     G = nx.DiGraph()
     for node, neighbors in adjacency_list.items():
          G.add_node(node)
          for neighbor in neighbors:
               G.add_edge(node, neighbor)

     # Plot the graph using Kamada-Kawai layout
     plt.figure(figsize=(12, 8))

     plt.subplot(122)
     pos = nx.kamada_kawai_layout(G)
     nx.draw(
          G, 
          pos, 
          with_labels=True, 
          node_size=500, 
          font_size=4, 
          font_color='white', 
          node_color=[node_colors[node] for node in G.nodes()],
          edge_color=[edge_colors.get(edge, 'black') for edge in G.edges()])

     plt.tight_layout()
     plt.show()