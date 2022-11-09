from random import randint
lst = []


def creating_list():
    lst = []
    for i in range(randint(2, 10)):
        lst.append(randint(0, 10))
    print("before", lst)
    return selection(lst)


def selection(lst):
    for i in range(len(lst)):
        modul = i
        for j in range(i + 1, len(lst)):
            if lst[modul] > lst[j]:
                modul = j
        lst[i], lst[modul] = lst[modul], lst[i]
    print("after", end="")
    return lst


if __name__ == "__main__":
    print(creating_list())
