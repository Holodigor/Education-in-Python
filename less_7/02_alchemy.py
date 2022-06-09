# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Air:
    def __str__(self):
        return f'Я воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Storm:
    def __str__(self):
        return f'Я шторм'

    def __add__(self, other):
        return None


class Lightning:
    def __str__(self):
        return f'Я молния'

    def __add__(self, other):
        return None


class Lava:
    def __str__(self):
        return f'Я лава'

    def __add__(self, other):
        return None


class Fire:
    def __str__(self):
        return f'Я огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Steam:
    def __str__(self):
        return f'Я пар'

    def __add__(self, other):
        return None


class Dust:
    def __str__(self):
        return f'Я пиль'

    def __add__(self, other):
        return None


class Earth:
    def __str__(self):
        return f'Я земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Steam()
        else:
            return None


class Dirt:
    def __str__(self):
        return f'Я грязь'

    def __add__(self, other):
        return None


class Water:
    def __str__(self):
        return f'Я вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


if __name__ == '__main__':
    print(Water(), '+', Air(), '=', Water() + Air())
    print(Fire(), '+', Air(), '=', Fire() + Air())
    print(Fire(), '+', Water(), '=', Fire() + Water())
    print(Fire(), '+', Earth(), '=', Fire() + Earth())
    print(Air(), '+', Lightning(), '=', Air() + Lightning())
    f = Fire()
    w = Water()
    res = f + w
    print(res)
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
