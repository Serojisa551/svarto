def bubble(ite):
    for i in range(len(ite)):
        for j in range(len(ite)):
            if ite[i] < ite[j]:
                ite[i], ite[j] = ite[j], ite[i]
    return ite


def insertion(ite):
    for i in range(1, len(ite)):
        for j in range(i, 0, -1):
            if ite[j] < ite[j - 1]:
                ite[j], ite[j - 1] = ite[j - 1], ite[j]
    return ite


def selection(lst):
    for i in range(len(lst)):
        modul = i
        for j in range(i + 1, len(lst)):
            if lst[modul] > lst[j]:
                modul = j
        lst[i], lst[modul] = lst[modul], lst[i]
    return lst
