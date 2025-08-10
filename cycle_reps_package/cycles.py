import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from .graphgen import format_label

def find_cycles_from_non_tree_edges(G, T):
    cycles = []
    tree_edges = set(T.edges()) | {(v, u) for u, v in T.edges()}
    for u, v in G.edges():
        if (u, v) not in tree_edges:
            path = nx.shortest_path(T, source=u, target=v)
            cycle = list(zip(path, path[1:])) + [(u, v)]
            cycles.append(cycle)
    return cycles

def draw_cycle(G, cycle, pos, weights, index, filename=None):
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, node_color='lightgray', edge_color='lightgray', node_size=1500)

    tree_path_edges = cycle[:-1]
    non_tree_edge = [cycle[-1]]

    nx.draw_networkx_edges(G, pos, edgelist=tree_path_edges, edge_color='red', width=2)
    nx.draw_networkx_edges(G, pos, edgelist=non_tree_edge, edge_color='blue', width=3, style='dashed')

    for node in G.nodes():
        x, y = pos[node]
        label = format_label(int(node[1:]) + 1)
        weight = weights.get(node, '')
        plt.text(x, y, label, fontsize=10, ha='center', va='center',
                 bbox=dict(facecolor='none', edgecolor='none', boxstyle='round,pad=0.1'))
        dx = -0.15 if node.startswith("L") else 0.15
        ha = 'right' if node.startswith("L") else 'left'
        plt.text(x + dx, y, f"{weight}", fontsize=10, ha=ha, va='center', color='green')

    plt.title(f"Cycle {index + 1}")
    plt.axis("off")
    if filename:
        plt.savefig(filename, bbox_inches='tight')
    plt.show()
    plt.close()

def edgeset(cycle_edges):
    return set(frozenset(e) for e in cycle_edges)

def decompose_manual_cycle_exact(manual_cycle_edges, fundamental_cycles):
    manual_set = edgeset(manual_cycle_edges)

    for r in range(1, len(fundamental_cycles) + 1):
        for idx_tuple in combinations(range(len(fundamental_cycles)), r):
            combined = set()
            for i in idx_tuple:
                combined ^= edgeset(fundamental_cycles[i])
            if combined == manual_set:
                return list(idx_tuple)

    print("Could not decompose the manual cycle using fundamental cycles.")
    return None

def is_valid_cycle(G, cycle):
    if len(cycle) < 3 or cycle[0] != cycle[-1]:
        return False
    for u, v in zip(cycle, cycle[1:]):
        if not G.has_edge(u, v):
            return False
    return True

def draw_manual_cycle(G, cycle, pos, weights, title="Manual Cycle"):
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, node_color='lightgray', edge_color='lightgray', node_size=1500)

    cycle_edges = list(zip(cycle, cycle[1:]))

    nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color='purple', width=3)

    for node in G.nodes():
        x, y = pos[node]
        label = format_label(int(node[1:]) + 1)
        weight = weights.get(node, '')
        plt.text(x, y, label, fontsize=10, ha='center', va='center',
                 bbox=dict(facecolor='none', edgecolor='none', boxstyle='round,pad=0.1'))
        dx = -0.15 if node.startswith("L") else 0.15
        ha = 'right' if node.startswith("L") else 'left'
        plt.text(x + dx, y, f"{weight}", fontsize=10, ha=ha, va='center', color='green')

    plt.title(title)
    plt.axis("off")
    plt.show()
