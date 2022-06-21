import calcprint
import time
import sys
import math

PARAMS = {'precision': None,
          'output_type': None,
          'possible_types': None,
          'dest': None}


def load_params(file="params.ini"):
    '''
        Функция записи параметров из файла в словарь PARAMS
        На вход поступает имя файла, в процессе выполнения 
        Параметры построчно записываются в PARAMS. 
        Функция ничего не возвращает
    '''
    global PARAMS
    try:
        f = open(file, mode='r', errors='ignore')
        lines = f.readlines()
        for l in lines:
            param = l.split('=')
            param[1] = param[1].strip('\n')
            if (param[0] != 'dest'):
                param[1] = eval(param[1])

            PARAMS[param[0]] = param[1]
        f.close()
    except FileNotFoundError:
        print("Файл с параметрами не найден, проверьте наличие файла 'params.ini'!")


def convert_precision(p):
    ''' 
        Функция, конвертирующая заданную точность:
        0.000001 -> 6

        >>> convert_precision(0.000001)
        6
        >>> convert_precision(0.0001)
        4
        >>> convert_precision(0.001)
        3
    '''
    score = 0
    while (p < 1):
        p *= 10
        score += 1
    return score


def user_input():
    args = []
    global PARAMS

    action = input("Введите действие\n Доступные действия: +, -, *, /, ^, log \n")
    if(action not in [ '+', '-', '*', '/', '^', 'log']):
        print('Недопустимое действие')
        sys.exit()
    while True:
        value = input("Введите число: ")
        try:
            if value == "":
                break
            value = float(value)
        except ValueError:
            print("Неправильный формат, разделитель '.'!")
        else:
            args.append(value)

    print(args)
    if len(args) <= 1:
        return

    res = calculate(*args, action, **PARAMS)
    calcprint.print_results(*args, action=action, result=res)
    calcprint.write_log(*args, action=action, result=res)


def calculate(*args, **kwargs):
    '''
        Функция-калькулятор. На вход поступают:
        операнды, действие и словарь с параметрами

        Доступные операции:
       '+'   '-'   '*'   '/'   'other'
    '''
    precision = convert_precision(kwargs['precision'])
    output_type = kwargs['output_type']

    action = args[-1]

    if (action == '+'):
        result_sum = sum(args[0:len(args) - 1])
        if type(result_sum) is not output_type:
            result_sum = output_type(result_sum)
        return round(result_sum, precision)

    if (action == '-'):
        result_diff = args[0]
        for n in args[1:len(args) - 1]:
            result_diff -= n
        if type(result_diff) is not output_type:
            result_diff = output_type(result_diff)
        return round(result_diff, precision)

    if (action == '*'):
        res = 1
        for n in args[0:len(args) - 1]:
            res *= n
        return round(res, precision)

    if (action == '/'):
        try:
            result_division = args[0]
            for n in args[1:len(args) - 1]:
                result_division /= n
            if type(result_division) is not output_type:
                result_division = output_type(result_division)
            return round(result_division, precision)
        except ZeroDivisionError:
            print('Деление на ноль!!!\n '
                  'Программа приостановлена')
            sys.exit()

    if (action == '^'):
        res = 1
        for n in args[1:len(args) - 1]:
            res *= n
        return pow(args[0], res)

    if (action == 'log'):
        if (len(args) > 3):
            print('Введите два значения')
            sys.exit()
        else:
            x = args[0]
            base = args[1]
            if ((base > 0 and base != 1) and (x > 0)):
                return math.log(x, base)
            else:
                print('Не удовлетворяет ОДЗ')
                sys.exit()

if __name__ == "__main__":
    load_params()
    user_input()
