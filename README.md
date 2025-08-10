# Bipartite Graph Weighted Spanning Tree

This repository contains Python code to generate bipartite graphs with weighted nodes, and compute a **degree-biased spanning tree** that prioritizes edges connecting vertices with higher weights.

## Features

- Generate bipartite graphs with two node sets (`L` and `R`) and weighted vertices.
- Assign weights to nodes to represent birth times of vertices of the combinatorial model for the (restricted) second configuration space of star graphs.
- Compute a spanning tree biased towards nodes with higher weights using a max-weight edge priority.
- Visualize the original bipartite graph and the degree-biased spanning tree with node weights.

## Usage

1. **Install dependencies**

```bash
pip install networkx matplotlib
```

2. **Run the code**

- Modify parameters like `n` (graph size) and `weights` (node weights).
- Generate the bipartite graph.
- Assign weights to nodes.
- Compute the degree-biased spanning tree.
- Visualize the graphs.

```python
from cycle_reps_package.graph_utils import generate_bipartite_graph, assign_weights, weight_biased_spanning_tree, find_cycles_from_non_tree_edges

n = 4
weights = [2, 1, 3, 4]

G, left_nodes, right_nodes = generate_bipartite_graph(n)
assign_weights(G, left_nodes, right_nodes, weights)

T = weight_biased_spanning_tree(G)
draw_weighted_bipartite_graph(T, left_nodes, right_nodes, title="Degree-Biased Spanning Tree")
```

## File Structure

- `Cycle_reps.ipynb` — Contains all functions for graph generation, weight assignment, spanning tree computation, and visualization.

## Notes

- The spanning tree algorithm prioritizes edges where the maximum node weight of the endpoints is highest, resulting in nodes with larger weights having higher degrees.
- The graph is visualized with left nodes in light blue and right nodes in light coral; node weights are displayed in green.

## License

This project is open source and available under the MIT License.
