import networkx as nx
import json
import matplotlib.pyplot as plt
# Use of any function from networkx.algorithms module is strictly not allowed.
# Matplotlib can be used for visualization purposes

# Add your functions here if needed
def read_json(json_file): #Read the json file
    f = open(json_file,)
    data = json.load(f)
    return data
    

def construct_metabolic_graph(name_of_json_file):
    """
    Given the reaction dict, return the metabolic directed bi-partite networkx graph
    """
    pass
    data = read_json(name_of_json_file)
    plt.figure(figsize = (30,30))
    DG = nx.DiGraph()
    reactions = [x['name'] for x in data['reactions']]

    for i in data['reactions']:
        DG.add_node(i['name']) #Adding the enzymes as the nodes
        d = i['metabolites']
        for p in d.keys():
            if(d[p]<0): #Extracting the reactants
                if(p not in DG.nodes()):
                    DG.add_node(p) #Adding the reactants as the nodes
                DG.add_edge(p,i['name']) #Adding an edge from reactants to enzymes
            else: #Extracting the reactants
                if(p not in DG.nodes()):
                    DG.add_node(p) #Adding the products as the nodes
                DG.add_edge(i['name'],p) #Adding an edge from products to enzymes

    cmap = ['red' if node in reactions else 'blue' for node in DG] #Adding a coloring rule for the bipartite graph
#     nx.draw(DG, with_labels=True, node_color = cmap)
#     plt.show()
    return DG

def Find_Cycles_In_Metabolic_Graph(Graph):
    """
    Given a bi-partite networkx graph, return the list of list of metabolites involved in the cycle i.
    """
    pass
    data = read_json('e_coli_core.json')
    DG = construct_metabolic_graph('e_coli_core.json')
    enzymes = [x['name'] for x in data['reactions']]
    def DFS(node,p): #Implementing DFS
    
        if p[-1]==source:
            cyclic.append(p)
        if state[node]==0:
            return
        state[node] = state[node] - 1
        for n in DG.neighbors(node):
            DFS(n,p+[n])
    cycles= []
    for i in DG: #Checking for cycles
        cyclic = []
        source = i
        state = {node : len(list(DG.predecessors(node))) for node in DG} #Store the number of incident edges of each node in the graph
        DFS(source,[source])
        p = []
        for elements in cyclic:
            for i in elements:
                if(len(elements))>1: #If cycle is found, add it to the list
                    if(i not in enzymes): #Remove the enzyme names from the list of reactions present in the cycles list
                        p.append(i)
            if(len(p)>1):
                cycles.append(p)
            p = []
    return cycles
    



# For the purpose of parsing, look under "metabolites" sub-section of "reaction" section. The stoichiometric coefficients will help you in determining if a metabolite is a reactant or a product.
G = construct_metabolic_graph("e_coli_core.json")
# Add code to visualized G below
data = read_json('e_coli_core.json')
reactions = [x['name'] for x in data['reactions']]
cmap = ['red' if node in reactions else 'blue' for node in G] #Adding a coloring rule for the bipartite graph
nx.draw(G, with_labels = True, node_color = cmap) 
plt.show()

cycles = Find_Cycles_In_Metabolic_Graph(G)
print(cycles)