"""
Pros:
1. Most implementations are stable
Cons:
1. Not in-place

Complexity:
    Time: O(k*n), where n is the number of items and k is
          the number of digits in the largest item
    Space: O(k+n)

Note: If k (the number of digits) is less than log(n),
      radix sort can be faster than algorithms such as quicksort.

Sources: https://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/radix_sort/radix_sort_solution.ipynb
"""

from typing import Iterable

from algorithms.sorting.base import args_validator


@args_validator
def radix_sort(iterable: Iterable[int], reverse=False) -> Iterable[int]:
    max_digits = len(str(abs(max(iterable))))
    result = list(iterable)

    for digit in range(max_digits):
        buckets = [[] for _ in range(10)]
        for num in result:
            bucket_index = num // 10 ** digit % 10
            buckets[9 - bucket_index if reverse else bucket_index].append(num)

        result = []
        for bucket in buckets:
            result.extend(bucket)
    return result
