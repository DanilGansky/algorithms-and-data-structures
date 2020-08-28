import unittest

from data_structures.queue.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        print('Test: test_enqueue')
        queue = Queue()

        print('Test: None input')
        self.assertRaises(ValueError, queue.enqueue, None)

        print('Test: Enqueue to an empty queue')
        queue.enqueue(1)
        self.assertEqual(queue._front.data, 1)
        self.assertEqual(queue._rear.data, 1)

        print('Test: General case')
        queue.enqueue(2)
        self.assertEqual(queue._rear.data, 2)
        queue.enqueue(3)
        self.assertEqual(queue._rear.data, 3)
        queue.enqueue(4)
        self.assertEqual(queue._rear.data, 4)
        print('Success: test_enqueue')

    def test_dequeue(self):
        print('Test: test_dequeue')
        queue = Queue()

        print('Test: Dequeue an empty queue')
        self.assertEqual(queue.dequeue(), None)

        print('Test: Dequeue a queue with one element')
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue._front, None)
        self.assertEqual(queue._rear, None)

        print('Test: General case')
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        print('Success: test_dequeue')

    def test_peek(self):
        print('Test: test_peek')
        queue = Queue()

        print('Test: Peek to an empty queue')
        self.assertEqual(queue.peek(), None)

        print('Test: General case')
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 1)
        print('Success: test_peek')

    def test_is_empty(self):
        print('Test: test_is_empty')
        queue = Queue()

        print('Test: Empty queue')
        self.assertEqual(queue.is_empty(), True)

        print('Test: Not an empty queue')
        queue.enqueue(1)
        self.assertEqual(queue.is_empty(), False)
        print('Success: test_is_empty')


def main():
    test = TestQueue()
    test.test_enqueue()
    test.test_dequeue()
    test.test_peek()
    test.test_is_empty()


if __name__ == "__main__":
    main()
