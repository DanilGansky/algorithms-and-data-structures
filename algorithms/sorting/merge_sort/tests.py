import unittest
import random

from algorithms.sorting import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        random_list = [random.randint(-10, 10) for _ in range(10)]

        print('None input')
        self.assertRaises(ValueError, merge_sort, None)
        self.assertRaises(ValueError, merge_sort, [], None)

        print('Empty input')
        self.assertEqual(merge_sort([]), [])

        print('One element')
        self.assertEqual(merge_sort([1, ]), [1, ])

        print('Two or more elements')
        self.assertEqual(merge_sort(random_list), sorted(random_list))

        print('Two or more elements in reverse')
        self.assertEqual(merge_sort(random_list, reverse=True),
                         sorted(random_list, reverse=True))

        print('Success: test_quicksort')


def main():
    test = TestMergeSort()
    test.test_merge_sort()


if __name__ == "__main__":
    main()
