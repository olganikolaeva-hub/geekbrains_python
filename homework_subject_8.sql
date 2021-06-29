# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class MyData():
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
