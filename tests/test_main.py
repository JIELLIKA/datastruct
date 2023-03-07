import unittest
from main import *


class TestMain(unittest.TestCase):

    def test_node_init(self):
        node_1 = Node(10)
        self.assertEqual(node_1.data, 10)
        self.assertEqual(node_1.new_node, None)

    def test_stack_init(self):
        stack_1 = Stack()
        self.assertEqual(stack_1.top, None)

    def test_stack_push(self):
        stack_1 = Stack()
        stack_1.push('test_data1')
        stack_1.push('test_data2')
        stack_1.push('test_data3')
        self.assertEqual(stack_1.top.new_node.data, 'test_data2')
        self.assertEqual(stack_1.top.new_node.new_node.data, 'test_data1')
        self.assertEqual(stack_1.top.new_node.new_node.new_node, None)

    def test_stack_pop_one(self):
        stack_2 = Stack()
        stack_2.push('test_data1')
        data1 = stack_2.pop()
        self.assertEqual(data1, 'test_data1')
        self.assertEqual(stack_2.top, None)


    def test_stack_pop_two(self):
        stack_3 = Stack()
        stack_3.push('test_data1')
        stack_3.push('test_data2')
        data2 = stack_3.pop()
        self.assertEqual(data2, 'test_data2')
        self.assertEqual(stack_3.top.data, 'test_data1')

