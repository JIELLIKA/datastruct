import unittest
from classes.qustom_queue import *


class TestQustom_queue(unittest.TestCase):


    def test_queue_init(self):
        queue_1 = Queue()
        self.assertEqual(queue_1.head, None)
        self.assertEqual(queue_1.tail, None)

    def test_queue_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        deq_element = queue.dequeue()
        deq_element_2 = queue.dequeue()
        deq_element_3 = queue.dequeue()
        deq_element_4 = queue.dequeue()
        self.assertEqual('data1', deq_element)
        self.assertEqual('data2', deq_element_2)
        self.assertEqual('data3', deq_element_3)
        self.assertEqual(None, deq_element_4)