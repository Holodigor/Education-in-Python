# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    total_food = 0
    total_money = 0

    def __init__(self):
        House.total_food = 0
        House.total_money = 0
        self.food = 50
        self.money = 100
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return f'В доме денег {self.money}, грязи {self.dirt}, еды {self.food}, еды для кота {self.cat_food} '


class Man:

    def __init__(self):
        self.degree_of_satiety = 30
        self.degree_of_happiness = 100

    def __str__(self):
        return f'Moe счастье {self.degree_of_happiness}, моя сытость {self.degree_of_satiety}'

    def eat(self):
        if self.house.food >= 30:
            self.degree_of_satiety += 30
            self.house.food -= 30
            House.total_food += 30
            return f'{self.name} поел'
        elif self.house.food == 0:
            return f'{self.name}В доме нет еды'
        else:
            self.degree_of_satiety += self.house.food
            House.total_food += self.house.food
            self.house.food = 0
            return f'{self.name} поел'


class Husband(Man):

    def __init__(self, name, house, salary=150):
        super().__init__()
        self.name = name
        self.house = house
        self.salary = salary

    def __str__(self):
        return f'{self.name} ' + super().__str__()

    def act(self):
        if self.degree_of_satiety <= 0:
            cprint(f'{self.name} умер с голодухи', color='red')
            return
        if self.degree_of_happiness < 10:
            cprint(f'{self.name} умер от депресии', color='red')
            return
        if self.house.dirt > 90:
            self.degree_of_happiness -= 10

        if self.degree_of_satiety < 30:
            cprint(self.eat(), color='blue')
        elif self.degree_of_happiness < 20:
            self.gaming()
        else:
            self.work()

    def work(self):
        self.house.money += self.salary
        self.degree_of_satiety -= 10
        House.total_money += self.salary
        cprint(f'{self.name} сходил на роботу', color='blue')

    def gaming(self):
        self.degree_of_satiety -= 10
        self.degree_of_happiness += 20
        cprint(f'{self.name} играл в WOT', color='blue')


class Wife(Man):
    total_fur_coat = 0

    def __init__(self, name, house):
        super().__init__()
        Wife.total_fur_coat = 0
        self.name = name
        self.house = house

    def __str__(self):
        return f'{self.name} ' + super().__str__()

    def act(self):
        if self.degree_of_satiety <= 0:
            cprint(f'{self.name} умерла с голодухи', color='red')
            return

        if self.degree_of_happiness < 10:
            cprint(f'{self.name} умерла от депресии', color='red')
            return

        if self.house.dirt > 90:
            self.degree_of_happiness -= 10

        if self.degree_of_satiety < 30:
            cprint(self.eat(), color='yellow')
        elif self.degree_of_happiness < 20:
            self.buy_fur_coat()
        elif self.house.food < 60:
            self.shopping()
        elif self.house.cat_food < 20 * Cat.total_cat:
            self.shopping()
        else:
            self.clean_house()

    def shopping(self):
        self.degree_of_satiety -= 10
        if self.house.money == 0:
            cprint(f'{self.name} В доме нет денег на еду', color='yellow')
            return
        if self.house.food < 60:
            if self.house.money > 90:
                self.house.food += 90
                self.house.money -= 90
            else:
                self.house.food = self.house.money
                self.house.money = 0
            cprint(f'{self.name} Купила еды', color='yellow')

        if self.house.cat_food < 20 * Cat.total_cat:
            if self.house.money >= 20 * Cat.total_cat:
                self.house.money -= 20 * Cat.total_cat
                self.house.cat_food += 20 * Cat.total_cat
            else:
                self.house.cat_food += self.house.money
                self.house.money = 0
            cprint(f'{self.name} Купила еды', color='yellow')

    def buy_fur_coat(self):
        self.degree_of_satiety -= 10
        if self.house.money >= 350:
            self.house.money -= 350
            self.degree_of_happiness += 60
            cprint(f'{self.name} Купила шубу', color='yellow')
            Wife.total_fur_coat += 1
        else:
            cprint(f'{self.name} На шубу не хватило денег', color='yellow')

    def clean_house(self):
        self.degree_of_satiety -= 10
        if self.house.dirt > 100:
            self.house.dirt -= 100
            cprint(f'{self.name} Убрала в квартире', color='yellow')
        elif self.house.dirt > 0:
            self.house.dirt = 0
            cprint(f'{self.name} Убрала в квартире', color='yellow')
        else:
            cprint(f'{self.name} В квартире чисто', color='yellow')


