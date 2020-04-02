class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def init_tree():
    new_node = Node("A")
    root = new_node

    new_node = Node("B")
