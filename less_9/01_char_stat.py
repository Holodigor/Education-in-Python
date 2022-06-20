# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile
import os
from abc import ABCMeta, abstractmethod


class StatisticsLetters:

    def __init__(self, file_name):
        self.file = None
        self.file_name = file_name
        self.stat = {}
        self.total_char = 0

    def search_path(self, path_dir='c:\\'):
        path = os.path.normpath(path_dir)
        for dirpath, dirnames, filenames in os.walk(top=path):
            if self.file_name in filenames:
                self.file = os.path.join(dirpath, self.file_name)

    def _zip_file(self):
        zfile = zipfile.ZipFile(self.file, mode='r')
        path = os.path.dirname(__file__)
        self.file_name = self.file_name[:-4]
        zfile.extract(self.file_name, path=path)
        self.file = self.file_name

    def statistic(self):
        if self.file.endswith('.zip'):
            self._zip_file()
        with open(file=self.file, mode='r') as file:
            for line in file.readlines():
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += line.count(char)
                            self.total_char += 1
                        else:
                            self.stat[char] = 1
                            self.total_char += 1

    def write_in_file(self):
        with open('rez.txt', 'w', encoding='utf8') as file:
            file.write(f'+---------+-----------+\n|{"Буква":^9}|{"Частота":^11}|\n+---------+-----------+\n')
            for char, count in self.stat.items():
                file.write(f'|{char:^9}|{count:11d}|\n')
            file.write(f'+---------+----------+\n|  итого  |{self.total_char:11d}|\n+---------+-----------+')
        os.startfile('rez.txt')

    def write_on_console(self):
        print(f'\n+---------+----------+\n|{"Буква":^9}|{"Частота":^11}|\n+---------+-----------+\n', end='')
        for char, count in self.stat.items():
            print(f'|{char:^9}|{count:11d}|\n', end='')
        print(f'+---------+----------+\n|  итого  |{self.total_char:11d}|\n+---------+----------+', end='')


class SortedDict(metaclass=ABCMeta):
    def __init__(self, my_dict):
        self.my_dict = my_dict
        self.my_list = []

    def _make_list(self):
        for kay, value in self.my_dict.items():
            self.my_list.append([kay, value])

    def _make_dict(self):
        self.my_dict = {}
        for i in self.my_list:
            if str(i[0]).isalpha():
                self.my_dict[i[0]] = i[1]
            else:
                self.my_dict[i[1]] = i[0]

    @abstractmethod
    def sorted_dict(self):
        pass


class FrequencyAscending(SortedDict):  # по частоте по возрастанию

    def sorted_dict(self):
        self._make_list()
        for i in self.my_list:
            i[0], i[1] = i[1], i[0]
        self.my_list = sorted(self.my_list)
        self._make_dict()
        return self.my_dict


class AlphabeticallyAscending(SortedDict):  # - по алфавиту по возрастанию

    def sorted_dict(self):
        self._make_list()
        self.my_list = sorted(self.my_list)
        self._make_dict()
        return self.my_dict


class AlphabeticallyDescending(SortedDict):  # - по алфавиту по убыванию

    def sorted_dict(self):
        self._make_list()
        self.my_list = sorted(self.my_list, reverse=True)
        self._make_dict()
        return self.my_dict


top = r'C:\Users\holod\PycharmProjects\Education-in-Python\less_9'
stat = StatisticsLetters('voyna-i-mir.txt.zip')
stat.search_path(top)
stat.statistic()
stat.stat = AlphabeticallyDescending(stat.stat).sorted_dict()
stat.write_on_console()
stat.stat = AlphabeticallyAscending(stat.stat).sorted_dict()
stat.write_on_console()
stat.stat = FrequencyAscending(stat.stat).sorted_dict()
stat.write_on_console()
stat.write_in_file()
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
