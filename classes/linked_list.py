class Node:
    """Инициализация экземпляра класса Node"""

    def __init__(self, data: dict, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        """Инициализация экземпляра класса LinkedList"""
        self.head = None
        self.tail = None
        self.elements = []

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

    def insert_at_end(self, data) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next_node:
            itr = itr.next_node
        itr.next_node = Node(data, None)

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        i_node = self.head
        while i_node is not None:
            self.elements.append(i_node.data)
            i_node = i_node.next_node
        return self.elements

    def get_data_by_id(self, id: int) -> dict:
        """Возвращает первый найденный в LinkedList словарь с ключом id,
        значение которого равно переданному в метод значению.
        Обрабатывает исключения на предмет некорректного ввода данных"""
        self.elements = ll.to_list()
        for element in self.elements:
            try:
                for key, values in element.items():
                    if values == id:
                        return element
            except:
                print("Данные не являются словарем или в словаре нет id.")


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})
    lst = ll.to_list()
    for item in lst: print(item)
    user_data = ll.get_data_by_id(2)
    print(user_data)
    # ll = LinkedList()
    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end('idusername')
    # ll.insert_at_end([1, 2, 3])
    # ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
    # user_data = ll.get_data_by_id(2)
    # print(user_data)
