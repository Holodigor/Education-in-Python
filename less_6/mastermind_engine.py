#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
from random import randint

from colorama import Style, Fore


def think_number():
    global secret_number
    secret_number = ''
    _number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(4):
        if i == 0:
            index = randint(1, len(_number_list)-1)
            secret_number += str(_number_list[index])
            _number_list.pop(index)
        else:
            index = randint(0, len(_number_list)-1)
            secret_number += str(_number_list[index])
            _number_list.pop(index)


def check_number(number):
    if number == secret_number:
        return 0
    else:
        my_dict = {'bulls': 0, 'cows': 0}
        for index, figure in enumerate(secret_number):
            if number[index] == figure:
                my_dict['bulls'] += 1
            elif figure in number:
                my_dict['cows'] += 1
        return my_dict


def correct_number(number):
    if len(number) == 4:
        if number[0] != number[1] != number[2] != number[3]:
            return True
        else:
            return False
    else:
        return False


def count_players():
    print(Style.BRIGHT + Fore.BLUE + "Выбирите режим игры: \n"
                                     " 1 : Один игрок \n"
                                     " 2 : Игрок против Игрока\nВвод: " + Style.RESET_ALL, end='')
    config = input()
    while True:
        if config == '1':
            config = False
            break
        elif config == '2':
            config = True
            break
        else:
            print(Style.BRIGHT + Fore.BLUE + "Выбирите верный режим игры: " + Style.RESET_ALL, end='')
            config = input()
    return config


if __name__ == "__main__":
    count_players()
    number = '1569'
    think_number()
    print('secret_number', secret_number)
    print('number', number)
    print(correct_number(number=number))
    print(check_number(number=number))