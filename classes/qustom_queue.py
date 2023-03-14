from classes.node import Node


class Queue:

    def __init__(self, head=None, tail=None):
        """Инициализация экземпляра класса Queue"""
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Добавление элементов в очередь"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """Удаление элементов из очереди по методу FiFo"""
        if self.head is None:
            return None
        deq_element = self.head
        self.head = self.head.next_node
        return deq_element.data


# if __name__ == "__main__":
#     queue = Queue()
#     queue.enqueue('data1')
#     queue.enqueue('data2')
#     queue.enqueue('data3')
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
