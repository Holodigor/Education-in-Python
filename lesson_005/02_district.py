# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import room_1
import room_2

people_list = room_1.folks + room_2.folks
people_string = ', '.join([i for i in people_list])
print('На районе живут ',people_string)






