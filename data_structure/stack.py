class Stack:
    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        if len(self.lst) == 0:
            raise IndexError("pop from empty list")
        else:
            self.lst.pop()
    
    def size(self):
        return len(self.lst)
lst = Stack()
lst.push(3)
lst.push(7)
lst.push(9)
print(lst.size())
lst.pop()
print(lst.size())
