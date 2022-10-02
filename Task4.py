# Задача 4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Введите число: '))
list_nums = []

while num > 1:
    a_num = num % 2
    list_nums.append(str(a_num))
    num = int(num / 2)

list_nums.append(str(num))
list_nums.reverse()


print(''.join(list_nums))
