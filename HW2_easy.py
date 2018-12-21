print('Задача 1')
fruit = ['арбуз', 'дыня', 'виноград', 'гранат', 'персик']
i=0
while i!= len(fruit):
    i+=1
    print(f'{i}. {fruit[i-1]:>10}')

print('Задача 2')
list1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 'no', 'yes', 'no']
list2 = [1, 2, 3, 'no']
print(list1)
print(list2)
i=0
while i != len(list2):
    j = 0
    while j != len(list1):
       if list2[i] == list1[j]:
           list1.remove(list2[i])
       else:
           j += 1
    i += 1
print(list1)

print('Задача 3')
import random
n = random.randrange(5, 10, 1)
list1 = []
i = 0
while i != n:
   elem = random.randrange(1, 100, 1)
   list1.append(elem)
   i += 1
i = 0
list2 = []
while i != len(list1):
    if list1[i] % 2 == 0:
        list2.append(list1[i]/4)
    else:
        list2.append(list1[i]*2)
    i += 1
print(list1)
print(list2)