from typing import List, Union


class Node:
    def __init__(self, key: Union[str, int]) -> None:
        self.key = key
        self.neighbors = []

    def add_neighbor(self, node: 'Node', weight: int = 0) -> None:
        if not isinstance(node, Node):
            raise ValueError('"node" must be an instance of Node')
        if node is self:
            raise ValueError('you cannot add this node to neighbors')
        self.neighbors.append([node, weight])

    def remove_neighbor(self, key: Union[str, int]) -> None:
        for index, node in enumerate(self.neighbors):
            if node[0].key == key:
                del self.neighbors[index]
                return
        raise ValueError(f'node with key {key} not found')

    def __repr__(self) -> str:
        return f'<Node: {self.key}>'


class Graph:
    def __init__(self, letters: bool = False) -> None:
        self._nodes = []
        self._letters = letters
        self._counter = 97 if letters else 0

    @property
    def nodes(self) -> List[Node]:
        return self._nodes

    def add_node(self) -> Node:
        key = chr(self._counter) if self._letters else self._counter
        new_node = Node(key)

        if self._letters and self._counter not in range(97, 123):
            raise NotEnoughKeys

        self._counter += 1
        self._nodes.append(new_node)
        return new_node

    def remove_node(self, key: Union[str, int]) -> None:
        for index, node in enumerate(self._nodes):
            if node.key == key:
                node.neighbors = []
                del self._nodes[index]
                return
        raise ValueError(f'node with key {key} not found')

    def add_edge(self, src_node: Node,
                 dest_node: Node, weight: int = 0) -> None:
        if not (isinstance(src_node, Node) and isinstance(dest_node, Node)):
            raise ValueError(
                '"src_node" and "dest_node" must be instances of Node')
        src_node.add_neighbor(dest_node, weight)

    def add_undirected_edge(self, src_node: Node,
                            dest_node: Node, weight: int = 0) -> None:
        self.add_edge(src_node, dest_node, weight)
        self.add_edge(dest_node, src_node, weight)

    def __repr__(self) -> str:
        return f'<Graph: {self._nodes}>'


class NotEnoughKeys(Exception):
    pass
