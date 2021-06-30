# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class MyData:
    def __init__(self, txt):
        self.txt = txt
    @classmethod
    def to_number(cls, txt):
        return int(txt.replace("-",""))
    @staticmethod
    def validation(txt):
        text = txt.split("-")
        if (int(text[0]) <= 0 or int(text[0]) > 31) or (int(text[1]) <=0 or int(text[1]) > 12):
            print("Неверный формат даты")
 
#Проверка
number = MyData.to_number('01-01-1984')
print(type(number))
print(MyData.validation('01-14-1984'))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
# пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class MyDivisionError(Exception):
    def __init__(self, text):
        self.text = text

def division(x, y):
    try:
        x = int(x)
        y = int(y)
      
        if y == 0:
            raise MyDivisionError("Делитель равен нулю. Операция невозможна.")
        else:
            print(f"При делении {x} на {y} получится {x/y}")
    except ValueError:
        print("Вы ввели не число")
    except MyDivisionError as err:
        print(err)
   
#Проверка
division(5, "привет")
division(5, 0)
  
# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
# работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом
# работа скрипта не должна завершаться.

class MyException(Exception):
    def __init__(self, text):
        self.text = text

def func():
    my_number = input("Введите число: ")
    my_list = []
    while my_number != 'stop':
        try:  
            if my_number.isalpha():
                raise MyException("Вы ввели не число. Продолжите ввод данных")
            
            else:
                my_list.append(my_number)
                my_number = input("Введите число: ")
                
        except MyException as err:
            print(err)
            my_number = input("Введите число: ")
                
    print(f"Вы ввели последовательно следующие числа: {my_list}")

#Проверка
func()

# 4 -6. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
# будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
# определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа
# оргтехники.

class Warehouse:
    def __init__(self, name, price, cnt):
        self.name = name
        self.price = price
        self.cnt = cnt
        try:
            self.cnt = int(self.cnt)
            self.price = int(self.price)     
        except ValueError:
            print("Неверный формат данных. Повторите ввод.")
        if self.name.isdigit():
            print("Введите название Оргтехники")
        
    def accept(self):
        cnt_all = int(self.cnt)*int(self.price)
        print(f"На склад принято {self.cnt} шт. оргтехники типа {self.name} стоимостью {self.price} за 1 штуку. Общая стоимость: {cnt_all}")
        
    def transfer(self):
        print(f"Оргтехника типа {self.name} передана в подразделение для хранения")
              

class Printer(Warehouse):  
    def do(self):
        print("I am printing")

class Scaner(Warehouse):
    def do(self):
        print("I am scaning")

class Xerox(Warehouse):
    def do(self):
        print("I am xeroxing")    

#Проверка
example_printer = Printer('Принтер_2010', 10000, 4)
example_printer.price

example_printer.do()
example_warehouse = Warehouse('Принтер_2010', 10000, 3)
example_warehouse.cnt

example_warehouse.accept()
example_warehouse.transfer()

example_warehouse = Warehouse('Принтер_2010', 10000, 'пример')

#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов 
# сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Задано комплексное число: {self.x} + i * {self.y}"
    
    def __add__(self, other):
        return  ComplexNumber(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return  ComplexNumber((self.x * other.x) -  (self.y * other.y), (self.x * other.y) + (self.y * other.x))
        
#Проверка
number_1 = ComplexNumber(3,5)
number_2 = ComplexNumber(3,5)
print(number_1)

print(number_1 + number_2)
print(number_1 * number_2)
