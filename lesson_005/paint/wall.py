# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
from shapes import draw_triangle


def wall(point, width, height):
    for y in range(point.y, height, 25):
        x = point.x
        while x < width:
            if int(y / 5) % 2 == 0:
                left_bottom = sd.get_point(x, y)
                right_top = sd.get_point(x + 50, y + 25)
                sd.rectangle(left_bottom, right_top, width=1)
                x += 50
            else:
                if x == point.x or x + 25 >= width:
                    left_bottom = sd.get_point(x, y)
                    right_top = sd.get_point(x + 25, y + 25)
                    sd.rectangle(left_bottom, right_top, width=1)
                    x += 25
                else:
                    left_bottom = sd.get_point(x, y)
                    right_top = sd.get_point(x + 50, y + 25)
                    sd.rectangle(left_bottom, right_top, width=1)
                    x += 50
    sd.rectangle(point, sd.get_point(width, height), width=1)
    draw_triangle(start_point_x=point.x, start_point_y=height, lenght=width, angle=0)


if __name__ == '__main__':
    sd.set_screen_size(1200, 900)
    point = sd.get_point(100, 100)
    wall(point, 400, 350)


    sd.pause()

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
