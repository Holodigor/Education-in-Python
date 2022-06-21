# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from abc import abstractmethod, ABCMeta
from os import walk, path, makedirs


# fl = {'file1':['year', 'mons'],
#       'file2':['year', 'mons'],
        ..........
#       }

class SortByTime(metaclass=ABCMeta):

    def __init__(self):
        self.list_name_files = []
        self.list_path_sort_file = {}
        pass

    def _copy_files(self):
        pass

    def _make_dir(self):
        _path = os.path.dirname(__file__)
        for file, data_list in self.list_path_sort_file:
            new_dir = os.path.join(_path, data_list[0], data_list[1])
            os.makedirs(new_dir, exist_ok=True )

    def _get_data_file(self):
        for file in self.list_name_files:
            os.path.getctime(

            )


    @abstractmethod
    def make_lis_name_files(self):
        pass

    def sort_files(self):
        pass


class UnZipFile:

    def __init__(self, file_name, file_zip_name):
        self.file_name = file_name
        self.file_zip_name = file_zip_name

    def _one_un_zip_file(self):
        pass

    def _all_un_zip_file(self):
        pass

    def un_un_zip_file(self):
        pass


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
