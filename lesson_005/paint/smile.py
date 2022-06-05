# -*- coding: utf-8 -*-

# (определение функций)
from random import randint

import simple_draw as sd


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(center_smile, radius=50):

    sd.circle(center_smile, radius, width=3)
    eye_x_y = (((radius / 2) ** 2) / 2) ** .5
    eye_center_1 = sd.get_point(center_smile.x - eye_x_y, center_smile.y + eye_x_y)
    eye_center_2 = sd.get_point(center_smile.x + eye_x_y, center_smile.y + eye_x_y)
    sd.circle(eye_center_1, radius / 5, width=0)
    sd.circle(eye_center_2, radius / 5, width=0)
    point_1 = sd.get_point(center_smile.x - eye_x_y, center_smile.y - eye_x_y / 2)
    point_2 = sd.get_point((center_smile.x - eye_x_y / 2), (center_smile.y - eye_x_y))
    point_3 = sd.get_point((center_smile.x + eye_x_y / 2), (center_smile.y - eye_x_y))
    point_4 = sd.get_point((center_smile.x + eye_x_y), (center_smile.y - eye_x_y / 2))
    sd.lines([point_1, point_2, point_3, point_4], closed=True, width=2)


if __name__ == '__main__':
    for i in range(10):
        point = sd.random_point()
        smile(point, 20)
    sd.pause()
