"""
Pros:
1. Easily increase or decrease the Queue size
Cons:
1. Requires extra memory to keep details about next node
"""

from typing import Any, Iterable

from data_structures.base import Node, data_validator


class Queue:
    """Linked List based Queue"""

    def __init__(self) -> None:
        self._front = None
        self._rear = None

    def __iter__(self) -> Iterable[Node]:
        current = self._front
        while current is not None:
            yield current
            current = current.next

    @data_validator
    def enqueue(self, data: Any) -> None:
        new_node = Node(data, None)

        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node

    def dequeue(self) -> Any:
        if self.is_empty():
            return None

        data = self._front.data

        if self._front is self._rear:
            self._front = self._rear = None
        else:
            self._front = self._front.next
        return data

    def peek(self) -> Any:
        if self.is_empty():
            return None
        return self._front.data

    def is_empty(self) -> bool:
        return self._front is None

    def __repr__(self) -> str:
        return f'<Queue: [{", ".join([str(_) for _ in self])}]>'

    def __str__(self) -> str:
        return f'[{", ".join([str(_) for _ in self])}]'
