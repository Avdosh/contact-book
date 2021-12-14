from .person import Person
from time import time


def decorator_for_time(func):
    def wrapper(*args, **kwargs):
        t = time()
        res = func(*args, **kwargs)
        print('Затраченное время: ', func.__name__, time() - t)
        return res
    return wrapper


class Book:

    @decorator_for_time
    def __init__(self, filename):
        self.persons = []
        self.filename = filename
        self.file = open(self.filename, 'a+')
        self.file.close()
        self.file = open(self.filename, 'r+')
        content = self.file.read()
        self.file.close()
        for line in content.split('\n'):
            element = line.split(' ')
            if len(element) < 5:
                continue
            else:
                self.add(element[0], element[1], element[2], element[3], element[4])

    def add(self, name, surname, mail, phone, work):
        p = Person(name, surname, mail, phone, work)
        self.persons.append(p)

    def delete(self, phone):
        for p in self.persons:
            if p.phone == phone:
                self.persons.remove(p)
                print('Запись удалена')
                break

    def show(self):
        if len(self.persons) != 0:
            for p in self.persons:
                print(f'name: {p.name} surname: {p.surname}, mail: {p.mail}, phone: {p.phone}, work: {p.work}')
        else:
            print('Нет записей')

    @decorator_for_time
    def write_file(self):
        self.file = open(self.filename, 'w')
        if len(self.persons) != 0:
            for p in self.persons:
                self.file.write(f'{p.name} {p.surname} {p.mail} {p.phone} {p.work}\n')
        self.file.close()
