import unittest
from classes.linked_list import *


class TestMain(unittest.TestCase):

    def test_node_init(self):
        node_1 = Node({'id': 1})
        self.assertEqual(node_1.data, {'id': 1})
        self.assertEqual(type(node_1.data), dict)
        self.assertEqual(node_1.next_node, None)

    def test_linkedlist_init(self):
        ll = LinkedList()
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_linkedlist_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'bi': 2})
        self.assertEqual(ll.head.data, {'bi': 2})
        self.assertEqual(ll.head.next_node.data, {'id': 1})

    def test_linkedlist_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 1})
        ll.insert_at_end({'bi': 2})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.head.next_node.data, {'bi': 2})

    def test_linkedlist_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 5, 'username': 'name_1'})
        ll.insert_at_end({'id': 6, 'username': 'name_2'})
        lst = ll.to_list()
        self.assertEqual(lst, [{'id': 5, 'username': 'name_1'}, {'id': 6, 'username': 'name_2'}])

