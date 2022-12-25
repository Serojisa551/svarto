class Iterator:
    @staticmethod
    def f(lst):
        for i in lst:
            print(i)
        return "Done"

class List_: 
    def __init__(self, itr):
        self.itr = itr

lst = List_([1, 2, 3, 4, 5])        
print(Iterator.f(lst.itr))