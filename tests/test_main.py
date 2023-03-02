import unittest
from main import Node, Stack


class TestMain(unittest.TestCase):

    def test_node_init(self):
        node_1 = Node(10)
        self.assertEqual(node_1.data, 10)
        self.assertEqual(node_1.new_node, None)

    def test_stack_init(self):
        stack_1 = Stack()
        self.assertEqual(stack_1.top, None)

    def test_stack_push(self):
        node_1 = (10)
        node_2 = Node(5, node_1)
        assert node_2.new_node is node_1
