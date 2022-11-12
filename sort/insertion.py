from random import randint


def my_print(*object):
    for element in object:
        print(element)


def creating_list():
    lst = []
    for i in range(randint(2, 10)):
        lst.append(randint(0, 10))
    my_print("before", lst)
    return lst


def insertion(ite):
    for i in range(1, len(ite)):
        for j in range(i, 0, -1):
            if ite[j] < ite[j - 1]:
                ite[j], ite[j-1] = ite[j-1], ite[j]
    my_print("after")
    return ite


if __name__ == "__main__":
    my_print(insertion(creating_list()))
