# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def christmas_snow(number_of_snowflakes=20, height=sd.resolution[0], wight=sd.resolution[1]):
    n = number_of_snowflakes
    snow_center_list = []
    snow_length_list = []
    for i in range(n):
        snow_center_list.append(sd.get_point(sd.random_number(-200, 600), sd.random_number(500, 900)))
        snow_length_list.append(sd.random_number(10, 50))
    while True:
        sd.start_drawing()
        for i, point in enumerate(snow_center_list):
            if point.y > snow_length_list[i] and point.x < 600:
                sd.snowflake(center=point, length=snow_length_list[i])
            else:
                if point.y <= snow_length_list[i]:
                    sd.snowflake(center=point, length=snow_length_list[i])
                point.y = sd.random_number(600, 700)
                point.x = sd.random_number(-30, 600)
        sd.finish_drawing()

        sd.sleep(0.05)

        sd.start_drawing()
        for i, point in enumerate(snow_center_list):
            sd.snowflake(center=point, length=snow_length_list[i], color=sd.background_color)

        sd.finish_drawing()
        if sd.user_want_exit():
            break

        for i, snow in enumerate(snow_center_list):
            if snow_length_list[i] > 25:
                speed = 4
                acceleration = 2
            else:
                speed = 8
                acceleration = 1
            snow.y -= speed
            snow.x += acceleration + sd.random_number(-5, 5)


if __name__ == "__main__":
    christmas_snow()

    sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
