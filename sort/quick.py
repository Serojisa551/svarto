from random  import randint

lst = []

for i in range(randint(2,10)):
   lst.append(randint(-10, 10)

def quick(ite):
    if len(ite) > 1:
      reference_element = ite[randint(0,len(ite) - 1)]
      less = [i for i in ite if i < reference_element]
      equal = [i for i in ite if i == reference_element]
      more = [i for i in ite if i > reference_element]
      function_keys = quick(less) + equal + quick(more)
    else:
       return function_keys

quick(lst)
