import unittest

from data_structures.linked_lists import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_append(self):
        print('Test: test_append')
        linked_list = DoublyLinkedList()

        print('Test: None input')
        self.assertRaises(ValueError, linked_list.append, None)

        print('Test: empty list')
        linked_list.append(0)
        self.assertEqual(linked_list.first().data, 0)

        print('Test: general case')
        linked_list = DoublyLinkedList()
        for item in range(5):
            linked_list.append(item)
        for node, item in zip(linked_list, range(5)):
            self.assertEqual(node.data, item)
        print('Success: test_append')

    def test_is_empty(self):
        print('Test: is_empty')
        linked_list = DoublyLinkedList()
        self.assertEqual(linked_list.is_empty(), True)

        for item in range(5):
            linked_list.append(item)

        self.assertEqual(linked_list.is_empty(), False)
        print('Success: test_is_empty')

    def test_insert_after(self):
        print('Test: test_insert_after')
        linked_list = DoublyLinkedList()

        print('Test: None input')
        self.assertRaises(ValueError, linked_list.insert_after, None, None)
        self.assertRaises(TypeError, linked_list.insert_after, 1, None)

        print('Test: insert_after general case')
        linked_list.append(1)
        linked_list.insert_after(2, linked_list.first())
        self.assertEqual(linked_list.first().next.data, 2)
        print('Success: test_insert_after')

    def test_insert_to_front(self):
        print('Test: test_insert_to_front')
        linked_list = DoublyLinkedList()

        print('Test: None input')
        self.assertRaises(ValueError, linked_list.insert_to_front, None)

        print('Test: empty list')
        linked_list.insert_to_front(1)
        self.assertEqual(linked_list.first().data, 1)

        print('Test: general case')
        linked_list = DoublyLinkedList()
        for item in range(3):
            linked_list.insert_to_front(item)
        for node, item in zip(linked_list, reversed(range(3))):
            self.assertEqual(node.data, item)
        print('Success: test_insert_to_front')

    def test_find(self):
        print('Test: test_find')
        linked_list = DoublyLinkedList()

        print('Test: find on an empty list')
        self.assertRaises(ValueError, linked_list.find, 5)

        print('Test: find the last element')
        for item in range(5):
            linked_list.append(item)
        self.assertEqual(linked_list.find(None).data, 4)

        print('Test: find with no matches')
        self.assertRaises(ValueError, linked_list.find, 5)

        print('Test: find general case')
        self.assertEqual(linked_list.find(2).data, 2)
        print('Success: test_find')

    def test_delete(self):
        print('Test: test_delete')
        linked_list = DoublyLinkedList()

        print('Test: None input')
        self.assertRaises(ValueError, linked_list.delete, None)

        print('Test: delete on an empty list')
        self.assertRaises(ValueError, linked_list.delete, 5)

        print('Test: delete general case')
        for item in range(3):
            linked_list.append(item)

        linked_list.delete(1)
        self.assertRaises(ValueError, linked_list.find, 1)
        self.assertEqual(linked_list.first().next.data, 2)

        print('Test: delete with no matches')
        self.assertRaises(ValueError, linked_list.delete, 5)
        print('Success: test_delete')


def main():
    test = TestDoublyLinkedList()
    test.test_append()
    test.test_is_empty()
    test.test_insert_after()
    test.test_insert_to_front()
    test.test_find()
    test.test_delete()


if __name__ == "__main__":
    main()
