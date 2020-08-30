import unittest

from data_structures.hash_map import HashMap

from .hash_map import NotEnoughCells


class TestHashMap(unittest.TestCase):
    def test_getitem(self):
        print('Test: test_getitem')
        hash_map = HashMap(10)

        print('Test: get a non-existent item')
        self.assertRaises(KeyError, hash_map.__getitem__, 0)

        print('Test: general case')
        hash_map[0] = 'hello'
        hash_map[1] = 'world'
        hash_map[15] = 'foo'
        hash_map[28] = 'bar'
        self.assertEqual(hash_map[0], 'hello')
        self.assertEqual(hash_map[1], 'world')
        self.assertEqual(hash_map[15], 'foo')
        self.assertEqual(hash_map[28], 'bar')

        print('Test: get deleted item')
        del hash_map[15]
        self.assertRaises(KeyError, hash_map.__getitem__, 15)
        print('Success: test_getitem')

    def test_setitem(self):
        print('Test: test_setitem')
        hash_map = HashMap(10)

        print('Test: general case')
        hash_map[0] = 'hello'
        hash_map[1] = 'world'
        hash_map[15] = 'foo'
        hash_map[28] = 'bar'
        self.assertEqual(hash_map[0], 'hello')
        self.assertEqual(hash_map[1], 'world')
        self.assertEqual(hash_map[15], 'foo')
        self.assertEqual(hash_map[28], 'bar')

        print('Test: set item in filled hashmap')
        hash_map = HashMap(3)
        hash_map[0] = 'hello'
        hash_map[1] = 'world'
        hash_map[15] = 'foo'
        self.assertRaises(NotEnoughCells, hash_map.__setitem__, 28, 'bar')

        print('Test: update item value')
        hash_map[1] = 'World'
        self.assertEqual(hash_map[1], 'World')
        print('Success: test_setitem')

    def test_delitem(self):
        print('Test: test_delitem')
        hash_map = HashMap(10)

        print('Test: general case')
        hash_map[0] = 'hello'
        hash_map[1] = 'world'
        hash_map[15] = 'foo'
        hash_map[28] = 'bar'

        del hash_map[1]
        self.assertRaises(KeyError, hash_map.__getitem__, 1)
        del hash_map[28]
        self.assertRaises(KeyError, hash_map.__getitem__, 28)

        print('Test: delete a non-existent item')
        self.assertRaises(KeyError, hash_map.__delitem__, 80)

        print('Test: delete previously deleted item')
        hash_map[50] = 'item'
        del hash_map[50]
        self.assertRaises(KeyError, hash_map.__delitem__, 50)
        print('Success: test_delitem')

    def test_contains(self):
        print('Test: test_contains')
        hash_map = HashMap(10)
        self.assertEqual(0 in hash_map, False)
        hash_map[0] = 'foo'
        self.assertEqual(0 in hash_map, True)
        del hash_map[0]
        self.assertEqual(0 in hash_map, False)
        print('Success: test_contains')


def main():
    test = TestHashMap()
    test.test_getitem()
    test.test_setitem()
    test.test_delitem()
    test.test_contains()


if __name__ == "__main__":
    main()
