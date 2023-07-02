#За день машина проезжает n километров. Сколько дней нужно, 
# чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:2

# n = int (input())
# m = int (input())
# print((m + n - 1)//n)

# В некоторой школе решили набрать три новых математических класса и оборудовать 
# кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input())
# b = int(input())
# c = int(input())
# print((a + 1) // 2 + (b + 1) // 2 + (c + 1) // 2)

# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
#   это зависит от того, в какую сторону едет электричка). 
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. 
# Напишите программу, которая будет это делать или сообщать, 
# что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input())
# j = int(input())
# if i == j:
#     print("Нет дополнительной информации")
# else:
#     print(i + j - 1)





# n = int(input())
#  True(1)
#  False(0)
#  and(*)(&&) - и
#  or(+)(||) - или

# # n = 2018
# #    True      *     True      +   False   = 1 * 1 + 0 = 1(True)
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('yes')
# else:
#     print('no')


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
# n = 1
# m = 4
# k = 1
# print(f'{n}\n{m}\n{k}') - вывод  в одну строку







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



# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while


# Input:       5

# Output:    120


# n = int(input("Введите число: "))
# i = 2
# result = 1
# while i <= n:
#     result *= i # result = result * i
#     i += 1
# print(f'{n}! = {result}')


#  0 1 1 2 3 5 8 13 21 34 55

# # 5 -> 6
# # 7 -> error

# 13:23
# Дано натуральное число A > 1. Определите, 
# каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# Input:     5

# Output:  6



# n = int(input())
# n0 = 0 1 2
# n1 = 0
# n2 = 1
# i = 2 # Так как 2 первых числа уже известны это 0 и 1
# while n0 < n:
#     n0 = n1 + n2 1 2 3
#     n1 = n2 1
#     n2 = n0 2 3
#     i += 1
#     if n0 > n:
#         i = 0
# if i != 0:
#     print(i)
# else:
#     print(-1)





#15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
#Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
#Input:	5 -> 5 1 6 5 9
#Output:	1 9
# n = int(input("Введите кол-во арбузов: "))
# x = int(input("Введите массу арбуза: "))
# min_massa, max_massa = x, x
# for i in range(n - 1):
#     x = int(input("Введите массу арбуза: "))
#     if max_massa < x:
#         max_massa = x
#     if min_massa > x:
#         min_massa = x
# print(min_massa, max_massa)



# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, 
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2


# n = int(input("Введите кол-во дней: "))
# count = 0
# max_count = 0
# for i in range(n):
#     temp = int(input("Введите кол-во градусов: "))
#     if temp > 0:
#         count += 1
#     else:
#         count = 0
    
#     if count > max_count:
#         max_count = count
# print(max_count)





# n = int(input("Введите кол-во монет: "))
# count = 0
# max_orel = 0
# max_rehca = 0
# for i in range(n):
#      temp = int(input("Введите стороны монет: "))
#      if temp == 1:
#          max_orel += 1
#      else: temp == 0 
#      max_rehca += 1 
     
#      if max_orel > max_rehca:
#          print(max_rehca)
#      else:
#         print(max_orel) 




# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# a = [1, 1, 2, 0, -1, 3, 4, 4,]
# b = set(a)
# print(len(b))


# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [3, 4, 5, 1, 2]

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# from random import randint as rd
# # as(alias) - псевдоним


# n = int(input("Введите кол-во элементов: "))
# numbers = list() # []
# for i in range(n):
#     numbers.append(rd(1, 51)) # [1; 50]
# print(numbers)
# k = int(input("Введите кол-во элементов для сдвига: "))
# k = k % n

# # [1, 2, 3, 4, 5] k = 3
# #  0  1  2  3  4
# # [3, 4, 5, 1, 2]
# #  2  3  4  0  1
# result = [0] * n
# for i in range(k): # 0 1 2
#     result[i] = numbers[n - k + i]
# for i in range(n - k):
#     result[k + i] = numbers[i]
# print(result)


# Напишите программу для печати всех уникальных значений в словаре. 

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, 
#          {"VIII":"S007"}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# Примечание: Список словарей задан изначально. Пользователь его не вводит

# s = {'name': {'surname': 'Ivanov'}}
# print(name)Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает 
# количество элементов массива, больших предыдущего (элемента с предыдущим номером) 


# Input: [0, -1, 5, 2, 3]


# Output: 2 

# Пояснение: (-1 < 5, 2 < 3)


# Примечание: Пользователь может вводить значения списка или список задан изначально.

# 13:55
# from random import randint as rd


# n = int(input("Введите кол-во элементов: "))
# numbers = list() # []
# count = 0
# for i in range(n):
#     numbers.append(rd(1, 21))
# print(numbers)
# for i in range(1, n):
#     if numbers[i] > numbers[i - 1]:
#         count += 1
# print(count)


# import random

# n = int (input())

# list_1 = [random.randint(1,5) for i in range(1,n)]
# print (list_1)


# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# x =  "a a a b c a a d c d d".split()
# n ={}
# for i in x:
#     if i in n:


# print (type (x))

# stroka = "a a a b c a a d c d d".split()
# print(stroka)
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1

# text = input().split()
# set_result = set()
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))









# Задача No27. Решение в группах
# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure.So if she sells sea shells on the sea shore I'm 
# sure that the shells are sea shore shells
# Output: 13

# Задача 33
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1


n = int (input())
list_1 = [1,3,3,3,4]
number_min = 0
number_max = 0
for i in list_1:

# n = int(input("Введите кол-во оценок: "))
# marks = []
# for i in range(n):
#     mark = int(input("Введите оценку: "))
#     marks.append(mark)
# # print(min(marks), max(marks))
# for i in range(n):  # 0 1 2 3 4... n - 1
#     if marks[i] == max(marks):
#         marks[i] = min(marks)
# print(marks)

# Задача  35
# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым

# Напоминание: 
# Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

# Input: 5
# Output: yes

# n = int(input("Введите число: "))
# f = 1
# for i in range(2, n // 2 + 1):  # [2, 5]
#     if n % i == 0:
#         f = 0

# if f == 0:
#     print("no")
# else:
#     print("yes")

 
 

 
# def reverse_numbers(n):
#     if n == 0:
#         return ''
#     chislo = input()
#     return reverse_numbers(n - 1) + f' {chislo}'


# n = int(input("Введите число: "))
# print(reverse_numbers(n))

# r(2) -> " 4" + " 3" = " 4 3"

