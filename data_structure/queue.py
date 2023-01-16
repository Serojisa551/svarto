class Queue:
    def __init__(self) -> None:
        self.lst = []

    def add(self, item):
        return self.lst.insert(0, item)

    def delet(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

lst = Queue()
lst.add(3)
lst.add(2)
print(lst.lst)
lst.delet()
print(lst.lst)
print(lst.size())