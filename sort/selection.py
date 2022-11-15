from random import randint
from insertion import my_print
from insertion import creating_list
 

def selection(lst):
    for i in range(len(lst)):
        modul = i
        for j in range(i + 1, len(lst)):
            if lst[modul] > lst[j]:
                modul = j
        lst[i], lst[modul] = lst[modul], lst[i]
    my_print("after")
    return lst


if __name__ == "__main__":
    my_print(selection(creating_list()))
