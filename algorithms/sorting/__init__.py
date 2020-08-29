from .insertion_sort.insertion_sort import insertion_sort
from .quicksort.quicksort import quicksort
from .merge_sort.merge_sort import merge_sort
from .selection_sort.selection_sort import selection_sort
from .radix_sort.radix_sort import radix_sort

from .insertion_sort import tests as insertion_sort_tests
from .quicksort import tests as quicksort_tests
from .merge_sort import tests as merge_sort_tests
from .selection_sort import tests as selection_sort_tests
from .radix_sort import tests as radix_sort_tests


__all__ = (insertion_sort, quicksort, merge_sort,
           selection_sort, radix_sort)
