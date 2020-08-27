import unittest
import random

from quicksort import quicksort


class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        random_list = [random.randint(-10, 10) for _ in range(10)]

        print('None input')
        self.assertRaises(TypeError, quicksort, None)

        print('Empty input')
        self.assertEqual(quicksort([]), [])

        print('One element')
        self.assertEqual(quicksort([1, ]), [1, ])

        print('Two or more elements')
        self.assertEqual(quicksort(random_list), sorted(random_list))

        print('Two or more elements in reverse')
        self.assertEqual(quicksort(random_list, reverse=True),
                         sorted(random_list, reverse=True))

        print('Success: test_quicksort')


def main():
    test = TestQuicksort()
    test.test_quicksort()


if __name__ == "__main__":
    main()
