# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и
# той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# from random import randint
# countN = int(input("Enter the number of coins: "))
# tails = 0
# eagle = 0
# count = 0
# for i in range(countN):
#     x = randint(0, 1)
#     if x == 0:
#         eagle += 1
#     else:
#         tails += 1
#     print(x)
# if eagle >= tails:
#     count = countN - eagle
# else:
#     count = countN - tails
# print('Minimum number of coins to flip:', count)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# s = int(input('Enter the sum of the numbers: '))
# p = int(input('Enter the product of the numbers: '))
# a = 0
# for x in range(s):
#     y = s - x
#     if x + y == s and x * y == p:
#         a += 1
#         print(x, y)
#         break
# if a == 0:
#     print('You entered incorrect data')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Enter the number N: '))
k = 0
res = 1
while res < n+1:
    print(res, end=' ')
    k += 1
    res = 2 ** k