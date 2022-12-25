class Observer:
    @staticmethod
    def cash():
        return "this product is in stock"

    @staticmethod
    def notCash():
        return "this no product is in stock"


class Shop(Observer):
    @staticmethod
    def checkingCash():
        TPL = ("apple", "meat", "milk", "tea", "cigarettes")
        if input("input name product. ") in TPL:
            total = Observer.cash()
            return total
        else:
            total = Observer.notCash()
            return total

print(Shop.checkingCash())