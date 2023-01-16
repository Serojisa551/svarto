class Node:
    def __init__(self, data, next=None):
        self.set_data(data)
        self.next = next

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class Linkid_List:
    def __init__(self):
        self.head = None

    # def set_head(self, head):
    #     self.__head = head

    # def get_head(self):
    #     return self.__head

    def append(self, data):
        new_element = Node(data)
        if self.head == None:
            self.head = new_element.get_data()
            return
        current = self.head
        while current.netx:
            current = current.next
        current.next = new_element

if __name__ == "__main__":
    lst = Linkid_List()
    lst.append(5)
    print(lst.head)
    lst.append(4)
    print(lst.head)


