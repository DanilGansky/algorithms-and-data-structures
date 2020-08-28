"""
Pros:
1. In-place
2. Simple and easy to implement
Cons:
1. Most implementations are not stable, due to swapping of values
2. Inefficient for large lists

Complexity:
    Time: O(n^2) average, worst, best
    Space: O(1) iterative, O(m) recursive where m is the recursion
           depth (unless tail-call elimination is available, then O(1))

Sources: http://www.icodeguru.com/cpp/SortingAlgorithms/selection.html
"""


from typing import Iterable


def selection_sort(iterable: Iterable[int], reverse=False) -> Iterable[int]:
    find_min_or_max = max if reverse else min

    def _compare(min_or_max, item):
        return min_or_max > item if reverse else min_or_max < item

    for i in range(len(iterable) - 1):
        num_index = find_min_or_max(enumerate(iterable[i+1:]),
                                    key=lambda x: x[1])[0]
        num_index += i + 1
        if _compare(iterable[num_index], iterable[i]):
            iterable[i], iterable[num_index] = iterable[num_index], iterable[i]
    return iterable
