### Урок 3. Функции ##########################################################################################################

#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
#пользователя, предусмотреть обработку ситуации деления на ноль.

def devision():
    a = int(input("Введите числитель: "))
    b = int(input("Введите знаменатель: "))
    if b == 0:
        return False
    else:
        return a/b

#Проверяем, как работает функция:
dev =  devision()
print(dev)

#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город
#проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о
#пользователе одной строкой.
def user_data(name, surname, date_of_birth, city, email, phone):
    print(f"Пользователь указал следующие анкетные данные: {name}, {surname}, {date_of_birth}, {city}, {email}, {phone}")

#Проверка:
user_data(name = 'Иван', surname = 'Иванов', date_of_birth = '01.01.2010', city = 'Москва', email = 'ivanov@gmail.com', \
          phone = '890111111111')

#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    list_of_arguments = [a, b, c]
    list_of_arguments.sort(reverse = True)
    return sum(list_of_arguments[:2])

#Проверка 
my_func(2,3,5)


#4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
#числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без
#встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более
#сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    if x <= 0:
        return(f"Введенное число {x} не является положительным")
    if type(y) != int:
        return(f"Введенное число {y} не является целым")
    else:
        return(f"Возведение числа {x} в степень {y} равно {x ** y}")

#Проверка 
my_func(x=2, y=-2)

#использование цикла

def my_func_2(x, y):
    if x <= 0:
        return(f"Введенное число {x} не является положительным")
    if type(y) != int:
        return(f"Введенное число {y} не является целым")
    if y >= 0:
        return(f"Введенное число {y} не является отрицательным")
    else:
        if y*(-1) > 0:     
            n = 2
            x_temp = x
            while n <= y*(-1):
                x_temp = x_temp * x
                n = n + 1
            return(f"Возведение числа {x} в степень {y} равно {1/x_temp}")
        else:
            return(f"Возведение числа {x} в степень {y} равно {1/x}") 
#Проверка 
my_func(x=2, y=-2)

#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
#Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
#добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
#после этого завершить программу.

def string_of_numbers():
    numbers = input("Введите числа, разделенные пробелом: ")
    numbers = numbers.split(" ")
    int_numbers = []
    for n in numbers:
        if n.isdigit() == True:
            int_numbers.append(int(n))
    return sum(int_numbers)


a = string_of_numbers()
print(a)
b = string_of_numbers()
print(int(a) + int(b))


#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой
#буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из
#латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
#Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    return word.capitalize()

#Проверка
int_func('привет')

def seq_of_words(words):
    words = words.split(" ")
    new_seq_of_words = []
    for word in words:
        new_seq_of_words.append(int_func(word))
    return (" ").join(new_seq_of_words)

#Проверка
seq_of_words('привет саша как дела')