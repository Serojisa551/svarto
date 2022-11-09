from random import randint


def creating_list():
    lst = []
    for i in range(randint(2, 10)):
        lst.append(randint(0, 10))
    print(lst)
    return lst


def linear(ite, key):
    print(key)
    for element in ite:
        if key == element:
            return True
    else:
        return False


if __name__ == "__main__":
    print(linear(creating_list(), randint(-2, 12)))
