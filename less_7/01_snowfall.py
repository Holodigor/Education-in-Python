# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self, x=100, y=400, color=sd.COLOR_WHITE, length=50):
        self.x = x
        self.y = y
        self.color = color
        self.length = length
        self.speed = 5
        self.acceleration = 0

    def move(self):
        self.y -= self.speed
        self.x += self.acceleration

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(point, self.length, color=self.color)

    def __str__(self):
        return (f'x = {self.x}, y = {self.y}, color = {self.color}, length = {self.length},'
                f' speed = {self.speed}, acceleration = {self.acceleration}')

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(point, self.length, color=sd.background_color)

    def can_fall(self):
        if self.y > 0:
            return True
        else:
            return False


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.acceleration = 5
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         print(flake)
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
def get_flakes(count):
    lis_flakes = []
    for i in range(count):
        flake_rd = Snowflake()
        flake_rd.x = randint(0, sd.resolution[0])
        flake_rd.y = randint(int(sd.resolution[1] * .75), sd.resolution[1])
        flake_rd.length = randint(20, 40)
        flake_rd.speed = randint(1, 10)
        lis_flakes.append(flake_rd)

        print(flake_rd)
    return lis_flakes


def get_fallen_flakes():
    global flakes
    count = 0
    for flake in flakes:
        if not flake.can_fall():
            count += 1
    return count


def append_flakes(count):
    global flakes
    new_list = get_flakes(count)
    flakes = flakes + new_list


flakes = get_flakes(count=20)  # создать список снежинок
print(len(flakes))
while True:
    for flake in flakes:
        if flake.can_fall():
            flake.clear_previous_picture()
            flake.move()
            flake.draw()
        else:
            flakes.remove(flake)
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    print(fallen_flakes)
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
        print(len(flakes))
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
