from typing import Any, Optional, Type


class Node:
    """
    Node implementation for Stack, SinglyLinkedList, Queue
    """

    def __init__(self, data: Any, next_node: Optional[Type['Node']]) -> None:
        self.data = data
        self._next_node = self._validate_new_node(next_node)

    def _validate_new_node(self, new_node: Any) -> Optional[Type['Node']]:
        if isinstance(new_node, Node) or new_node is None:
            return new_node
        raise TypeError('Invalid argument type')

    @property
    def next(self) -> Optional[Type['Node']]:
        return self._next_node

    @next.setter
    def next(self, new_node: Any) -> None:
        self._next_node = self._validate_new_node(new_node)

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f'<Node: {self.data}>'


class DoubleNode(Node):
    """
    Node implementation for DoublyLinkedList
    """

    def __init__(self, data: Any, prev_node: Optional['DoubleNode'],
                 next_node: Optional['DoubleNode']) -> None:
        super(DoubleNode, self).__init__(data, next_node)
        self._prev_node = self._validate_new_node(prev_node)

    def _validate_new_node(self, new_node: Any) -> Optional['DoubleNode']:
        if isinstance(new_node, DoubleNode) or new_node is None:
            return new_node
        raise TypeError('Invalid argument type')

    @property
    def prev(self) -> Optional['DoubleNode']:
        return self._prev_node

    @prev.setter
    def prev(self, new_node: Any) -> None:
        self._prev_node = self._validate_new_node(new_node)

    def __repr__(self) -> str:
        return f'<DoubleNode: {self.data}>'


def data_validator(method):
    def wrapper(self, data, *args, **kwargs):
        if data is None:
            raise ValueError('"data" cannot be NoneType')
        return method(self, data, *args, **kwargs)
    return wrapper
