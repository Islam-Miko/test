def full_name():
    first_name = input('First name: ').capitalize()
    last_name = input('Last name: ').capitalize()
    full_name = dict(first_name=first_name, last_name=last_name)
    return full_name


def age():
    age = input('Age: ')
    return age


def child(age):
    a = int(age()) < 12
    return a


def info(full_name, age, child):
    info = {'full_name': full_name(), 'age': age(), 'child': child(age)}
    return info


full_name()