class Child(Man):

    def __init__(self, name, house):
        super().__init__()
        self.name = name
        self.house = house

    def __str__(self):
        return f'{self.name} ' + super().__str__()

    def eat(self):
        if self.house.food >= 10:
            self.degree_of_satiety += 20
            self.house.food -= 10
            House.total_food += 10
            return f'{self.name} поел'
        elif self.house.food == 0:
            self.sleep()
        else:
            self.degree_of_satiety += self.house.food * 2
            House.total_food += self.house.food
            self.house.food = 0
            return f'{self.name} поел'

    def act(self):
        if self.degree_of_satiety <= 0:
            cprint(f'{self.name} умерла с голодухи', color='red')
            return

        if self.degree_of_happiness < 10:
            cprint(f'{self.name} умерла от депресии', color='red')
            return

        if self.degree_of_satiety < 30:
            cprint(self.eat(), color='green')
        else:
            self.sleep()

    def sleep(self):
        self.degree_of_satiety -= 10
        cprint(f'{self.name} поспал', color='green')


class Cat:
    all_total_cat = 0
    total_cat = 0

    def __init__(self, name, house):
        Cat.total_cat += 1
        Cat.all_total_cat += 1
        self.name = name
        self.house = house
        self.degree_of_satiety = 30
        self.status = 'alive'

    def __str__(self):
        return f'Я кот {self.name}, моя сытость {self.degree_of_satiety}'

    def act(self):
        if self.degree_of_satiety <= 0:
            cprint(f'{self.name} умер с голодухи', color='red')
            self.status = 'die'
            Cat.total_cat -= 1
            return
        if self.degree_of_satiety <= 20 and self.house.cat_food > 0:
            self.eat()
        else:
            choice = randint(1, 2)
            self.sleep() if choice == 1 else self.soil()

    def eat(self):
        if self.house.cat_food <= 0:
            cprint(f'в доме нет еды для кота', color='magenta')
            return
        if self.house.cat_food >= 10:
            self.house.cat_food -= 10
            self.degree_of_satiety += 20
        else:
            self.degree_of_satiety += self.house.cat_food * 2
            self.house.cat_food = 0
        cprint(f'Кот {self.name} поел', color='magenta')

    def sleep(self):
        self.degree_of_satiety -= 10
        cprint(f'Кот {self.name} поспал', color='magenta')

    def soil(self):
        self.degree_of_satiety -= 10
        self.house.dirt += 5
        cprint(f'кот {self.name} Драл обоии', color='magenta')


