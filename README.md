# Algorithms and data structures

Implementation of the most popular algorithms and data structures in Python.

## Algorithms:

-   [Sorting](algorithms/sorting/)
    -   [Insertion sort](algorithms/sorting/insertion_sort/insertion_sort.py)
    -   [Quicksort](algorithms/sorting/quicksort/quicksort.py)
    -   [Merge sort](algorithms/sorting/merge_sort/merge_sort.py)
    -   [Selection sort](algorithms/sorting/selection_sort/selection_sort.py)
    -   [Radix sort](algorithms/sorting/radix_sort/radix_sort.py) (Only for positive numbers)
-   [Graph algorithms](algorithms/graph/)
    -   [Dijkstra's algorithm](algorithms/graph/dijkstra/dijkstra.py)

## Data structures:

-   [Linked lists](data_structures/linked_lists/)
    -   [SinglyLinkedList](data_structures/linked_lists/singly_linked_list/singly_linked_list.py)
    -   [DoublyLinkedList](data_structures/linked_lists/doubly_linked_list/doubly_linked_list.py)
-   [Stack](data_structures/stack/stack.py)
-   [Queue](data_structures/queue/queue.py)
-   [HashMap](data_structures/hash_map/hash_map.py)
-   [Graph](data_structures/graph/graph.py)

## Tests

For running all tests write down:

```bash
$ python -m unittest discover -s ./ -p 'tests.py'
```

For running specific tests:

```bash
$ python -m unittest <module>.<data_structure_or_algorithm>_tests
```

Ex: stack

```bash
$ python -m unittest data_structures.stack_tests
```

Ex: quicksort

```bash
$ python -m unittest algorithms.quicksort_tests
```
