import networkx as nx
import matplotlib.pyplot as plt

def format_label(number):
    s = str(number)
    return f"{s[:-1]}0" if s.endswith("0") else s

def generate_bipartite_graph(n):
    G = nx.Graph()
    left_nodes = [f"L{i}" for i in range(n)]
    right_nodes = [f"R{i}" for i in range(n)]
    G.add_nodes_from(left_nodes, bipartite=0)
    G.add_nodes_from(right_nodes, bipartite=1)
    for i in range(n):
        for j in range(1, n):
            G.add_edge(left_nodes[i], right_nodes[(i + j) % n])
    return G, left_nodes, right_nodes

def assign_weights(G, left_nodes, right_nodes, weights):
    for i in range(len(weights)):
        G.nodes[left_nodes[i]]['weight'] = weights[i]
        G.nodes[right_nodes[i]]['weight'] = weights[i]

def get_positions(left_nodes, right_nodes):
    pos = {}
    for i, node in enumerate(left_nodes):
        pos[node] = (0, -i)
    for i, node in enumerate(right_nodes):
        pos[node] = (1, -i)
    return pos

def draw_bipartite_graph(G, left_nodes, right_nodes):
    n = len(left_nodes)
    pos = get_positions(left_nodes, right_nodes)
    labels = {}
    node_colors = []

    for i, node in enumerate(left_nodes):
        labels[node] = format_label(i + 1)
        node_colors.append("lightblue")
    for i, node in enumerate(right_nodes):
        labels[node] = format_label(i + 1)
        node_colors.append("lightcoral")

    all_nodes = left_nodes + right_nodes

    plt.figure(figsize=(6, n * 1.2))
    nx.draw(G, pos,
            with_labels=False,
            nodelist=all_nodes,
            node_color=node_colors,
            edgecolors='black',
            node_size=1500)

    for node in all_nodes:
        x, y = pos[node]
        plt.text(x, y, labels[node],
                 fontsize=12,
                 ha='center',
                 va='center',
                 bbox=dict(facecolor='none', edgecolor='none', boxstyle='round,pad=0.1'))

        weight = G.nodes[node].get('weight', '')
        dx = -0.15 if node.startswith("L") else 0.15
        ha = 'right' if node.startswith("L") else 'left'
        plt.text(x + dx, y, f"{weight}", fontsize=12, ha=ha, va='center', color='green')

    plt.axis("off")
    plt.title("Original Bipartite Graph")
    plt.show()
