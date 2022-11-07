from random import randint
lst=[]

for i in range(randint(2, 10)):
    lst.append(randint(0, 10))
print("before", lst)


def inserion(ite):
   for i in range(1, len(ite)):
       for j in range(i, 0 , -1):
          if ite[j] <ite[j - 1]:
             ite[j], ite[j-1] = ite[j-1], ite[j] 
                
   return ite

print("after", inserion(lst))
