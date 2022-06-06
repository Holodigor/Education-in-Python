# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

from paint import draw_tree_sun_earth
from paint import rainbow
from paint import smile
from paint import snowfall
from paint import wall
import simple_draw as sd

sd.set_screen_size(1200, 800)
sd.background_color = sd.COLOR_BLUE
rainbow.rainbow()
draw_tree_sun_earth.draw_earth()

point_sun = sd.get_point(150, 700)
draw_tree_sun_earth.draw_sun(point=point_sun)

point_bilding = sd.get_point(300, 20)
wall.wall(point=point_bilding, width=400, height=400)

smile_point = sd.get_point(500, 220)
smile.smile(center_smile=smile_point)

point_tree = sd.get_point(800, 20)
draw_tree_sun_earth.draw_branches(point=point_tree, lenght=130)
point_tree = sd.get_point(850, 20)
draw_tree_sun_earth.draw_branches(point=point_tree, lenght=80)

snowfall.christmas_snow(wight=240, height=500, floor_height=sd.resolution[1] / 6)

sd.pause()
sd.quit()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
