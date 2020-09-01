"""
Pros:
1. Can be iterated in forward as well as reverse direction. In case of needing
   to delete previous node, there is no need to traverse from head node,
   as the node to be deleted can be found from ‘.previous’ pointer.
Cons:
1. Relatively complex to implement, requires more memory for storage
   (1 ‘.previous’ pointer per node).
2. Insertions and deletions are relatively more time consuming
   (assigning/reassigning ‘.previous’ pointer for neighbor nodes)

Sources: https://stackoverflow.com/a/12387760
"""

from typing import Any, Iterator, Optional

from data_structures.base import DoubleNode, data_validator


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head = None
        self._last = None

    def __iter__(self) -> Iterator[DoubleNode]:
        current = self._head
        while current is not None:
            yield current
            current = current.next

    def is_empty(self) -> bool:
        return self._head is None

    @data_validator
    def insert_after(self, data: Any, prev_node: DoubleNode) -> None:
        if not isinstance(prev_node, DoubleNode):
            raise TypeError('"prev_node" must be a DoubleNode')

        new_node = DoubleNode(data, prev_node, prev_node.next)
        if prev_node is self._last:
            self._last = new_node
        else:
            prev_node.next.prev = new_node
        prev_node.next = new_node

    @data_validator
    def insert_to_front(self, data: Any) -> None:
        new_node = DoubleNode(data, None, self._head)
        if self.is_empty():
            self._last = new_node
        else:
            self._head.prev = new_node
        self._head = new_node

    @data_validator
    def append(self, data: Any) -> None:
        new_node = DoubleNode(data, self._last, None)

        if self.is_empty():
            self._head = new_node
        else:
            self._last.next = new_node
        self._last = new_node

    def find(self, data: Any) -> DoubleNode:
        current = self._head
        while current is not None:
            if (current.data == data or
                    current.next is None and data is None):
                return current
            current = current.next
        raise ValueError(f'"{data}" not in list')

    def first(self) -> Optional[DoubleNode]:
        return self._head

    def last(self) -> Optional[DoubleNode]:
        return self._last

    @data_validator
    def delete(self, data: Any) -> None:
        node = self.find(data)

        if node is None:
            return None

        if node is self._head:
            self._head = self._head.next
            if self.is_empty():
                self._last.prev = None
                self._last = None
            else:
                self._head.prev = None
        elif node is self._last:
            node.prev.next = None
            self._last.prev = None
            self._last = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        del node

    def __repr__(self) -> str:
        return f'<DoublyLinkedList: [{", ".join([str(_) for _ in self])}]>'

    def __str__(self) -> str:
        return f'[{", ".join([str(_) for _ in self])}]'
