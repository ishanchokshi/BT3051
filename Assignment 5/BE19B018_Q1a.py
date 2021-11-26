import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue
# Use of any function from networkx.algorithms module is strictly not allowed.
# Other libraries are not allowed expect for matplotlib for visualization purposes

# Add your functions here if needed
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

def minimum_time_for_spread_of_contagion(G, patient_zero):
    """
    Given an connected undirected weighted networkx graph which represents the physical contant graph of a community and a node which represents patient zero of the contagion, return the minimum time taken for the contagion to spread in the complete graph.
    """
    pass
    time_taken = dijkstra(G,patient_zero)
    return time_taken

G = nx.Graph()
G.add_edge(1,2,weight = 2); G.add_edge(3,2,weight = 3); G.add_edge(3,1,weight = 2)
G.add_edge(3,4,weight = 1); G.add_edge(4,5,weight =3); G.add_edge(5,6,weight =4)
G.add_edge(7,6,weight =7); G.add_edge(5,8,weight =2); G.add_edge(7,8,weight =6)

print(minimum_time_for_spread_of_contagion(G, 3))
# Expected output: 12
# Explanation: 
# Infected node | Time taken to reach that node
#      3        |  0
#      4        |  1
#      1        |  2
#      2        |  3
#      5        |  4 (1+3)
#      8        |  6 (1+3+2)
#      7        |  12(1+3+2+6)

# Hint:
# Therefore, minimum time taken to spread in the community = argmax_i(min(time taken to reach node i from patient zero node))
# Mininum time taken to reach node i from patient zero node can be thought of as a dynamic programming question. 
# Time taken to reach node i from node j can be thought of as a dynamic programming question. 
# To find the shortest path/minimum time taken for the person to be infected you can either use Dijkstra's algorithm or a dynamic programming variant of Dijkstra's algorithm i.e. Floyd-Warshall algorithm for all pairs of shortest paths

# """Pseudocode for Floyd-Warshall algorithm
# let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
# for each edge (u, v) do
#     dist[u][v] ← w(u, v)  // The weight of the edge (u, v)
# for each vertex v do
#     dist[v][v] ← 0
# for k from 1 to |V|
#     for i from 1 to |V|
#         for j from 1 to |V|
#             if dist[i][j] > dist[i][k] + dist[k][j] 
#                 dist[i][j] ← dist[i][k] + dist[k][j]
#             end if
# """