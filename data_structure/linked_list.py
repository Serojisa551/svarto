class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_element = Node(data)
        if self.head == None:
            self.head = new_element
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_element

    def len(self):
        numbers = 0
        current = self.head
        while current:
            numbers += 1
            current = current.next
        return numbers

    def pop(self):
        size = self.len() - 1
        number = 1
        current = self.head
        while current and number != size:
            current = current.next
            number += 1
        current.next = None

    def my_print(self):
        current = self.head
        print("[", end="")
        while current:
            print(current.data, end=",")
            current = current.next
        print("]")


if __name__ == "__main__":
    lst = Linked_List()
    lst.append(5)
    lst.append(4)
    lst.append(3)
    lst.append(2)
    lst.append(1)
    lst.append(0)
    lst.pop()
    lst.my_print()