from random import randint


def my_print(*object):
    for element in object:
        print(element)


def creating_list():
    lst = []
    for i in range(randint(2, 10)):
        lst.append(randint(0, 10))
    my_print(lst)
    return lst


def linear(ite, key):
    my_print(key)
    for element in ite:
        if key == element:
            return True
    else:
        return False


if __name__ == "__main__":
    my_print(linear(creating_list(), randint(-2, 12)))
