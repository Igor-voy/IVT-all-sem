import math


def main():
    operand1 = float(input("Введите первое значение: "))
    operand2 = float(input("Введите второе значение: "))
    action = input("Введите действие: ")
    result = calculate(operand1, operand2, action)
    print("Результат = " + str(result))


def expo_pow(o1, o2):
    return math.pow(o1, o2)


def calculate(op1, op2, act):
    if ((type(op1) is int) or (type(op1) is float)) and ((type(op2) is int) or (type(op2) is float)):
        if act == '+':
            return op1 + op2
        elif act == '-':
            return op1 - op2
        elif act == '*':
            return op1 * op2
        elif act == '^':
            if (op1 == 0) and (op2 == 0):
                return "неопределенность"
            return expo_pow(op1, op2)
        elif act == '/':
            if op2 != 0:
                return op1 / op2
            else:
                return "деление на ноль невозможно"
        else:
            return "Операция не распознана"
    elif ((type(op1) is int) or (type(op1) is float)) and (type(op2) is str):
        return "ошибка во втором операнде"
    elif (type(op1) is str) and ((type(op2) is int) or (type(op2) is float)):
        return "ошибка в первом операнде"

main()

