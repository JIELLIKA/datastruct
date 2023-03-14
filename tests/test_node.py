import unittest
from classes.node import Node


class TestMain(unittest.TestCase):

    def test_node_init(self):
        node_1 = Node(10)
        self.assertEqual(node_1.data, 10)
        self.assertEqual(node_1.next_node, None)