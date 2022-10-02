# Задача 2: Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

some_list = [int(i) for i in input('Введите несколько чисел через пробел: ').split()]
pair_list = []

if len(some_list) % 2 == 0:                  # Вычисление середины длины созданного списка
    len_half_some_list = len(some_list) / 2
else:
    len_half_some_list = int(len(some_list) / 2 + 1)

for i in range(len_half_some_list):
    num = some_list[i] * some_list[-i - 1]
    pair_list.append(num)


print(some_list, '->', pair_list)