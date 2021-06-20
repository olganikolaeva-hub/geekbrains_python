# Урок 5. Работа с файлами

# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода
# данных свидетельствует пустая строка.

import sys
new_text = input()
file_object = open('new_file.txt', 'w', encoding = 'utf-8')
while new_text:
    file_object.write(new_text + "\n")
    new_text = input()
file_object.close()

# 2. Создать текстоавый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
# слов в каждой строке.

# Обращаемся к файлу, созданному на предыдущем шаге
file_object = open('new_file.txt' , 'r', encoding = 'utf-8')
words = []
lines = []
for line in file_object.readlines():
    words.append(len(line.split(" ")))
    lines.append(line.replace("\n", ""))
file_object.close()
print(f"Количество строк в файле : {len(lines)} , список с количеством слов в каждой строке : {words}")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
import numpy as np
file_object = open('salary.txt', 'r')
salary = []
for line in file_object.readlines():
    if int(line.split(" ")[1]) < 20000:
        print(f"Сотрудник имеет зарплату меньше 20 тыс. рублей: {line}")
    salary.append(int(line.split(" ")[1]))
file_object.close()
print(f"Средний уровень заработной платы сотрудников: {np.mean(salary)}")

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
russian_dict = {"One": 'Один', "Two": 'Два', "Three" : "Три", "Four": "Четыре"}
with open('example_file.txt', 'r') as file_object:
    with open('new_file.txt', 'w', encoding = 'utf-8') as new_file_object:
        for line in file_object.readlines():
            new_line = []
            new_line.append(russian_dict[line.split(" ")[0]])
            new_line.append(line.split(" ")[1])
            new_line.append(line.split(" ")[2])
            new_file_object.write(" ".join(new_line))
            
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.

with open('file_with_numbers.txt', 'w') as file_object:
    number = input('Введите число: ')
    while number:
        file_object.write(number + "\n")
        number =  input('Введите число: ')

with open('file_with_numbers.txt', 'r') as file_object:
    numbers = []
    for line in file_object.readlines():
        numbers.append(int(line))
    print(f"Сумма чисел в файле равна: {sum(numbers)}")


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были
# все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на
# экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: 30(пр) 

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

subject_dit = {}
with open('subjects.txt', 'r') as file_object:
    for line in file_object.readlines():
        subject_position = line.find(":")
        subject = line[0:subject_position]
        hours = line[subject_position + 1:].rstrip().lstrip().split(" ")
        sum_of_hours = 0
        for hour in hours:
            if hour.find('(') > 0:
                position = hour.find('(')
                sum_of_hours += int(hour[:position])
        subject_dit[subject] = sum_of_hours
print(f'Общее количество занятий по каждому предмету: {subject_dit}')

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма 
# собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать файл, вычислить
# прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если 
# фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import numpy as np
import json
firm = []
firm_dict = {}
average_profit = []
average_profit_dict = {}
for_json = []
with open('firms.txt') as file_object:
    for line in file_object.readlines():
        firm = line.replace("\n", "").split(" ")
        profit = int(firm[-2]) - int(firm[-1])
        firm_dict[firm[0]] = profit
        if profit > 0:
            average_profit.append(profit)
    average_profit_dict['average_profit'] = np.mean(average_profit)
    for_json.append(firm_dict)
    for_json.append(average_profit_dict)

with open('firms_all.txt', 'w') as file_object:
    file_object.write(json.dumps(for_json))
