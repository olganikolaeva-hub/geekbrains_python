#ООП

# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
# реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше
# усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить
# работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.

import itertools
import time
class TrafficLight:
    __color__ = 'red'
    
    def running(self):
        colors = {'red' : 7, 'yellow' : 2, 'green' : 10}
        for item in itertools.repeat(list(colors.keys()), times = 2):
            if item[0]:
                print(f"Сейчас светофор горит цветом: {item[0]}. Проход запрещен.")
                for i in range(1, colors[item[0]] + 1):
                    sec = colors[item[0]] + 1 - i
                    print(f"До переключения осталось {sec} секунд")
                    time.sleep(1)
            if item[1]:
                print(f"Сейчас светофор горит цветом: {item[1]}. Внимание, скоро загорится зеленый цвет.")
                for i in range(1, colors[item[1]] + 1):
                    sec = colors[item[1]] + 1 - i
                    print(f"До переключения осталось {sec} секунд")
                    time.sleep(1)
            if item[2]:
                print(f"Сейчас светофор горит цветом: {item[2]}. Переходите дорогу.")
                for i in range(1, colors[item[2]] + 1):
                    sec = colors[item[2]] + 1 - i
                    print(f"До переключения осталось {sec} секунд")
                    time.sleep(1)
        print("2 Цикла переключения закончены")
 
#Инициализируем объект класса
my_TrafficLight = TrafficLight()
my_TrafficLight.__color__
my_TrafficLight.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов
# должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного
# кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    def __init__(self, lenght, width):
        self._lenght_ = lenght
        self._width_ = width
        
    def mass_of_asphalt(self, mass_for_1, depth):
        return print(f"Для заданных параметров дороги и полотна асфальта потребуется {self._lenght_ * self._width_ * mass_for_1 * depth} асфальта")
      
#Инициализируем объект класса
my_road_to_university = Road(20,5000)
my_road_to_university._lenght_
my_road_to_university.mass_of_asphalt(25, 5)

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income
# (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
# методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
# примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать
# методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_ = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        
    def get_full_name(self): 
        print(f"Сотрудника зовут {self.surname}  {self.name}")

    def get_total_income(self):
        total = self._income_[list(self._income_.keys())[0]] + self._income_[list(self._income_.keys())[1]]
        print(f"Доход сотрудника с учетом премии равен {total}")

#Инициализируем объект класса
worker = Position("Иван", "Иванов", "Начальник отдела", {"wage": 180000, "bonus": 50000})
worker.get_full_name()
worker.get_total_income()
worker.position
worker._income_

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При
# значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction):
        print(f"Машина повернула {self.direction}")
    def show_speed(self):
        print(f"Скорость машины составляет {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(color, speed, name, is_police)
        
    def show_speed(self):
        if int(self.speed) > 60:
            print(f"У этой городской машины превышена скорость")
        
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
    def show_speed(self):
        if int(self.speed) > 40:
            print("У этой рабочей машины превышена скорость")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

#Инициализируем объекты классов
car = Car(60, 'green', 'bmv', 0)
car_for_work = WorkCar(60, 'green', 'bmv', 0)
car.show_speed()
car_for_work.show_speed()
(car_for_work.speed, car_for_work.color, car_for_work.name)

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f"Запуск отрисовки. Рисуем {self.title}")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print(f"Запуск отрисовки. Рисуем экземпляр {self.title}")

class Penсil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print(f"Запуск отрисовки. Рисуем экземпляр {self.title}")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print(f"Запуск отрисовки. Рисуем экземпляр {self.title}")

 #Инициализируем объекты классов
example_pen = Pen("Ручка")
example_pencil = Penсil("Карандаш")
example_handle = Handle("Маркер")
example_pen.draw()
example_pencil.draw()
example_handle.draw()
