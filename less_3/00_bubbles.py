# -*- coding: utf-8 -*-
import random

import simple_draw as sd

height = 600
width = 1200
sd.resolution = (width, height)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(width / 2, height / 2)
# radius = 50
# for i in range(3):
#     radius += 10
#     sd.circle(point, radius=radius, width=3)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def draw_circle(point, step=5, radius=50, color=(0, 127, 0)):
    """draw a circle in point (x,y) wiht radius"""
    for i in range(3):
        radius += step
        sd.circle(point, radius, width=2, color=color)


# point = sd.get_point(200, 200)
# draw_circle(point, 5)

# Нарисовать 10 пузырьков в ряд

# for x in range(70, 701, 70):
#     point = sd.get_point(x, 200)
#     draw_circle(point)

# Нарисовать три ряда по 10 пузырьков

# for y in range(100, 301, 100):
#     for x in range(70, 701, 70):
#         point = sd.get_point(x, y)
#         draw_circle(point)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(101):
    x = random.randint(0, width)
    y = random.randint(0, height)
    color = sd.random_color()
    point = sd.get_point(x, y)
    draw_circle(point, color=color)



sd.pause()
