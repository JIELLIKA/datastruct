class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


# if __name__ == "__main__":
#     node_1 = Node(5)
#     node_2 = Node(10, node_1)
#     print(node_2.data)
#     print(node_2.next_node.data)