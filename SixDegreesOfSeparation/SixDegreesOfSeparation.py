import networkx as nx
import numpy as np
G=nx.read_edgelist('facebook_combined.txt')
N=list(G.nodes())
spll=[] #shortest path length list
for u in N:
    for v in N:
        if(u!=v):
            l=nx.shortest_path_length(G,u,v)
            print(f"Shortest path between {u} and {v} is of length {l}")
            spll.append(l)
min_spl=min(spll)
max_spl=max(spll)
avg_spl=np.average(spll)
print(f"Minimum shortest path length:{min_spl}\nMaximum shortest path length:{max_spl}\nAverage shortest path length:{avg_spl}")