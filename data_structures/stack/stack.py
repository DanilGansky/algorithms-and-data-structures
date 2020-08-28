"""
Pros:
1. Easily increase or decrease the Stack size
Cons:
1. Requires extra memory to keep details about next node
2. You only have access to the top element

Sources: https://www.codingame.com/playgrounds/6525/stack-data-structure
"""

from typing import Any, Iterator

from data_structures.base import Node, data_validator


class Stack:
    """Linked List based Stack"""

    def __init__(self) -> None:
        self._head = None

    def __iter__(self) -> Iterator[Node]:
        current = self._head
        while current is not None:
            yield current
            current = current.next

    def find(self, data: Any) -> Node:
        current = self._head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        raise ValueError(f'"{data}" not in list')

    @data_validator
    def push(self, data: Any) -> None:
        self._head = Node(data, self._head)

    def pop(self) -> Any:
        if self._head is None:
            return None

        head_data = self._head.data
        self._head = self._head.next
        return head_data

    def peek(self) -> Any:
        if self._head is None:
            return None
        return self._head.data

    def is_empty(self) -> bool:
        return self._head is None

    def __repr__(self) -> str:
        return f'<Stack: [{", ".join([str(_) for _ in self])}]>'

    def __str__(self) -> str:
        return f'[{", ".join([str(_) for _ in self])}]'
