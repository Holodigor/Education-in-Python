# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_figure(point, angle=0, lenght=200, angles=3, color=sd.COLOR_ORANGE):
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


print(f'Возможные фигуры: \n'
      f'0 : Триугольник \n'
      f'1 : Квадрат \n'
      f'2 : Пятиугольник \n'
      f'3 : Шестиугольник')
while True:
    user_shape = input('Выберите фигуру: ')
    if 0 <= int(user_shape) <= 3:
        point = sd.get_point(sd.resolution[0] / 2 - 100, sd.resolution[1]/2 - 100)
        draw_figure(point=point, angles=int(user_shape) + 3)
        break
    else:
        print('Вы ввели не коректный номер')





sd.pause()