class Simulation:

    def __init__(self, money_incidents, food_incidents):
        self.money_incidents = money_incidents
        self.food_incidents = food_incidents
        self.max_cats = 1

    def experiment(self, salary=150):
        Cat.total_cat = 0
        Cat.all_total_cat = 0
        home = House()
        serge = Husband(name='Сережа', house=home, salary=salary)
        masha = Wife(name='Маша', house=home)
        dron = Child(name='ДРОН', house=home)
        list_cat = []
        for number_cat in range(0, self.max_cats):
            list_cat.append(Cat(name=str(number_cat), house=home))

        for day in range(365):
            cprint('================== День {} =================='.format(day), color='red')
            if self.money_incidents > 0:
                if randint(0, 5) == 1:
                    if home.money > 0:
                        home.money = int(home.money / 2)
                        self.money_incidents -= 1
                        serge.degree_of_happiness += 100
                        cprint(f'{serge.name} загулял')
            if self.food_incidents > 0:
                if randint(0, 5) == 1:
                    if home.food > 0:
                        home.food = int(home.food / 2)
                        self.food_incidents -= 1
                        cprint(f'Коты украли еду')
                        for cat in list_cat:
                            cat.degree_of_satiety += 20
            home.dirt += 5
            serge.act()
            masha.act()
            dron.act()
            for cat in list_cat:
                if cat.status == 'die':
                    list_cat.remove(cat)
                else:
                    cat.act()
            cprint(serge, color='cyan')
            cprint(masha, color='cyan')
            cprint(dron, color='cyan')
            for cat in list_cat:
                cprint(cat, color='cyan')
            cprint(home, color='cyan')
        print('\n ========== ИТОГИ ===========\n')
        cprint(f'Cьедено еды {House.total_food}')
        cprint(f'Заработано денег {House.total_money}')
        cprint(f'Куплено шуб {Wife.total_fur_coat}')
        cprint(f'Выжило котов {Cat.total_cat}  из {Cat.all_total_cat}')
        return Cat.all_total_cat, Cat.total_cat


res_experiment = []
for food_incidents in range(2):
    for money_incidents in range(2):
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 451, 50):
            while True:
                all_total_cat, total_cat = life.experiment(salary=salary)
                if all_total_cat != total_cat:
                    res_experiment.append(''.join(str(life.max_cats - 1)))
                    break
                else:
                    life.max_cats += 1
food_incidents = 0
money_incidents = 0
print('                                       |   50  ||  100  ||  150  ||  200  ||  250  ||  300  ||  350  ||  400  ||  450  |')
print('------------------------------------------------------------------------------------------------------------------------')
print(f'food_incidents = {food_incidents} money_incidents = {money_incidents}', end=' ')
enter = 9
for i, max_cat in enumerate(res_experiment):
    if i < enter:
        if int(max_cat) < 10:
            print(f'|    {max_cat}  |', end='')
        else:
            print(f'|   {max_cat}  |', end='')
    else:
        print('')
        print('------------------------------------------------------------------------------------------------------------------------')
        print(f'food_incidents = {food_incidents} money_incidents = {money_incidents}', end=' ')
        print(f'|    {max_cat}  |', end='')
        enter += 9
        if money_incidents == 6:
            money_incidents = 0
            food_incidents += 1
        else:
            money_incidents += 1



# сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.
######################################################## Часть вторая
# #
# # После подтверждения учителем первой части надо
# # отщепить ветку develop и в ней начать добавлять котов в модель семьи
# #
# # Кот может:
# #   есть,
# #   спать,
# #   драть обои
# #
# # Люди могут:
# #   гладить кота (растет степень счастья на 5 пунктов)
# #
# # В доме добавляется:
# #   еда для кота (в начале - 30)
# #
# # У кота есть имя и степень сытости (в начале - 30)
# # Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# # Еда для кота покупается за деньги: за 10 денег 10 еды.
# # Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# # Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
# #
# # Если кот дерет обои, то грязи становится больше на 5 пунктов
#
#
# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#
#


# ######################################################## Часть вторая бис
# #
# # После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
# #
# # Ребенок может:
# #   есть,
# #   спать,
# #
# # отличия от взрослых - кушает максимум 10 единиц еды,
# # степень счастья  - не меняется, всегда ==100 ;)
#
# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
# # TODO после реализации второй части - отдать на проверку учителем две ветки
#
#
# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#
#
# # Усложненное задание (делать по желанию)
# #
# # Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# # Коты должны выжить вместе с семьей!
# #
# # Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# # Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
# #
# # Дополнительно вносить некий хаос в жизнь семьи
# # - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# # - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# # Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
# #   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
# #
# # в итоге должен получится приблизительно такой код экспериментов
# # for food_incidents in range(6):
# #   for money_incidents in range(6):
# #       life = Simulation(money_incidents, food_incidents)
# #       for salary in range(50, 401, 50):
# #           max_cats = life.experiment(salary)
# #           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#
