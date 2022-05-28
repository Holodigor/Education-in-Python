# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные
from pprint import pprint


def paper_fit_in_envelope (envelop_x, envelop_y, paper_x, paper_y):
    if envelop_x >= paper_x and envelop_y >= paper_y:
        print('да')
        return 1
    elif envelop_y >= paper_x and envelop_x >= paper_y:
        print('да')
        return 1
    else:
        print('нет')
        return 1

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
pprint(f'envelop: {envelop_x} and {envelop_y} , paper:{paper_x} and {paper_y}')
paper_fit_in_envelope(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 9, 8
pprint(f'envelop: {envelop_x} and {envelop_y} , paper:{paper_x} and {paper_y}')
paper_fit_in_envelope(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 6, 8
pprint(f'envelop: {envelop_x} and {envelop_y} , paper:{paper_x} and {paper_y}')
paper_fit_in_envelope(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 8, 6
pprint(f'envelop: {envelop_x} and {envelop_y} , paper:{paper_x} and {paper_y}')
paper_fit_in_envelope(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 3, 4
pprint(f'envelop: {envelop_x} and {envelop_y} , paper:{paper_x} and {paper_y}')
paper_fit_in_envelope(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 11, 9
pprint(f'envelop: {envelop_x} and {envelop_y} , paper:{paper_x} and {paper_y}')
paper_fit_in_envelope(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 9, 11
pprint(f'envelop: {envelop_x} and {envelop_y} , paper:{paper_x} and {paper_y}')
paper_fit_in_envelope(envelop_x, envelop_y, paper_x, paper_y)
# (просто раскоментировать нужную строку и проверить свой код)



# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

# hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)


