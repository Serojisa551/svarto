from insertion import my_print
from insertion import creating_list


def bubble(ite):
    for i in range(len(ite)):
        for j in range(len(ite)):
            if (ite[i] < ite[j]):
                ite[i], ite[j] = ite[j], ite[i]
    my_print("after")
    return ite


if __name__ == "__main__":
    my_print(bubble(creating_list()))
