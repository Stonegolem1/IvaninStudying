print('Задача 1')
import random
n = random.randrange(5, 10, 1)
list1 = []
i = 0
while i != n:
   elem = random.randrange(-16, 16, 1)
   list1.append(elem)
   i += 1
list2 = []
i = 0
while i != n:
    if list1[i] >= 0:
        a = list1[i]**0.5
        if a%1 == 0:
            list2.append(a)
    i += 1
print(list1)
print(list2)


