class Node:
    """Инициализация экземпляра класса Node"""
    def __init__(self, data: dict, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:

    def __init__(self):
        """Инициализация экземпляра класса LinkedList"""
        self.head = None
        self.nail = None


    def insert_beginning(self, data):
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data, self.head)
        self.head = node


    def print_ll(self):
        """Вывод в консоль данных из односвязанного списка"""
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node
        ll_string += ' None'
        print(ll_string)

    def insert_at_end(self, data):
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next_node:
            itr = itr.next_node

        itr.next_node = Node(data, None)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    ll.print_ll()