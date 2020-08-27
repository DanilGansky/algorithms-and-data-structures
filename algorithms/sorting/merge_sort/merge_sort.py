"""
Pros:
1. Worst case, best case, average case time complexity is : o(n log(n))
   which makes it very efficient
2. Highly parallelisable
3. Most implementations are stable

Cons:
1. Marginally slower than quick sort in practice
2. Not in-place

Complexity:
   Time: O(n log(n))
   Space: O(n)

Sources: https://www.quora.com/What-are-the-pros-and-cons-of-merge-sort
"""

from typing import Iterable


def merge_sort(iterable: Iterable[int], reverse=False) -> Iterable[int]:
    return _partitioning(iterable, reverse)


def _partitioning(iterable: Iterable[int], reverse=False) -> Iterable[int]:
    if len(iterable) < 2:
        return iterable

    mid = len(iterable) // 2
    left = iterable[:mid]
    right = iterable[mid:]
    left = _partitioning(left, reverse)
    right = _partitioning(right, reverse)
    return _merge(left, right, reverse)


def _merge(left: Iterable[int], right: Iterable[int],
           reverse=False) -> Iterable[int]:
    left_pointer, right_pointer = 0, 0
    result = []

    def _compare(x, y, reverse):
        if reverse:
            return x > y
        return x < y

    while left_pointer < len(left) and right_pointer < len(right):
        if _compare(left[left_pointer], right[right_pointer], reverse):
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    while left_pointer < len(left):
        result.append(left[left_pointer])
        left_pointer += 1
    while right_pointer < len(right):
        result.append(right[right_pointer])
        right_pointer += 1
    return result
