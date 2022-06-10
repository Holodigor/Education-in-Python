# -*- coding: utf-8 -*-

from random import randint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и копоселиться в домету надо вместе прожить 365 дней.


class House:

    def __init__(self, number):
        self.money = 100
        self.food = 100
        self.food_cat = 0
        self.dirt = 0
        self.number = number
        print(f'Построен дом № {self.number}')

    def __str__(self):
        return f' money {self.money}, food {self.food}, food_cat {self.food_cat}, dirt {self.dirt}'


class Man:

    def __init__(self, name):
        self.house = None
        self.name = name
        self.satiety = 20
        print(f'Привет я {self.name}')

    def __str__(self):
        return f' name {self.name}, satiety {self.satiety}'

    def settle_in_the_house(self, house):
        self.house = house
        print(f'{self.name} Переехал в дом')

    def pick_up_a_cat(self, other):
        other.house = self.house
        print(f'{self.name} подобрал кота {other.name}')

    def buy_cat_food(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food_cat += 50
            print(f'{self.name} купил коту еды')

    def buy_my_food(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food += 50
            print(f'{self.name} купил еды')

    def clean_up_the_house(self):
        self.house.dirt -= 100
        self.satiety -= 20
        print(f'{self.name} убрал в квартире')

    def work(self):
        self.house.money += 150
        self.satiety -= 20
        print(f'{self.name} сходил на роботу')

    def eat(self):
        if self.house.food >= 30:
            self.satiety += 40
            self.house.food -= 40
            print(f'{self.name} поел')

    def watch_tv(self):
        self.satiety -= 20
        print(f'{self.name} смотрел телевизор')

    def action(self):
        if self.satiety == 0:
            print(f'{self.name} умер')
        elif self.satiety <= 30:
            self.eat()
        elif self.house.food < 30:
            self.buy_my_food()
        elif self.house.food_cat < 10:
            self.buy_cat_food()
        elif self.house.money < 50:
            self.work()
        else:
            random_action = randint(1, 2)
            if random_action == 1:
                self.watch_tv()
            else:
                self.clean_up_the_house()


class Cat:

    def __init__(self, name):
        self.name = name
        self.satiety = 20
        self.house = None
        print(f'Привет я кот {self.name}')

    def __str__(self):
        return f'name {self.name}, satiety {self.satiety} '

    def sleep(self):
        self.satiety -= 10
        print(f'{self.name} поспал')

    def tear_wallpaper(self):
        self.satiety -= 10
        self.house.dirt += 10
        print(f'{self.name} драл обоии')

    def eat(self):
        if self.house.food_cat >= 10:
            self.satiety += 30
            self.house.food_cat -= 10
            print(f'{self.name} поел')

    def action(self):
        if self.satiety == 0:
            print(f'{self.name} умер')
        elif self.satiety <= 10:
            self.eat()
        else:
            random_action = randint(1, 2)
            if random_action == 1:
                self.tear_wallpaper()
            else:
                self.sleep()


if __name__ == '__main__':
    vasia = Man('Вася')
    murzik = Cat('Мурзик')
    house = House(43)
    vasia.settle_in_the_house(house=house)
    vasia.pick_up_a_cat(murzik)
    vasia.buy_cat_food()
    for i in range(25):
        print(f'=============== день {i} ===================')
        vasia.action()
        murzik.action()
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
