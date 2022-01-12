class Home:
    square_rate = 40_000

    def __init__(self, name, square):
        self.name = name
        self.__price = square * Home.square_rate

    @property
    def price(self):
        return self.__price


house_market = [
    Home('1 комната', 50),
    Home('2 komnata', 65),
    Home('3 komnata', 120)
]

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

    def buy_house(self):
        for house in house_market:
            print(f'{house.name}: {house.price}')
            if self.__money >= house.price:
                choice = input('Buy? Y|N').upper() == 'Y'
                if choice:
                    self.__house = house
                    self.__money -= house.price
                    house_market.remove(house)
    @property
    def house(self):
        if self.__house is None:
            print('NO House')
        else:
            print(f'{self.name} has house by name {self.__house.name}')

adam = Person('adam', 30)
adam.work(1000000)
adam.buy_house()
adam.house
