# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

height = 600
width = 600
sd.resolution = (width, height)

for y in range(0, height, 50):
    for x in range(0, width + 100, 100):
        if int(y/10) % 2 == 0:
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + 100, y + 50)
            sd.rectangle(left_bottom, right_top, width=1)
        else:
            left_bottom = sd.get_point(x - 50, y)
            right_top = sd.get_point(x - 50 + 100, y + 50)
            sd.rectangle(left_bottom, right_top, width=1)



# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


sd.pause()
