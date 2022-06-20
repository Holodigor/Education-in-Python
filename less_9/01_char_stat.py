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


class StatisticsLetters:

    def __init__(self, file_name):
        self.file = None
        self.file_name = file_name
        self.stat = {}

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
                        else:
                            self.stat[char] = 1

    def sort_stat(self):
        pass

    def write_in_file(self):
        n = 0
        with open('rez.txt', 'w', encoding='utf8') as file:
            file.write(f'+---------+----------+\n|{"Буква":^9}|{"Частота":^11}|\n+---------+----------+\n')
            for char, count in self.stat.items():
                n += count
                file.write(f'|{char:^9}|{count:11d}|\n')
            file.write(f'+---------+----------+\n|  итого  |{n:11d}|\n+---------+----------+')

    def write_on_console(self):
        n = 0
        print(f'+---------+----------+\n|{"Буква":^9}|{"Частота":^11}|\n+---------+----------+\n', end='')
        for char, count in self.stat.items():
            n += count
            print(f'|{char:^9}|{count:11d}|\n', end='')
        print(f'+---------+----------+\n|  итого  |{n:11d}|\n+---------+----------+', end='')



top = 'C:\\Users\\holod\\PycharmProjects\\Education-in-Python\\less_9'
stat = StatisticsLetters('voyna-i-mir.txt.zip')
stat.search_path(top)
stat.statistic()
stat.write_in_file()
stat.sort_stat()
stat.write_on_console()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
