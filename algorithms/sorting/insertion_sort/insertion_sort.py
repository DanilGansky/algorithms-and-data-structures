"""
Pros:
1. Efficient for sorting of small data
2. Efficient for data that are almost sorted
3. In-place sorting as only constant amount of additional
   memory space is required
4. Stable sorting algorithm, since it does not change
   the relative order of elements with equal keys
Cons:
1. Less efficient for sorting of large data

Complexity:
   Time: O(n^2) average, worst. O(1) best if input is already sorted
   Space: O(1) for the iterative solution


Sources: 1. https://www.coursehero.com/file/p4mf0v/Insertion-Sort-Pros-and-Cons-Pros-Efficient-for-sorting-of-small-data-Efficient/
         2. https://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/insertion_sort/insertion_sort_solution.ipynb
"""

from typing import Iterable

from algorithms.sorting.base import args_validator


@args_validator
def insertion_sort(iterable: Iterable[int], reverse=False) -> Iterable[int]:
    iterable = list(iterable)

    if reverse:
        def _compare(item, item2):
            return item > item2
    else:
        def _compare(item, item2):
            return item < item2

    for i in range(1, len(iterable)):
        for j in range(i):
            if _compare(iterable[i], iterable[j]):
                temp = iterable[i]
                iterable[j+1:i+1] = iterable[j:i]
                iterable[j] = temp
    return iterable
