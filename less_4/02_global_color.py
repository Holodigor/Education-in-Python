# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
sd.set_screen_size(800, 800)

color_dict = {
    'red': sd.COLOR_RED,
    'orange': sd.COLOR_ORANGE,
    'yellow': sd.COLOR_YELLOW,
    'green': sd.COLOR_GREEN,
    'cyan': sd.COLOR_CYAN,
    'blue': sd.COLOR_BLUE,
    'purple': sd.COLOR_PURPLE
}


def draw_figure(point, angle, lenght, angles, color):
    next_angel = 360 / angles
    vector = sd.get_vector(start_point=point, angle=angle, length=lenght)
    point_line = vector.end_point
    while next_angel < 360:
        vector = sd.get_vector(start_point=vector.end_point, angle=angle + next_angel, length=lenght)
        vector.draw(color=color, width=3)
        sd.circle(vector.end_point, radius=4, width=0, color=color)
        next_angel += 360 / angles
    sd.line(start_point=vector.end_point, end_point=point_line, width=3, color=color)
    sd.circle(point_line, radius=4, width=0, color=color)


def draw_triangle(start_point_x=100, start_point_y=100, angle=0, lenght=200, color=sd.COLOR_YELLOW):
    point = sd.get_point(start_point_x, start_point_y)
    draw_figure(point=point, angle=angle, lenght=lenght, angles=3, color=color)


def draw_square(start_point_x=100, start_point_y=100, angle=0, lenght=200, color=sd.COLOR_YELLOW):
    point = sd.get_point(start_point_x, start_point_y)
    draw_figure(point=point, angle=angle, lenght=lenght, angles=4, color=color)


def draw_pentagon(start_point_x=100, start_point_y=100, angle=0, lenght=200, color=sd.COLOR_YELLOW):
    point = sd.get_point(start_point_x, start_point_y)
    draw_figure(point=point, angle=angle, lenght=lenght, angles=5, color=color)


def draw_hexagon(start_point_x=100, start_point_y=100, angle=0, lenght=200, color=sd.COLOR_YELLOW):
    point = sd.get_point(start_point_x, start_point_y)
    draw_figure(point=point, angle=angle, lenght=lenght, angles=6, color=color)


print('Возможные цвета')
for i, color in enumerate(list(color_dict)):
    print(f'{i} : {color}')
while True:
    user_color = input('Введите желаемый цвет: ')
    if 0 <= int(user_color) <= len(list(color_dict)):
        break
    else:
        print('Вы ввели не коректный номер')
user_color = color_dict[list(color_dict)[int(user_color)]]
draw_triangle(100, 100, lenght=150, angle=10, color=user_color)
draw_square(500, 100, lenght=150, angle=10, color=user_color)
draw_pentagon(100, 400, lenght=150, angle=10, color=user_color)
draw_hexagon(500, 400, lenght=100, angle=10, color=user_color)

sd.pause()
