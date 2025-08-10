import networkx as nx
import matplotlib.pyplot as plt
from .graphgen import format_label, get_positions
from .spanningtree import weight_biased_spanning_tree
from .cycles import find_cycles_from_non_tree_edges, draw_cycle

def superlevel_subgraph(G, threshold):
    selected_nodes = [v for v, data in G.nodes(data=True) if data.get('weight', float('-inf')) >= threshold]
    return G.subgraph(selected_nodes).copy()

def draw_filtered_subgraph(G, left_nodes, right_nodes, threshold):
    G_sub = superlevel_subgraph(G, threshold)
    print(f"Threshold = {threshold}")
    print(f"Nodes in filtered subgraph: {list(G_sub.nodes())}")
    print(f"Number of nodes: {G_sub.number_of_nodes()}, edges: {G_sub.number_of_edges()}")

    if G_sub.number_of_nodes() == 0:
        print("No nodes satisfy the threshold condition.")
        return

    # Count path components
    num_components = nx.number_connected_components(G_sub)
    print(f"Number of path components in filtered subgraph: {num_components}")

    pos = get_positions(left_nodes, right_nodes)
    nodes_sub = list(G_sub.nodes())

    node_colors = []
    labels = {}
    for node in nodes_sub:
        if node in left_nodes:
            node_colors.append("lightblue")
            i = left_nodes.index(node)
        else:
            node_colors.append("lightcoral")
            i = right_nodes.index(node)
        labels[node] = format_label(i + 1)

    plt.figure(figsize=(4, len(nodes_sub) * 1.2))

    nx.draw(G_sub, pos,
            with_labels=False,
            nodelist=nodes_sub,
            node_color=node_colors,
            edgecolors='black',
            node_size=1500)

    for node in nodes_sub:
        x, y = pos[node]
        plt.text(x, y, labels[node],
                 fontsize=10,
                 ha='center',
                 va='center',
                 bbox=dict(facecolor='none', edgecolor='none', boxstyle='round,pad=0.1'))

    for node in nodes_sub:
        x, y = pos[node]
        weight = G_sub.nodes[node].get('weight', '')
        if node in left_nodes:
            plt.text(x - 0.1, y, f"{weight}", fontsize=12, ha='right', va='center', color='green')
        else:
            plt.text(x + 0.1, y, f"{weight}", fontsize=12, ha='left', va='center', color='green')

    plt.title(f"Superlevel Subgraph with Threshold ≥ {threshold}")
    plt.axis("off")
    plt.show()

def analyze_and_draw_superlevel_cycles(G, left_nodes, right_nodes, threshold):
    G_sub = superlevel_subgraph(G, threshold)
    print(f"Threshold = {threshold}")
    print(f"Nodes in filtered subgraph: {list(G_sub.nodes())}")
    print(f"Number of nodes: {G_sub.number_of_nodes()}, edges: {G_sub.number_of_edges()}")

    if G_sub.number_of_nodes() == 0:
        print("No nodes satisfy the threshold condition.")
        return

    pos = get_positions(left_nodes, right_nodes)
    pos_sub = {node: pos[node] for node in G_sub.nodes()}

    node_colors = []
    labels = {}
    for node in G_sub.nodes():
        if node in left_nodes:
            node_colors.append("lightblue")
            i = left_nodes.index(node)
        else:
            node_colors.append("lightcoral")
            i = right_nodes.index(node)
        labels[node] = format_label(i + 1)

    plt.figure(figsize=(4, len(G_sub.nodes()) * 0.8))
    nx.draw(G_sub, pos_sub,
            with_labels=False,
            node_color=node_colors,
            edgecolors='black',
            node_size=1500)

    for node in G_sub.nodes():
        x, y = pos_sub[node]
        plt.text(x, y, labels[node],
                 fontsize=10,
                 ha='center',
                 va='center',
                 bbox=dict(facecolor='none', edgecolor='none', boxstyle='round,pad=0.1'))

    for node in G_sub.nodes():
        x, y = pos_sub[node]
        weight = G_sub.nodes[node].get('weight', '')
        if node in left_nodes:
            plt.text(x - 0.1, y, f"{weight}", fontsize=12, ha='right', va='center', color='green')
        else:
            plt.text(x + 0.1, y, f"{weight}", fontsize=12, ha='left', va='center', color='green')

    plt.title(f"Superlevel Subgraph with Threshold ≥ {threshold}")
    plt.axis("off")
    plt.show()

    T_sub = weight_biased_spanning_tree(G_sub)
    cycles_sub = find_cycles_from_non_tree_edges(G_sub, T_sub)

    for i, cycle in enumerate(cycles_sub):
        draw_cycle(G_sub, cycle, pos_sub, nx.get_node_attributes(G_sub, 'weight'), i)
