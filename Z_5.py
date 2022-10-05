#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def lstFib(lst):
    if lst in [1, 2]:
        return 1
    else:
        return lstFib(lst-1) + lstFib(lst-2)

def otrFib(lst):
    if lst == 1 and lst == 2:
        return 1, -1
    else:
        one, two = 1, -1
        for i in range(2, lst):
            one, two = two, one - two
        return two

spisok = [0]
num = int(input('Enter number: '))
for i in range(1, num + 1):
    spisok.append(lstFib(i))
    spisok.insert(0, otrFib(i))
print(f'The list of Fibonacci numbers is equal to = {spisok}')