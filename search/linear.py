from random import randint


def my_print(*object):
    lst = []
    for element in object:
        if type(element) == list:
            print(element)
            break
        elif len(object) == 1:
            print(element)
            break
        else:
            lst.append(element)
    else:
        print(lst)


def creating_list():
    lst = []
    for i in range(randint(2, 10)):
        lst.append(randint(0, 10))
    return lst


def linear(ite, key):
    my_print("lst", ite)
    my_print("key", key)
    for element in ite:
        if key == element:
            return True
    else:
        return False


if __name__ == "__main__":
    my_print(linear(creating_list(), randint(-2, 12)))
