from random import randint
lst=[]
for i in range(randint(2, 10)):
   lst.append(randint(0, 10))
print("before",lst)


def bubbel(ite):
    for i in range(len(lst)):
        is_assorted = True
        for j in range(len(lst)):
    	    if(lst[i] < lst[j]):
               lst[i],lst[j] = lst[j],lst[i]
              # is_assorted = False
        #if is_assorted == True:
         #  return "mtav",lst
    return  lst


print("after", bubbel(lst))

