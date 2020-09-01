import unittest

from data_structures.graph import Graph, Node
from data_structures.graph.graph import NotEnoughKeys


class TestNode(unittest.TestCase):
    def test_add_neighbor(self):
        print('Test: test_add_neighbor')
        n, n1 = Node(0), Node(1)

        print('Test: Invalid input')
        self.assertRaises(ValueError, n.add_neighbor, None)
        self.assertRaises(ValueError, n.add_neighbor, n)

        print('Test: general case')
        n.add_neighbor(n1)
        self.assertEqual(n.neighbors[0][0].key, n1.key)
        print('Success: test_add_neighbor')

    def test_remove_neighbor(self):
        print('Test: test_remove_neighbor')
        n, n1 = Node(0), Node(1)

        print('Test: remove a non-existent node')
        self.assertRaises(ValueError, n.remove_neighbor, 1)

        print('Test: general case')
        n.add_neighbor(n1)
        self.assertEqual(n.neighbors[0][0].key, n1.key)
        n.remove_neighbor(1)
        self.assertEqual(len(n.neighbors), 0)
        print('Success: test_remove_neighbor')


class TestGraph(unittest.TestCase):
    def test_add_node(self):
        print('Test: test_add_node')
        print('Test: keys are numbers')
        g = Graph()
        g.add_node()
        self.assertEqual(len(g._nodes), 1)
        self.assertEqual(g._counter, 1)

        print('Test: keys are chars')
        g = Graph(letters=True)
        g.add_node()
        self.assertEqual(len(g._nodes), 1)
        self.assertEqual(g._counter, 98)

        print('Test: keys are chars (not enough keys)')
        for i in range(98, 123):
            g.add_node()

        self.assertRaises(NotEnoughKeys, g.add_node)
        print('Success: test_add_node')

    def test_remove_node(self):
        print('Test: test_remove_node')
        g = Graph()

        print('Test: remove a non-existent node')
        self.assertRaises(ValueError, g.remove_node, 0)

        print('Test: general case')
        n = g.add_node()
        self.assertEqual(len(g._nodes), 1)
        g.remove_node(n.key)
        self.assertEqual(len(g._nodes), 0)
        print('Success: test_remove_node')

    def test_add_edge(self):
        print('Test: test_add_edge')
        g = Graph()

        print('Test: Invalid input')
        self.assertRaises(ValueError, g.add_edge, None, None)

        print('Test: general case')
        n, n1 = g.add_node(), g.add_node()
        g.add_edge(n, n1)
        self.assertIn([n1, 0], n.neighbors)

        n2 = g.add_node()
        g.add_edge(n1, n2, 5)
        self.assertIn([n2, 5], n1.neighbors)
        print('Success: test_add_edge')

    def test_add_undirected_edge(self):
        print('Test: test_add_undirected_edge')
        g = Graph()
        n, n1 = g.add_node(), g.add_node()
        g.add_undirected_edge(n, n1, 5)
        self.assertIn([n1, 5], n.neighbors)
        self.assertIn([n, 5], n1.neighbors)
        print('Success: test_add_undirected_edge')


def main():
    test_node = TestNode()
    test_node.test_add_neighbor()
    test_node.test_remove_neighbor()

    test_graph = TestGraph()
    test_graph.test_add_node()
    test_graph.test_remove_node()
    test_graph.test_add_edge()
    test_graph.test_add_undirected_edge()


if __name__ == "__main__":
    main()
