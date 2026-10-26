import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

network_data = pd.read_csv("network.csv", header = None)
print(network_data) 

#Converts Pandas Dataframe into Networkx graph 
#edgelist refers to creating an edge list, specifying node edges
#2nd & 3nd parameters for source node column and target node column
#Defaultly creates nx.Graph, create_using argument can change graph type
network_graph = nx.from_pandas_edgelist(network_data,0,1,create_using= nx.DiGraph)
print("Number of Edges:", network_graph.edges())
#print(list(network_graph.neighbors(1)))

nx.draw(network_graph, with_labels=True)
plt.show()