# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg




def draw_figure(point, angle, lenght, angles):
    next_angel = 360 / angles
    vector = sd.get_vector(start_point=point, angle=angle, length=lenght)
    point_line = vector.end_point
    while next_angel < 360:
        vector = sd.get_vector(start_point=vector.end_point, angle=angle + next_angel, length=lenght)
        vector.draw(width=3)

        next_angel += 360 / angles
    sd.line(start_point=vector.end_point, end_point=point_line, width=3)



def draw_triangle(start_point_x=100, start_point_y=100, angle=0, lenght=200):
    point = sd.get_point(start_point_x, start_point_y)
    draw_figure(point=point, angle=angle, lenght=lenght, angles=3)


def draw_square(start_point_x=100, start_point_y=100, angle=0, lenght=200):
    point = sd.get_point(start_point_x, start_point_y)
    draw_figure(point=point, angle=angle, lenght=lenght, angles=4)


def draw_pentagon(start_point_x=100, start_point_y=100, angle=0, lenght=200):
    point = sd.get_point(start_point_x, start_point_y)
    draw_figure(point=point, angle=angle, lenght=lenght, angles=5)


def draw_hexagon(start_point_x=100, start_point_y=100, angle=0, lenght=200):
    point = sd.get_point(start_point_x, start_point_y)
    draw_figure(point=point, angle=angle, lenght=lenght, angles=10)


if __name__ == '__main__':
    sd.set_screen_size(1000, 1000)

    x, y, = 300, 300
    draw_triangle(200, 200, lenght=150, angle=20)
    draw_square(600, 200, lenght=150, angle=0)
    draw_pentagon(200, 600, lenght=150, angle=60)
    draw_hexagon(600, 600, lenght=100, angle=70)

    sd.sleep(5)
    sd.quit()

    # Часть 1-бис.
    # Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
    # Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
    # А если таких функций не 4, а 44?

    # Часть 2 (делается после зачета первой части)
    #
    # Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
    # Это называется "Выделить общую часть алгоритма в отдельную функцию"
    # Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
    #
    # В итоге должно получиться:
    #   - одна общая функция со множеством параметров,
    #   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
    #
    # Не забудте в этой общей функции придумать, как устранить разрыв
    #   в начальной/конечной точках рисуемой фигуры (если он есть)

    # Часть 2-бис.
    # А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
    # Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
    # Будьте ленивыми, не используйте копи-пасту!

    sd.pause()
