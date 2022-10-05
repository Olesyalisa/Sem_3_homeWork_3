#Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = []
lst = list(map(float, input('Enter digits - interval: ').split()))
count = [round(i % 1,2) for i in lst if i % 1 != 0]
print(max(count) - min(count))