# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# import random
# import os

# os.system('cls')

# n = int(input('Из скольки элементов должен состоять список?: '))

# def calc_sum (list):
#     sum = 0
#     index = 1
#     while index <= (len(list) - 1):
#         sum += list[index]
#         index += 2
#     return sum

# some_list = [random.randint(0, 10) for _ in range(n)]
# print(f'\nСозданный список имеет вид: {some_list}')
# print(f'\nСумма элементов, стоящих на нечётных позициях списка: {calc_sum(some_list)}\n' )

# ***************************************************************************************************************************************

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import os
# import random

# os.system('cls')

# n = int(input('Из скольки элементов должен состоять список?: '))

# some_list = [random.randint(0, 10) for _ in range(n)]
# print(f'\nСозданный список имеет вид: {some_list}')

# def create_list(list):
#     if len(list) % 2 == 0: count = int(len(list) / 2)
#     else: count = int(len(list) / 2) + 1
#     start_index = 0
#     last_index = len(list) - 1
#     result_list = []
#     for _ in range(count):
#         result_list.append(list[start_index] * list[last_index])
#         start_index += 1
#         last_index -= 1
#     return result_list

# print(f'\nРезультирующий список имеет вид: {create_list(some_list)}\n')

# ******************************************************************************************************************************************

# Задача 3. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import os
# import random

# os.system('cls')

# n = int(input('Из скольки элементов должен состоять список?: '))

# some_list = [round(random.uniform(0.0, 10.0), 2) for _ in range(n)]
# print(f'\nСозданный список имеет вид: {some_list}')

# def find_max_or_min(findMax, list):
#     if  findMax == True:
#         max = float('0.' + str(list[0]).split('.')[1])
#         for elem in list:
#             current = float('0.' + str(elem).split('.')[1])
#             if current > max: max = current
#         return max
#     else:
#         min = float('0.' + str(list[0]).split('.')[1])
#         for elem in list:
#             current = float('0.' + str(elem).split('.')[1])
#             if current < min: min = current
#         return min

# print(f'\nРазница м/у максимальной и минимальной дробной частью = {find_max_or_min(True, some_list) - find_max_or_min(False, some_list)}\n') 

# ******************************************************************************************************************************************

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# import os

# os.system('cls')

# n = int(input('Напишите десятичное число для преобразования: '))
# result_str = ''

# def convert_to_dec (x):
#     global result_str
#     if x == 2:
#         result_str += '01'
#         return
#     result_str += str(x % 2)
#     convert_to_dec(int(x / 2))

# convert_to_dec(n)
# print(f'\nДвоичный вид Вашего числа: {result_str[::-1]}\n')

# ******************************************************************************************************************************************

# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# import os

# os.system('cls')

# n = int(input('Введи число N: '))

# list_pos = [0, 1]
# list_neg = []
# index = 2

# for _ in range (n - 1):
#     list_pos.append(list_pos[index - 1] + list_pos[index - 2])
#     index += 1

# i = len(list_pos) - 1

# while i > 0:
#     if i % 2 == 0:
#         list_neg.append(list_pos[i] * -1)
#     else:
#         list_neg.append(list_pos[i])
#     i -= 1

# print(f'\nCписок Негафибоначчи: {list_neg + list_pos}\n')