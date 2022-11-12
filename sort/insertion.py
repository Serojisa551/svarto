from random import randint


def creating_list():
    lst = []
    for i in range(randint(2, 10)):
        lst.append(randint(0, 10))
    print("before", lst)
    return inserion(lst)


def inserion(ite):
    for i in range(1, len(ite)):
        for j in range(i, 0, -1):
            if ite[j] < ite[j - 1]:
                ite[j], ite[j-1] = ite[j-1], ite[j]
    print("after", end="")
    return ite


if __name__ == "__main__":
    print(creating_list())
