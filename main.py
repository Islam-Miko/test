class Home:
    square_rate = 40_000

    def __init__(self, name, square):
        self.name = name
        self.__price = square * Home.square_rate


class Person:
    hour_rate = 250
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.__money = 0
        self.__house = None

    def work(self, hours):
        pay = hours * Person.hour_rate
        self.__money += pay
        print(f'{self.name} worked {hours} hours and earned {pay} som')
