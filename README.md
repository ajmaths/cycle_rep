# cycle_reps_package

A Python package for generating bipartite graphs with weighted vertices, computing weight-biased spanning trees, and analyzing cycle representatives—especially in filtered subgraphs based on vertex weights.

---

## Features

- Generate bipartite graphs with labeled left (`L`) and right (`R`) node sets.
- Assign weights to vertices representing birth times or other attributes.
- Compute a **weight-biased spanning tree** prioritizing edges connected to nodes with higher weights.
- Extract and visualize fundamental cycle representatives from non-tree edges.
- Filter graphs by vertex weight thresholds and analyze cycles in the filtered subgraphs.
- Visualize graphs, spanning trees, filtered subgraphs, and cycles with clear node/edge coloring and weight labels.

---

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

**Example usage in Python:**
```python
from cycle_reps_package.graphgen import generate_bipartite_graph, assign_weights
from cycle_reps_package.spanningtree import weight_biased_spanning_tree, draw_weight_biased_spanning_tree
from cycle_reps_package.cycles import find_cycles_from_non_tree_edges, decompose_manual_cycle_exact
from cycle_reps_package.filtering import draw_filtered_subgraph, analyze_and_draw_superlevel_cycles

import cycle_reps_package.graphgen as gg
print(dir(gg))

n = 5
weights = [2, 1, 3, 5, 4] # weights of vertices of the form 0i. (Note: 0i=i0)

G, left_nodes, right_nodes = gg.generate_bipartite_graph(n)
gg.assign_weights(G, left_nodes, right_nodes, weights)
gg.draw_bipartite_graph(G, left_nodes, right_nodes)

T = weight_biased_spanning_tree(G)
draw_weight_biased_spanning_tree(T, left_nodes, right_nodes)

cycles = find_cycles_from_non_tree_edges(G, T)
draw_filtered_subgraph(G, left_nodes, right_nodes, threshold=0.5)
analyze_and_draw_superlevel_cycles(G, left_nodes, right_nodes, threshold=0.5)

```

## File Structure

- `Cycle_reps.ipynb` — Contains all functions for graph generation, weight assignment, spanning tree computation, and visualization.
- cycle_reps_package/
├-- __init__.py
├-- graph_utils.py      # Core functions for graph generation, weights, spanning tree, cycle reps, filtering, and drawing
├-- filters.py          # Filtering-related functions 
├-- cycles.py           # Cycle analysis and drawing utilities 
└-- tests/
    └-- test_basic.py   # Unit tests for main functionalities

## Notes

- The spanning tree algorithm prioritizes edges where the maximum node weight of the endpoints is highest, resulting in nodes with larger weights having higher degrees.
- The graph is visualized with left nodes in light blue and right nodes in light coral; node weights are displayed in green.

## License

This project is open source and available under the MIT License.

## Contact

For questions or contributions, please open an issue or submit a pull request.
