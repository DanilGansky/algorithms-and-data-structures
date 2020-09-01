"""
Dijkstra's algorithm
Complexity:
    Time: O(v^2), where v is the number of vertices
    Space: O(v^2)
"""

from typing import Dict, List, Optional, Tuple, Union

from data_structures.graph import Graph, Node


def _update_unvisited(unvisited: List[List[Union[Node, int]]],
                      neighbors: List[List[Union[Node, int]]],
                      previous: Dict[Union[str, int], Union[str, int]],
                      current: Node, path_weight: int) -> None:
    for node, weight in neighbors:
        new_weight = weight + path_weight
        index = _find_node(unvisited, node)
        if new_weight < unvisited[index][1]:
            unvisited[index][1] = new_weight
            previous[node.key] = current.key


def _find_node(nodes: List[List[Union[Node, int]]],
               node: Node) -> Optional[int]:
    for index, _node in enumerate(nodes):
        if node.key == _node[0].key:
            return index


def _delete_visited_node(unvisited: List[List[Union[Node, int]]],
                         current: Node) -> None:
    for index, node in enumerate(unvisited):
        if node[0].key == current.key:
            del unvisited[index]
            return


def _show_path(previous: Dict[Union[str, int], Union[str, int]],
               start: Union[str, int],
               goal: Union[str, int]) -> List[Union[str, int]]:
    path = [goal, ]
    while start != goal:
        goal = previous[goal]
        path.append(goal)
    return path


def dijkstra(graph: Graph, current: Node,
             goal: Node) -> Tuple[List[Union[str, int]], int]:
    import math
    start = current
    path_weight = 0
    unvisited = [[n, 0] if n is current else [n, math.inf]
                 for n in graph.nodes]
    visited = []
    previous = {}

    while current is not goal:
        visited.append(current)
        neighbors = [n for n in current.neighbors if n[0] not in visited]
        _update_unvisited(unvisited, neighbors, previous, current, path_weight)
        _delete_visited_node(unvisited, current)
        current, weight = min(unvisited, key=lambda x: x[1])
        path_weight = weight
    path = _show_path(previous, start.key, goal.key)
    return path, weight
