import unittest
import networkx as nx
from mygraph.graph_utils import generate_bipartite_graph, assign_weights, weight_biased_spanning_tree, find_cycles_from_non_tree_edges

class TestBasicFunctions(unittest.TestCase):
    def setUp(self):
        # Setup a basic graph for tests
        self.n = 4
        self.weights = [2, 1, 3, 4]
        self.G, self.left_nodes, self.right_nodes = generate_bipartite_graph(self.n)
        assign_weights(self.G, self.left_nodes, self.right_nodes, self.weights)

    def test_graph_nodes(self):
        self.assertEqual(len(self.G.nodes), 8)  # 4 left + 4 right
        self.assertEqual(len(self.G.edges), 12)  # n * (n-1)

    def test_weights_assigned(self):
        for i, node in enumerate(self.left_nodes):
            self.assertEqual(self.G.nodes[node]['weight'], self.weights[i])
        for i, node in enumerate(self.right_nodes):
            self.assertEqual(self.G.nodes[node]['weight'], self.weights[i])

    def test_spanning_tree(self):
        T = weight_biased_spanning_tree(self.G)
        # Tree has same nodes as G
        self.assertEqual(set(T.nodes), set(self.G.nodes))
        # Tree edges count is nodes - 1 (for connected graph)
        self.assertEqual(len(T.edges), len(T.nodes) - 1)

    def test_fundamental_cycles(self):
        T = weight_biased_spanning_tree(self.G)
        cycles = find_cycles_from_non_tree_edges(self.G, T)

        # Check that some cycles are found
        self.assertTrue(len(cycles) > 0, "No cycles found.")

        # Check each cycle is valid (closed loop)
        for cycle in cycles:
            nodes_in_path = [edge[0] for edge in cycle] + [cycle[-1][1]]
            self.assertEqual(nodes_in_path[0], nodes_in_path[-1], "Cycle does not start and end at the same node.")

            # Check all edges exist in the graph
            for u, v in cycle:
                self.assertTrue(self.G.has_edge(u, v) or self.G.has_edge(v, u), f"Edge {(u, v)} not in graph")

        # Optionally check expected number of cycles (depends on graph structure)
        expected_cycles = self.G.number_of_edges() - self.G.number_of_nodes() + 1  # cyclomatic number
        self.assertEqual(len(cycles), expected_cycles, "Unexpected number of fundamental cycles.")

if __name__ == "__main__":
    unittest.main()
