from random import randint

def creating_list():
    lst=[]
    for i in range(randint(2, 10)):
        lst.append(randint(0, 10))
    print("before", lst)
    return  bubbel(lst)


def bubbel(ite):
    for i in range(len(ite)):
        for j in range(len(ite)):
    	    if(ite[i] < ite[j]):
               ite[i],ite[j] = ite[j],ite[i]
    print("after", end=" " )
    return  ite
if __name__ == "__main__":
    print(creating_list())

