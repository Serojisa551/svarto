from random import randint
from insertion import my_print

def creating_list():
    lst=[]
    for i in range(randint(2, 10)):
        lst.append(randint(0, 10))
    my_print("before", lst)
    return  bubble(lst)


def bubble(ite):
    for i in range(len(ite)):
        for j in range(len(ite)):
    	    if(ite[i] < ite[j]):
               ite[i],ite[j] = ite[j],ite[i]
    my_print("after", end=" " )
    return  ite
if __name__ == "__main__":
    my_print(creating_list())

