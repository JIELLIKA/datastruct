class Node:

    def __init__(self, data, new_node=None):
        self.data = data
        self.new_node = new_node


class Stack:

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_node = Node(data)
        new_node.new_node = self.top
        self.top = new_node


n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
print(n2.new_node)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.new_node.data)
print(stack.top.new_node.new_node.data)
print(stack.top.new_node.new_node.new_node)
print(stack.top.new_node.new_node.new_node.data)
