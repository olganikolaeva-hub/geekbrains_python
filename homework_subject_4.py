#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо
# использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо
# запускать скрипт с параметрами.

from sys import argv
#argv - параметры командной строки
script_name, first_param, second_param, third_param = argv
your_salary = (int(first_param) * int(second_param)) + int(third_param)

print(f"Your salary for this month is : {your_salary} ")

#Запуск через терминал
homework4.py 40 1000 20000

#2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
elements = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([elements[i] for i in range(1, len(elements)-1) if (elements[i] > elements[i-1])])

#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
import numpy as np
print([i for i in range (20,240) if (i % 20 == 0) or (i % 21 == 0)])

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно
# использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
dict_numbers = {num: numbers.count(num) for num in numbers}
print([item[0] for item in dict_numbers.items() if item[1] == 1])

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа
# от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
from functools import reduce

def mult(x, y):
    return x * y

numbers = [x for x in range (100, 1001) if x % 2 == 0]
print(reduce(mult, numbers))

#6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть
# бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

import itertools 
def gen_a():
    a = int(input("Введите целое число от 1 до 10: "))
    counter = itertools.count(a, 1)
    b = next(counter)

    while b <= 10:
        print(b)
        b = next(counter)

def gen_b():
    numbers = [1, 2, 3, 4, 5]
    counter = itertools.cycle(numbers)
    b = next(counter)
    n = 1
    
    while n <= 10:
        print(b)
        b = next(counter)
        n = n + 1

print(gen_a())
print(gen_b())

#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен
# создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение
# факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    x = 1
    start = 1
    while x <= n:
        start = start * (x)
        yield start
        x = x + 1

factorial_list = [print(el) for el in fact(5)]
