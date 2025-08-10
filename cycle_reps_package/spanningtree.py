import heapq
import networkx as nx
import matplotlib.pyplot as plt
from .graphgen import get_positions, format_label

def weight_biased_spanning_tree(G):
    weights = {v: G.nodes[v].get('weight', 0) for v in G.nodes}
    start = max(weights, key=weights.get)
    visited = {start}
    edges_in_tree = []

    heap = []
    for nbr in G.neighbors(start):
        priority = max(weights[start], weights[nbr])
        heapq.heappush(heap, (-priority, start, nbr))

    while len(visited) < G.number_of_nodes() and heap:
        neg_priority, u, v = heapq.heappop(heap)
        if v in visited and u in visited:
            continue

        new_node = v if u in visited else u
        visited.add(new_node)
        edges_in_tree.append((u, v))

        for nbr in G.neighbors(new_node):
            if nbr not in visited:
                priority = max(weights[new_node], weights[nbr])
                heapq.heappush(heap, (-priority, new_node, nbr))

    T = nx.Graph()
    T.add_nodes_from(G.nodes(data=True))
    T.add_edges_from(edges_in_tree)
    return T

def draw_weight_biased_spanning_tree(T, left_nodes, right_nodes):
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

    import matplotlib.pyplot as plt
    plt.figure(figsize=(6, n * 1.2))
    nx.draw(T, pos,
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

        weight = T.nodes[node].get('weight', '')
        dx = -0.15 if node.startswith("L") else 0.15
        ha = 'right' if node.startswith("L") else 'left'
        plt.text(x + dx, y, f"{weight}", fontsize=12, ha=ha, va='center', color='green')

    plt.axis("off")
    plt.title("Weight-Biased Spanning Tree")
    plt.show()
