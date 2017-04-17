import unittest
import inspect

from HashTable import HashTable


class HashTableTest(unittest.TestCase):
    def setUp(self):
        self.table_size = 11
        self.hash_table = HashTable(self.table_size)

    def show(self, msg=None):
        print(inspect.stack()[1][3], msg)
        print(self.hash_table.slots)


    def test_hash_function(self):
        key = 'cat'
        expected = 3
        actual = self.hash_table.hash(key)
        self.assertEqual(expected, actual)
        self.show(actual)

    def test_put_unique_key(self):
        key = 'cat'
        data = 'pet'
        self.hash_table.put(key, data)
        hash_value = self.hash_table.hash(key)
        l = self.hash_table.slots[hash_value]
        current = l.find(key)
        self.assertEqual(data, current.value)
        self.show((current.key, current.value))

    def test_put_two_unique_keys(self):
        key1 = 'key1'
        key2 = 'key2'
        value1 = 'value1'
        value2 = 'value2'
        self.hash_table.put(key1, value1)
        self.hash_table.put(key2, value2)
        hash_value1 = self.hash_table.hash(key1)
        hash_value2 = self.hash_table.hash(key2)
        l1 = self.hash_table.slots[hash_value1]
        l2 = self.hash_table.slots[hash_value2]

        self.show([(l1.find(key1).key, l1.find(key1).value),(l2.find(key2).key, l2.find(key2).value)])

    def test_put_override(self):
        key = 'cat'
        data = 'pet'
        self.hash_table.put(key, data)
        hash_value = self.hash_table.hash(key)
        l = self.hash_table.slots[hash_value]
        current = l.find(key)
        current.value = 'not a pet'
        self.assertEqual('not a pet', current.value)
        self.show((current.key, current.value))

    def test_remove_existing_key(self):
        key = 'cat'
        data = 'pet'
        self.hash_table.put(key, data)
        self.hash_table.remove(key)

        hash_value = self.hash_table.hash(key)
        slot = self.hash_table.slots[hash_value]
        self.assertIsNone(slot.find(key))
        self.show()

    def test_remove_none_existing_key(self):
        key = 'cat'
        data = 'pet'
        self.hash_table.put(key, data)

        with self.assertRaises(Exception):
            self.hash_table.remove('dog')

    def test_show(self):
        self.hash_table.put('key1', 'value1')
        self.hash_table.put('key2', 'value2')
        self.hash_table.put('key3', 'value3')
        self.hash_table.show()