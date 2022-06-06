# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

# height = 600
# width = 900
# sd.resolution = (width, height)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# # Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# x1, y1 = 50 , 50
# x2, y2 = 350, 400
# for color in rainbow_colors:
#     point_1 = sd.get_point(x1, y1)
#     point_2 = sd.get_point(x2, y2)
#
#     sd.line(point_1, point_2, color, 8)
#     y1 += 10
#     y2 += 10
#
# sd.sleep(2)
# sd.clear_screen()


def rainbow(width=10):
    global color
    radius = sd.resolution[0]
    for color in rainbow_colors:
        point = sd.get_point(0, -100)
        sd.circle(point, radius, color, width=width)
        radius += width


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

if __name__ == '__main__':
    rainbow()
    sd.sleep(2)
    sd.quit()
