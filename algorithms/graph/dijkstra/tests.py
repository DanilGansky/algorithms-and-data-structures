import unittest

from algorithms.graph import dijkstra
from data_structures.graph import Graph


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        print('Test: test_dijkstra')
        graph = Graph(letters=True)
        a, b, c, d, e, f, g, h = (graph.add_node(), graph.add_node(),
                                  graph.add_node(), graph.add_node(),
                                  graph.add_node(), graph.add_node(),
                                  graph.add_node(), graph.add_node())
        graph.add_undirected_edge(a, b, 8)
        graph.add_undirected_edge(a, c, 2)
        graph.add_undirected_edge(a, d, 5)
        graph.add_undirected_edge(c, d, 2)
        graph.add_undirected_edge(c, e, 5)
        graph.add_undirected_edge(e, d, 1)
        graph.add_undirected_edge(e, g, 1)
        graph.add_undirected_edge(g, d, 3)
        graph.add_undirected_edge(g, f, 2)
        graph.add_undirected_edge(g, h, 6)
        graph.add_undirected_edge(h, f, 3)
        graph.add_undirected_edge(f, d, 6)
        graph.add_undirected_edge(f, b, 13)
        graph.add_undirected_edge(b, d, 2)
        self.assertEqual(dijkstra(graph, h, a),
                         (['a', 'c', 'd', 'e', 'g', 'f', 'h'], 11))
        print('Success: test_dijkstra')


def main():
    test = TestDijkstra()
    test.test_dijkstra()


if __name__ == "__main__":
    main()
