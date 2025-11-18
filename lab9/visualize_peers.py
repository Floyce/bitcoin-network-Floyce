import json
import networkx as nx
import matplotlib.pyplot as plt

# Load peer info from JSON file (already saved from getpeerinfo)
with open('lab9/peer_info.json') as f:
    peers = json.load(f)

# Create a graph
G = nx.Graph()

# Add nodes (your local node + peers)
G.add_node("local_node")
for peer in peers:
    addr = peer['addr']
    G.add_node(addr)
    # Connect each peer to local node
    G.add_edge("local_node", addr)

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, k=0.5)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, edge_color='gray')
plt.title("Bitcoin Regtest Peer Network")
plt.savefig('lab9/peer_network.png')
plt.show()
