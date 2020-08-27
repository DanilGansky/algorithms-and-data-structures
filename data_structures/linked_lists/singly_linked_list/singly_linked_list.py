"""
Pros:
1. Inserting and deleting data does not require us to move/shift
   subsequent data elements.
Cons:
1. If we want to access a specific element, we need to traverse the list
   from the head of the list to find it which can take longer than an
   array access.
2. Linked lists require more memory.

IMPORTANT: Linked list will outperform arrays in say remove() method
           only when the pointer to node to be deleted is provided
           as parameter, not the value of node.
           Otherwise, you will have to search through list, which
           has same O(n) complexity as removing element from an
           indexed-based list.

Sources: 1. https://www.quora.com/What-are-the-pros-and-cons-of-using-a-linked-list
         2. https://stackoverflow.com/a/42021111
"""

from typing import Any, Iterator, Optional

from data_structures.base import Node, data_validator


class SinglyLinkedList:
    def __init__(self) -> None:
        self._head = None

    def __iter__(self) -> Iterator[Node]:
        current = self._head
        while current is not None:
            yield current
            current = current.next

    def is_empty(self) -> bool:
        return self._head is None

    @data_validator
    def insert_after(self, data: Any, prev_node: Node) -> None:
        if not isinstance(prev_node, Node):
            raise TypeError('"prev_node" must be a Node')
        new_node = Node(data, prev_node.next)
        prev_node.next = new_node

    @data_validator
    def insert_to_front(self, data: Any) -> None:
        self._head = Node(data, self._head)

    @data_validator
    def append(self, data: Any) -> None:
        new_node = Node(data, None)

        if self.is_empty():
            self._head = new_node
        else:
            last_node = self.last()
            last_node.next = new_node

    def find(self, data: Any) -> Node:
        current = self._head
        while current is not None:
            if (current.data == data or
                    current.next is None and data is None):
                return current
            current = current.next
        raise ValueError(f'"{data}" not in list')

    def first(self) -> Optional[Node]:
        return self._head

    def last(self) -> Optional[Node]:
        return self.find(None)

    @data_validator
    def delete(self, data: Any) -> None:
        node = self.find(data)

        if node is None:
            return None

        if node is self._head:
            self._head = self._head.next
        else:
            prev_node = None
            current = self._head
            while current is not None:
                if current.data == data:
                    break
                prev_node = current
                current = current.next
            prev_node.next = node.next
        del node

    def __repr__(self) -> str:
        return f'<SinglyLinkedList: [{", ".join([str(_) for _ in self])}]>'

    def __str__(self) -> str:
        return f'[{", ".join([str(_) for _ in self])}]'
