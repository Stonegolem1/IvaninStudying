print('Task 1')
import random
n = random.randrange(5, 10, 1)
print(n)
i = 0
list1 = []
while i != n:
    list1.append(random.randrange(0, 20, 1))
    i += 1
print(list1)
list2 = [x*x for x in list1]
print(list2)
print('')
print('Task2')
fruit1 = ['яблоко', 'дыня', 'арбуз', 'манго', 'маракуйя', 'манго']
fruit2 = ['абрикос', 'арбуз', 'арбуз', 'манго', 'маракуйя', 'виноград']
print(fruit1)
print(fruit2)
fruit3 = [f for f in fruit2 if f in fruit1]
fruit3 = set(fruit3)
print(fruit3)
print('')
print('Task3')
list1 = range(-10, 30, 1)
print(list1)
list2 = [n for n in list1 if n%3==0 and n>0 and n%4!=0]
print(list2)

