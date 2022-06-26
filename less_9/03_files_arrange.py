# -*- coding: utf-8 -*-

import time, shutil, os
import zipfile
from abc import abstractmethod, ABCMeta


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


# fl = {'file1':['year', 'mons'],
#       'file2':['year', 'mons'],
#         ..........
#       }

class SortByTime(metaclass=ABCMeta):

    def __init__(self):
        self.list_path_sort_file = {}

    @abstractmethod
    def _copy_files(self):
        pass

    @abstractmethod
    def _make_list_name_files(self):
        pass

    def _make_dir(self):
        for new_dir in self.list_path_sort_file.values():
            os.makedirs(new_dir, exist_ok=True)

    def sort_files(self):
        self._make_list_name_files()
        self._make_dir()
        self._copy_files()


class SortByTimeZip(SortByTime):

    def __init__(self, file_zip_name):
        super().__init__()
        self.file_zip_name = file_zip_name

    def _copy_files(self):
        with zipfile.ZipFile(self.file_zip_name) as my_zip:
            for member, path in self.list_path_sort_file.items():
                with my_zip.open(member) as source:
                    with open(os.path.join(path, os.path.basename(member)), 'wb') as target:
                        shutil.copyfileobj(source, target)

    def _make_list_name_files(self):
        _path = os.path.dirname(__file__)
        with zipfile.ZipFile(file=self.file_zip_name) as my_zip:
            my_list = [i for i in my_zip.namelist() if not i.endswith('/')]
            for file in my_list:
                date = my_zip.getinfo(file).date_time
                self.list_path_sort_file[file] = os.path.join(_path, str(date[0]), str(date[1]))


class SortByTimeDir(SortByTime):

    def __init__(self, dir_name):
        super().__init__()
        self.dir_name = dir_name

    def _make_list_name_files(self):
        _path = os.path.dirname(__file__)
        for dir_path, dir_names, file_name in os.walk(self.dir_name):
            for file in file_name:
                file = os.path.join(dir_path, file)
                date = time.gmtime(os.path.getmtime(file))
                self.list_path_sort_file[file] = os.path.join(_path, str(date[0]), str(date[1]))

    def _copy_files(self):
        for source, destination in self.list_path_sort_file.items():
            shutil.copy2(source, destination)


# with zipfile.ZipFile('icons.zip') as my_zip:
#     my_zip.extractall()
#
sort = SortByTimeZip(file_zip_name='icons.zip')
sort.sort_files()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
