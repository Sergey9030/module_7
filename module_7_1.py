#from pprint import pprint
"""
Согласно ТЗ метод get_products должен возвращать "единую строку со всеми товарами".
По анализу примера работы программы и выводу на консоль он возвращает
полную инфорацию о товаре (наименование, вес, категория) отдельной строкой.

В данной реализации get_products возвращает список наименований всех товаров.
"""


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self. category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        nn = []
        rr = file.readline()  # Читаем первую строку
        while rr != '':  # Пока не достигнут конец файла
            ss = rr.split(', ')  # Разбиваем строку на подстроки
            nn.append(ss[0])
            rr = file.readline()  # Читаем остальные строки
        file.close()
        return nn

    def add(self, *products):
        pp = self.get_products()
        for i in products:
            if not (i.name in pp):
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
                pp = self.get_products()
            else:
                print(f'Продукт {i.name} уже есть в магазине.')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
