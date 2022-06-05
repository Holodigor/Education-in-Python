# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.set_screen_size(1200, 600)
sd.background_color = sd.COLOR_BLUE


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

def draw_branches(point, angle=90, lenght=30, width=7, color=(153, 51, 0), tree_color=6):
    vector = sd.get_vector(start_point=point, angle=angle, length=lenght)
    vector.draw(width=width, color=color)
    tree_color -= 1
    r1 = sd.randint(80, 100)
    r2 = sd.randint(40, 100)
    angle_1 = angle - 50 * (r2 / 100)
    angle_2 = angle + 35 * (r2 / 100)
    lenght = lenght * .8
    if width > 1:
        width -= 1
    if tree_color == 0:
        color = sd.COLOR_GREEN
    if lenght > 2:
        draw_branches(vector.end_point, angle=angle_1, lenght=lenght * (r1 / 100), width=width, color=color,
                      tree_color=tree_color)
        draw_branches(vector.end_point, angle=angle_2, lenght=lenght * (r1 / 100), width=width, color=color,
                      tree_color=tree_color)
    return


def draw_sun(point):
    sd.circle(point, 45, color=sd.COLOR_YELLOW, width=0)
    for angle in range(0, 360, 20):
        sd.get_vector(point, angle=angle, length=80).draw(width=10, color=sd.COLOR_YELLOW)


def draw_earth():
    sd.polygon([sd.get_point(0, 0), sd.get_point(sd.resolution[0], 0),
                sd.get_point(sd.resolution[0], int(sd.resolution[1] / 6)),
                sd.get_point(0, int(sd.resolution[1] / 6))],
               color=sd.COLOR_DARK_GREEN, width=0)


if __name__ == '__main__':
    point = sd.get_point(600, 30)
    draw_earth()
    draw_sun(point)
    draw_branches(point=point, angle=90, lenght=130)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
