# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall_function import create_snowflakes, draw_snowflakes,\
    move_snowflakes, numbers_reached_bottom_of_screen, del_snowflakes

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
create_snowflakes(10)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowflakes(color=sd.background_color)
    #  сдвинуть_снежинки()
    move_snowflakes(step=5)
    #  нарисовать_снежинки_цветом(color)
    draw_snowflakes()
    reached_bottom_of_screen = numbers_reached_bottom_of_screen()
    if reached_bottom_of_screen:
        del_snowflakes(list_bottom_of_screen=reached_bottom_of_screen)
        create_snowflakes(len(reached_bottom_of_screen))
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
