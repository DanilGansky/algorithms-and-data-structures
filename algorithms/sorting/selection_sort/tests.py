import random
import unittest

from algorithms.sorting import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        random_list = [random.randint(-10, 10) for _ in range(10)]

        print('None input')
        self.assertRaises(ValueError, selection_sort, None)
        self.assertRaises(ValueError, selection_sort, [], None)

        print('Empty input')
        self.assertEqual(selection_sort([]), [])

        print('One element')
        self.assertEqual(selection_sort([1, ]), [1, ])

        print('Two or more elements')
        self.assertEqual(selection_sort(random_list), sorted(random_list))

        print('Two or more elements in reverse')
        self.assertEqual(selection_sort(random_list, reverse=True),
                         sorted(random_list, reverse=True))

        print('Success: test_selection_sort')


def main():
    test = TestSelectionSort()
    test.test_selection_sort()


if __name__ == "__main__":
    main()
