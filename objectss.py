import random


class PC:
    insurance_rate = 10
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.total_insurance = self.price * PC.insurance_rate

    def calculate_total(self, tax):
        return self.price + self.total_insurance + tax

    @classmethod
    def from_string(cls, data):
        datas = data.split(' ')
        return cls(datas[0], int(datas[1]))

    @classmethod
    def change(cls, value):
        cls.insurance_rate = value

    @staticmethod
    def get_discount():
        a = [10, 20, 30]
        return random.choice(a)

    def print(self):
        print(f'{self.price} {self.name}')


class Laptop(PC):

    def __init__(self, name, price, capacity):
        super().__init__(name, price)
        self.capacity = capacity

    def print(self):
        print(f'{self.price} {self.name} {self.name} {self.name}')


new_obj3 = Laptop('Laptop', 300, 2000)
print(type(new_obj3))
print(new_obj3.price)
print(new_obj3.name)
print(new_obj3.capacity)
new_obj3.print()

PC.count = 123
new_object = PC('ASUS', 100)
# new_object2 = PC.from_string('ASUS 100')

# new_object2 = PC('MAC', 200)
# new_object2 = PC('MAC', 200)
# new_object2 = PC('MAC', 200)
# new_object2 = PC('MAC', 200)
print(new_object.name)
print(new_object.price)
print(new_object.total_insurance)
new_object.print()
