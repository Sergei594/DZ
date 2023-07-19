# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# f = int(input())
# y = f // 1000
# v = y // 100   #- 1 цифра
# z = y % 100
# j = z // 10     #- 2 цифра
# x = z % 10      #- 3 цифра
# b = v+j+x
# print (b)
# n = f % 1000
# a = n // 100   #- 9 цифра
# g = n % 100     #- 16 цифра
# q = g // 10     #- 1 цифра
# c = g % 10      #- 6 цифa
# d = a+q+c
# print (d)

# if b == d:
#      print('yes')
# else:
#      print('no')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# f = int(input())
# n = f / 3
# f = n * 2
# v = f - n
# x = v / 2
# t = x
# print ("Петя", x)
# print ("Катя", f)
# print ("Сережа", t)

# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# f = int(input())
# n = f // 100
# v = f % 100
# g = v // 10
# j = v % 10
# print (n + j + g)
# print (n)
# print (v)
# print (g)
# print (j)


# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
# n = int(input())
# m = int(input())
# k = int(input())
# if n * m > k and (n % k == 0 or m % k == 0):
#     print('yes')
# else:
#     print('no')

# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть



# import random

# from random import randint

# amount_coin = int(input('введите количество монет: '))

# m = 0
# k = 0
# coins = [0, 1]
# for i in range(amount_coin):
#     random.shuffle(coins)
#     print(f'все монеты{coins}')
#     if int(coins[0]) == 0:
#         k += 1
#     if int(coins[0]) == 1:
#         m += 1
# print(f'всего монет {m, k}')

# if m > k:
#     ans = k
# else:
#     ans = m

# print(f"минимальное количество монет, которые нужно перевернуть {ans}")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
                                                                                                                                                        
# Помогите Кате отгадать задуманные Петей числа.

# S = int(input('Введите сумму чисел: '))
# P = int(input('Введите произведение чисел: '))

# X = (S-int((S**2-4*P)**0.5))//2
# Y = S - X
# if X<=1000 and Y<=1000:
#     print('неверные числа')
# print(f'числа задуманные Петей{X, Y}')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

# N = int(input('Введите целое число больше 1: '))
# k=1
# while k<=N:
#      print(k,end=' ')
#      k=k*2


# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


# import random

# n = int (input())
# list_1 = [random.randint(1,5) for i in range(0,n)]
# print (list_1)
# x = int (input())
# result = 0

# for i in list_1:
#     if i == x:
#         result +=1
#     else: result = 0 
    
# print(result)


# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X 


# import random

# n = int (input())
# list_1 = [random.randint(1,n) for i in range(0,n)]
# print (list_1)
# x = int (input())
# result = x

# for i in list_1:
#     if i == x:
#         result = x-1
#     else: x-1
    
# print(result)


# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются 
# так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; 
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы. 

# slovar = {"AEIOULNSTR":1,"DG":2,"BCMP":3,"FHVWY":4,"K":5,"JX":8,"QZ":10}
# word = input("Введите слово")
# count = 0
# for i in word:
#     for j in slovar:
#         if i in j:
#             count += slovar[j]
# print(count)
    

# ПРИМЕР

#     bonus = {'qwertyuiop': 1, 'asdfghjkl': 2, 'zxcvbnm': 3} 
#word = input("Введите слово")
#  count = 0
# for i in word:
#     for j in bonus:
#         if i in j:
#             count += bonus[j]
# print(count)


# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


# from random import randint
# n_set1 = set(randint(1, 10) for i in range(int(input("Введите кол-во элементов первого множества: "))))
# print(n_set1)
# m_set2 = set(randint(1, 10) for i in range(int(input("Введите кол-во элементов второго множества: "))))
# print(m_set2)
# s_set = sorted(n_set1.intersection(m_set2))
# print(s_set)
# c = input()
# set_1 = set()
# for i in range(6): # (b)
#     set_1.add(int(input("Введите число: ")))
# print(set_1)

# b = input()
# set_2 = set()
# for i in range(6): # (b)
#     set_2.add(int(input("Введите число: ")))
# print(set_2)

# set_3 = sorted(set_1.intersection(set_2))
# print(set_3)

# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 
# a = int(input("Ведите первое число:"))
# b = int(input("Ведите второе число:"))
# def summa(a, b):
#     a += 1
#     b -= 1
#     if b > 0:
#         return summa(a, b)
#     else:
#         return a
# print (summa(a, b))




# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


# a = int(input("Ведите первое число:"))
# b = int(input("Ведите степень числа:"))

# def stepen(a, b):
#     if b == 0:
#         return 1
#     return a * stepen(a, b - 1)
# print (stepen(a, b))

# добавление значений в список(множество)
# b = input()
# set_1 = set()
# for i in range(5(b)):
#     set_1.add(int(input("Введите число: "))
# print(set_1)


# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# a0 = int(input("Введите начальное значение: "))
# d = int(input("Введите разность(ариф. прогрессии): "))
# count = int(input("Введите кол-во элементов: "))
# for i in range(count):
#     print(a0, end=' ')
#     a0 += d




# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# list_2 = []
# min = 15
# max = 2

# for i in range(len(list_1)):
#     if min <= list_1[i] <= max:
#         print(i, end=' ') -       не работает


# list_1 = [-5, 9, 0,  -2, 1, 48,  10, 2,  -9, 8, 10, -9,  -55, -5, 70]
# list_2 = []
# max = 10
# min = 0
# for i in range(len(list_1)):
#     if list_1[i] > min and list_1[i] < max:
#         list_2.append(i)
# print(list_2)


# черника
# n = int(input("Введите кол-во кустов: "))
# weight = [int(i) for i in input("Введите кол-во ягод на каждом кусте: ").split()][:n]
# result = [weight[i - 1] + weight[i] + weight[(i + 1) % n] for i in range(len(weight))]
# print(max(result))




# Задача 34:  Винни-Пух попросил Вас посмотреть, 
# есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
# def vinni(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         result = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 result += 1
#         list_1.append(result)
#     return len(list_1) == list_1.count(list_1[0])

# print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')

# str = input()
# if vinni(str):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>3}" for x in i])

# print_operation_table(lambda x, y: x * y)