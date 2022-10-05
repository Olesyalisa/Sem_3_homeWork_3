#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

size = int(input('Enter size: '))
lst = []
newLst = []
for i in range(size):
    lst.append(randint(1, 10))

for i in range(len(lst)):
    if size > len(lst)/2 and i < len(lst)/2:
        size -= 1
        count = lst[i] * lst[size]
        newLst.append(count)
        i += 1
        print(lst, newLst)