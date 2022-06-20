# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import os


class AnalysisLogFile:
    _group_dict = {'minet': -16,
                   'day': -22,
                   'mons': -25,
                   'year': -28}

    def __init__(self, log_file, rez_log_file='rez_log_file.txt'):
        self.log_file = log_file
        self.rez_log_file = rez_log_file

    def _write_rez_log_file(self, line):
        with open(self.rez_log_file, 'a') as rez_log_file:
            rez_log_file.write(line)

    def _analysis_log_file(self, group=_group_dict['minet']):
        group = group
        if os.path.exists(self.rez_log_file):
            os.remove(self.rez_log_file)
        with open(self.log_file, 'r') as log_file:
            count_NOK = 0
            line_next = ''
            for line in log_file.readlines():
                if line.endswith('NOK\n'):
                    if line_next == '':
                        line_next = line[:group]
                        count_NOK += 1
                    else:
                        if line_next == line[:group]:
                            count_NOK += 1
                        else:
                            self._write_rez_log_file(line_next + '] ' + str(count_NOK) + '\n')
                            line_next = line[:group]
                            count_NOK = 1
            else:
                self._write_rez_log_file(line_next + '] ' + str(count_NOK) + '\n')
        os.startfile(self.rez_log_file)

    def group_by_year(self):
        self._analysis_log_file(group=AnalysisLogFile._group_dict['year'])

    def group_by_mons(self):
        self._analysis_log_file(group=AnalysisLogFile._group_dict['mons'])

    def group_by_day(self):
        self._analysis_log_file(group=AnalysisLogFile._group_dict['day'])


if __name__ == '__main__':
    log = AnalysisLogFile(log_file='events.txt')
    # log.group_by_year()
    # log.group_by_mons()
    log.group_by_day()
    # log._analysis_log_file()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
