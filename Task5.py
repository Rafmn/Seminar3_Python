# Задача 5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = int(input('Введите число: '))

fib1 = fib2 = 1
list_fib = [0, 1, 1]

for i in range(2, num):
    fib1, fib2 = fib2, fib1 + fib2
    list_fib.append(fib2)

revers_list_fib = list_fib[1:]
revers_list_fib.reverse()
revers_list_fib = [-i for i in revers_list_fib]

print(revers_list_fib + list_fib)