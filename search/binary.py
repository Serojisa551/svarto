from random import randint
from linear import creating_list, my_print


def bubbel(ite):
    for i in range(len(ite)):
        for j in range(len(ite)):
            if (ite[i] < ite[j]):
                ite[i], ite[j] = ite[j], ite[i]
    my_print(ite)
    return ite


def binary(ite, key):
    my_print("key", key,)
    length = len(ite)
    index = len(ite) - 1
    bottom_line = 0
    middle = (bottom_line + index) // 2
    while length > 0:
        if length == 1:
            if ite[middle] == key:
                return True
            else:
                return False
        elif ite[middle] == key:
            return True
        else:
            if ite[middle] > key:
                index = middle - 1
            elif ite[middle] < key:
                bottom_line = middle + 1
        middle = (bottom_line + index) // 2
        length //= 2
if __name__ == "__main__":
    modul = creating_list()
    modul =bubbel(modul)
    modul = binary(modul, key = randint(0, 10))
    my_print(modul)

def Test_binary():
    for i in range(100):
        if None == creating_list():
            return False
    else:
        return True


# my_print(Test_binary())
