"""
Pros:
1. The quick sort is regarded as the best sorting algorithm
2. It is able to deal well with a huge list of items
3. Because it sorts in place, no additional storage is required as well

Cons:
1. Not stable

Complexity:
    Time: O(n log(n)) average, best, O(n^2) worst
    Space: O(n)

Sources: 1. https://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/quick_sort/quick_sort_solution.ipynb
         2. http://z-sword.blogspot.com/2014/02/advantages-and-disadvantages-of-sorting.html
"""

from typing import Iterable, Optional


def quicksort(iterable: Iterable[int],
              reverse=False) -> Optional[Iterable[int]]:
    if len(iterable) < 2:
        return iterable

    iterable = list(iterable)
    left, middle, right = [], [], []
    pivot = iterable[len(iterable) // 2]

    for item in iterable:
        if item == pivot:
            middle.append(item)
        elif item < pivot:
            if reverse:
                right.append(item)
            else:
                left.append(item)
        elif item > pivot:
            if reverse:
                left.append(item)
            else:
                right.append(item)

    left = quicksort(left, reverse=reverse)
    right = quicksort(right, reverse=reverse)
    return left + middle + right
