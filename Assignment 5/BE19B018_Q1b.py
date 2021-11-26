import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue
# Use of any function from networkx.algorithms module is strictly not allowed.
# Other libraries are not allowed expect for matplotlib for visualization purposes

# Add your functions here if needed
# You are allowed to use the function that you used in the previous subquestion

def dijkstra(G, start_node):
    """
    Function which will calculate the the minimum time taken for the infection to spread in the whole community
    """
    n_nodes = len(G.nodes())
    paths = {v:float('inf') for v in G.nodes()} #Initializing the value of all nodes as infinity
    paths[start_node] = 0 #Initialize the value of node 3 to zero since it is the source
    pqueue = PriorityQueue() #Create a priority queue to store the neighbors
    pqueue.put((0, start_node)) #Add the starting node to the priority queue
    visited = [] #Create a list to store the nodes which are already visited
    while not pqueue.empty():
        (dist, current_node) = pqueue.get() #Get the next node based on the weight (priority)
        visited.append(current_node) #Mark the current node as visited
        for neighbor in G.neighbors(current_node):
            distance = G[current_node][neighbor]['weight'] #Get the edge weight
            if neighbor not in visited:
                old_distance = paths[neighbor]
                new_distance = paths[current_node] + distance
                if new_distance < old_distance: #Replacing the value of the weight; if the new value is less than the old value
                    pqueue.put((new_distance, neighbor)) #Add the valeue of the weight to the priority queue
                    paths[neighbor] = new_distance
    max_key = max(paths, key=paths.get)
    return paths[max_key]

def most_critical_node_for_contagion(G):
    """
    Given an connected undirected weighted networkx graph which represents the physical contant graph of a community, return the most critical node. The infection of the most critical node will result in minimum time for the spread in the whole community.
    """
    pass
    infection_time = [] #list to store the 
    node_list = []
    for i in G.nodes(): #Iterate through all the nodes considering them as starting vertex in every iteration
        time_taken = dijkstra(G,i)
        infection_time.append(time_taken) #Store the time taken for every iteration
        node_list.append(i) #Store the corresponding starting node
    min_time_index = infection_time.index(min(infection_time)) #Get the index of the least time
    return node_list[min_time_index]

G = nx.Graph()
G.add_edge(1,2,weight = 2); G.add_edge(3,2,weight = 3); G.add_edge(3,1,weight = 2)
G.add_edge(3,4,weight = 1); G.add_edge(4,5,weight =3); G.add_edge(5,6,weight =4)
G.add_edge(7,6,weight =7); G.add_edge(5,8,weight =2); G.add_edge(7,8,weight =6)

print(most_critical_node_for_contagion(G))
# Expected output: 5
# Explanation: 
# Patient zero node | minimum time taken
#      1            |  15
#      2            |  16
#      3            |  12
#      4            |  11
#      5            |  8 - minimum time
#      6            |  12
#      7            |  15