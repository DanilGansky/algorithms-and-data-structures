import unittest
import random

from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        random_list = [random.randint(-10, 10) for _ in range(10)]

        print('None input')
        self.assertRaises(ValueError, insertion_sort, None)
        self.assertRaises(ValueError, insertion_sort, [], None)

        print('Empty input')
        self.assertEqual(insertion_sort([]), [])

        print('One element')
        self.assertEqual(insertion_sort([1, ]), [1, ])

        print('Two or more elements')
        self.assertEqual(insertion_sort(random_list), sorted(random_list))

        print('Two or more elements in reverse')
        self.assertEqual(insertion_sort(random_list, reverse=True),
                         sorted(random_list, reverse=True))

        print('Success: test_insertion_sort')


def main():
    test = TestInsertionSort()
    test.test_insertion_sort()


if __name__ == "__main__":
    main()
