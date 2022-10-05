#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('enter: '))
newNumber = ''
while number != 0:
    newNumber += str(number % 2)
    number //= 2
print(newNumber)