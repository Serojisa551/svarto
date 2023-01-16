class Node:
    def __init__(self, data, next=None):
        self.set_data(data)
        self.next = next

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class Tree:
    def __init__(self):
        self.haed = None
        self.left = None
        self.right = None

# TODO(
    def add(self, item):
        new_node = Node(item)
        if self.haed:
            if new_node < self.haed:
                self.left = new_node
            elif new_node > self.haed:
                self.right = new_node
        else:
            self.haed = new_node #)