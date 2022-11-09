from random import randint


def creating_list():
    lst = []
    for i in range(randint(2, 10)):
        lst.append(randint(0, 10))
    return bubbel(lst)


def bubbel(ite):
    for i in range(len(ite)):
        for j in range(len(ite)):
            if (ite[i] < ite[j]):
                ite[i], ite[j] = ite[j], ite[i]
    print(ite)
    return binary(ite)


def binary(ite, key=randint(0, 10)):
    print("key -", key)
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


print(creating_list())


def Test_binary():
    for i in range(100):
        if None == creating_list():
            return False
    else:
        return True


#print(Test_binary())
