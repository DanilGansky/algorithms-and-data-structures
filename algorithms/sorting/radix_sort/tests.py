import unittest
import random

from algorithms.sorting import radix_sort


class TestRadixSort(unittest.TestCase):
    def test_radix_sort(self):
        random_list = [random.randint(0, 10) for _ in range(10)]

        print('None input')
        self.assertRaises(ValueError, radix_sort, None)
        self.assertRaises(ValueError, radix_sort, [], None)

        print('Empty input')
        self.assertEqual(radix_sort([]), [])

        print('One element')
        self.assertEqual(radix_sort([1, ]), [1, ])

        print('Two or more elements')
        self.assertEqual(radix_sort(random_list), sorted(random_list))

        print('Two or more elements in reverse')
        self.assertEqual(radix_sort(random_list, reverse=True),
                         sorted(random_list, reverse=True))

        print('Success: test_radix_sort')


def main():
    test = TestRadixSort()
    test.test_radix_sort()


if __name__ == "__main__":
    main()
