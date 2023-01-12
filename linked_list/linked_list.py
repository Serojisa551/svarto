class Node:
    def __init__(self, data):
        self.set_data(data)
        self.next = None

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def __str__(self):
        return f"[{self.get_data()}]-> {self.next}"


class Linkid_List:
    def __init__(self):
        self.set_head(None)

    def set_head(self, head):
        self.__head = head

    def get_head(self):
        return self.__head


if __name__ == "__main__":
    head_list = Linkid_List()
    module = Node(1)
    head = head_list.get_head()
    head = module
    for i in range(2, 5):
        module.next = Node(i)
        module = module.next

    print(head)
