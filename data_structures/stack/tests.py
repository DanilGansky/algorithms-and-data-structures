import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    stack = Stack()

    def test_push_pop_peek(self):
        print('Test: test_push_pop_peek')
        print('Test: Empty stack')
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.peek(), None)

        print('Test: More than one element')
        for item in [-5, 7, 0]:
            self.stack.push(item)

        self.assertEqual(self.stack.peek(), 0)
        self.assertEqual(self.stack.pop(), 0)
        self.assertEqual(self.stack.pop(), 7)
        self.assertEqual(self.stack.pop(), -5)
        print('Success: test_push_pop_peek')

    def test_iter_find_is_empty(self):
        print('Test: test_iter_find_is_empty')
        for item in [-5, 7, 0]:
            self.stack.push(item)

        print('Test: __iter__')
        for node, item in zip(self.stack, [0, 7, -5]):
            self.assertEqual(node.data, item)

        print('Test: find')
        self.assertEqual(self.stack.find(7).data, 7)
        self.assertRaises(ValueError, self.stack.find, 9)

        print('Test: is_empty')
        self.assertEqual(self.stack.is_empty(), False)
        for _ in self.stack:
            self.stack.pop()
        self.assertEqual(self.stack.is_empty(), True)
        print('Success: test_iter_find_is_empty')


def main():
    test = TestStack()
    test.test_push_pop_peek()
    test.test_iter_find_is_empty()


if __name__ == "__main__":
    main()
