# Задача 3: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

some_list = [float(i) for i in input('Введите несколько вещественных чисел через пробел: ').split()]
new_list = [i%1 for i in some_list]
max_num = max(new_list)
min_num = min(new_list)
diff_num = round(max_num - min_num, 3)


print(some_list, '->', diff_num)