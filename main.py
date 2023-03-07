class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """Добавляет элемент в конец списка"""
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """Удаляет последний элемент из списка"""
        if self.top is None:
            return
        value = self.top.data
        self.top = self.top.next_node
        return value


if __name__ == "__main__":
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()
    print(stack.top.data)
    print(data)