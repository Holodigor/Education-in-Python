# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


def wall(point, width, height):
    sd.rectangle(point, sd.get_point(width + point.x, height + point.y), width=0, color=sd.COLOR_DARK_RED)
    for y in range(point.y, height + point.y, 25):
        x = point.x
        while x < width + point.x:
            if int(y / 5) % 2 == 0:
                left_bottom = sd.get_point(x, y)
                right_top = sd.get_point(x + 50, y + 25)
                sd.rectangle(left_bottom, right_top, width=1, color=sd.COLOR_BLACK)
                x += 50
            else:
                if x == point.x or x + 25 >= width + point.x:
                    left_bottom = sd.get_point(x, y)
                    right_top = sd.get_point(x + 25, y + 25)
                    sd.rectangle(left_bottom, right_top, width=1, color=sd.COLOR_BLACK)
                    x += 25
                else:
                    left_bottom = sd.get_point(x, y)
                    right_top = sd.get_point(x + 50, y + 25)
                    sd.rectangle(left_bottom, right_top, width=1, color=sd.COLOR_BLACK)
                    x += 50
    sd.rectangle(point, sd.get_point(width + point.x, height + point.y), width=3, color=sd.COLOR_BLACK)
    sd.polygon([sd.get_point(point.x - 10, point.y + height),
                sd.get_point(point.x + width + 10, point.y + height),
                sd.get_point(point.x + width / 2, point.y + height + height / 2)],
               color=sd.COLOR_DARK_ORANGE, width=0)
    sd.rectangle(left_bottom=sd.get_point(point.x + width / 2 - width / 5, point.y + height / 2 - height / 5),
                 right_top=sd.get_point(point.x + width / 2 + width / 5, point.y + height / 2 + height / 5),
                 color=sd.background_color, width=0)
    sd.rectangle(left_bottom=sd.get_point(point.x + width / 2 - width / 5, point.y + height / 2 - height / 5),
                 right_top=sd.get_point(point.x + width / 2 + width / 5, point.y + height / 2 + height / 5),
                 width=4, color=sd.COLOR_BLACK)


if __name__ == '__main__':
    sd.set_screen_size(1200, 900)
    point = sd.get_point(200, 300)
    wall(point, 400, 100)

    sd.pause()

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
