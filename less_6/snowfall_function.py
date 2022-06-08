# -*- coding: utf-8 -*-
"""
    create_snowflakes(number_snowflakes=None)
    draw_snowflakes(color=sd.COLOR_WHITE)
    ove_snowflakes(step=1)
    numbers_reached_bottom_of_screen()
    del_snowflakes(list_bottom_of_screen=None)
"""

import simple_draw as sd


snowflakes_list = []


def create_snowflakes(number_snowflakes=None):
    """Создает N снежинок"""
    for i in range(number_snowflakes):
        snowflakes_list.append(sd.get_point(sd.random_number(0, sd.resolution[0]), sd.resolution[1]))


def draw_snowflakes(color=sd.COLOR_WHITE):
    """Отрисовывает все снежинки цветом color"""
    sd.start_drawing()
    for snowflakes in snowflakes_list:
        sd.snowflake(center=snowflakes, color=color, length=40)
    sd.finish_drawing()


def move_snowflakes(step=1):
    """ Cдвигает снежинки на шаг step"""
    for snowflakes in snowflakes_list:
        step += 2
        snowflakes.y -= step


def numbers_reached_bottom_of_screen():
    """Выдает список номеров снежинок, которые вышли за границу экрана"""
    list_bottom_of_screen = []
    for i, snowflakes in enumerate(snowflakes_list):
        if snowflakes.y <= 0:
            list_bottom_of_screen.append(i)
    return list_bottom_of_screen


def del_snowflakes(list_bottom_of_screen=None):
    """Удаляет снежинки с номерами из списка"""
    if list_bottom_of_screen is None:
        list_bottom_of_screen = []
    if list_bottom_of_screen:
        for i in list_bottom_of_screen[::-1]:
            snowflakes_list.pop(i)


if __name__ == "__main__":
    print(bool([]))
