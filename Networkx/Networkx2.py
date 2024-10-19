import networkx as nx
import matplotlib.pyplot as plt
# G=nx.gnp_random_graph(50,0.3)
G=nx.barabasi_albert_graph(50,2) #new nodes attach to nodes having higher degree
nx.draw(G)
plt.show()
nx.write_gexf(G,'analysis1.gexf')